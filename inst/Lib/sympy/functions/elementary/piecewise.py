
from sympy.core.basic import Basic, S
from sympy.core.function import Function, diff
from sympy.core.numbers import Number
from sympy.core.relational import Relational
from sympy.core.sympify import sympify

from sympy.utilities.decorator import deprecated

class ExprCondPair(Basic):
    """Represents an expression, condition pair."""

    def __new__(cls, expr, cond, **assumptions):
        expr = sympify(expr)
        cond = sympify(cond)
        return Basic.__new__(cls, expr, cond, **assumptions)

    @property
    def expr(self):
        return self.args[0]

    @property
    def cond(self):
        return self.args[1]

    def __iter__(self):
        yield self.expr
        yield self.cond


class Piecewise(Function):
    """
    Represents a piecewise function.

    Usage
    =====
      Piecewise( (expr,cond), (expr,cond), ... )
        - Each argument is a 2-tuple defining a expression and condition
        - The conds are evaluated in turn returning the first that is True.
          If any of the evaluated conds are not determined explicitly False,
          e.g. x < 1, the function is returned in symbolic form.
        - If the function is evaluated at a place where all conditions are False,
          a ValueError exception will be raised.
        - Pairs where the cond is explicitly False, will be removed.

    Examples
    ========
      >>> from sympy import *
      >>> x = Symbol('x')
      >>> f = x**2
      >>> g = log(x)
      >>> p = Piecewise( (0, x<-1), (f, x<=1), (g, True))
      >>> p.subs(x,1)
      1
      >>> p.subs(x,5)
      log(5)
    """

    nargs=None

    def __new__(cls, *args, **options):
        # Check types first
        for ec in args:
            if not isinstance(ec, tuple) or len(ec) != 2:
                raise TypeError, "args may only include (expr, cond) pairs"
            cond_type = type(ec[1])
            if not (cond_type is bool or issubclass(cond_type, Relational) or \
                    issubclass(cond_type, Number)):
                raise TypeError, \
                    "Cond %s is of type %s, but must be a bool," \
                    " Relational or Number" % (ec[1], cond_type)

        # sympify args
        args = map(lambda x:ExprCondPair(*x), args)

        r = cls.eval(*args)

        if r is None:
            return Basic.__new__(cls, *args, **options)
        else:
            return r

    def __getnewargs__(self):
        # Convert ExprCondPair objects to tuples.
        args = []
        for expr, condition in self.args:
            args.append((expr, condition))
        return tuple(args)

    @classmethod
    @deprecated
    def canonize(cls, *args):
        return cls.eval(*args)

    @classmethod
    def eval(cls, *args):
        # Check for situations where we can evaluate the Piecewise object.
        # 1) Hit an unevaluatable cond (e.g. x<1) -> keep object
        # 2) Hit a true condition -> return that expr
        # 3) Remove false conditions, if no conditions left -> raise ValueError
        all_conds_evaled = True
        non_false_ecpairs = []
        for expr, cond in args:
            cond_eval = cls.__eval_cond(cond)
            if cond_eval is None:
                all_conds_evaled = False
                non_false_ecpairs.append( (expr, cond) )
            elif cond_eval:
                if all_conds_evaled:
                    return expr
                non_false_ecpairs.append( (expr, cond) )
        if len(non_false_ecpairs) != len(args):
            return Piecewise(*non_false_ecpairs)

        # Count number of arguments.
        nargs = 0
        for expr, cond in args:
            if hasattr(expr, 'nargs'):
                nargs = max(nargs, expr.nargs)
            elif hasattr(expr, 'args'):
                nargs = max(nargs, len(expr.args))
        if nargs:
            cls.narg = nargs
        return None

    def doit(self, **hints):
        return Piecewise(*[(e.doit(), c.doit()) for e, c in self.args])

    def _eval_integral(self,x):
        from sympy.integrals import integrate
        return  Piecewise(*[(integrate(e, x), c) for e, c in self.args])

    def _eval_interval(self, sym, a, b):
        """Evaluates the function along the sym in a given interval ab"""
        # FIXME: Currently only supports conds of type sym < Num, or Num < sym
        int_expr = []
        mul = 1
        if a > b:
            a, b, mul = b, a, -1
        default = None

        # Determine what intervals the expr,cond pairs affect.
        # 1) If cond is True, then log it as default
        # 1.1) Currently if cond can't be evaluated, throw NotImplentedError.
        # 2) For each inequality, if previous cond defines part of the interval
        #    update the new conds interval.
        #    -  eg x < 1, x < 3 -> [oo,1],[1,3] instead of [oo,1],[oo,3]
        # 3) Sort the intervals to make it easier to find correct exprs
        for expr, cond in self.args:
            if isinstance(cond, bool) or cond.is_Number:
                if cond:
                    default = expr
                    break
                else:
                    continue
            curr = list(cond.args)
            if cond.args[0] == sym:
                curr[0] = S.NegativeInfinity
            elif cond.args[1] == sym:
                curr[1] = S.Infinity
            else:
                raise NotImplementedError, \
                    "Currently only supporting evaluation with only " \
                    "sym on one side of the relation."
            curr = [max(a, curr[0]), min(b, curr[1])]
            for n in xrange(len(int_expr)):
                if self.__eval_cond(curr[0] < int_expr[n][1]) and \
                        self.__eval_cond(curr[0] >= int_expr[n][0]):
                    curr[0] = int_expr[n][1]
                if self.__eval_cond(curr[1] > int_expr[n][0]) and \
                        self.__eval_cond(curr[1] <= int_expr[n][1]):
                    curr[1] = int_expr[n][0]
            if self.__eval_cond(curr[0] < curr[1]):
                int_expr.append(curr + [expr])
        int_expr.sort(key=lambda x:x[0])

        # Add holes to list of intervals if there is a default value,
        # otherwise raise a ValueError.
        holes = []
        curr_low = a
        for int_a, int_b, expr in int_expr:
            if curr_low < int_a:
                holes.append([curr_low, min(b, int_a), default])
            curr_low = int_b
            if curr_low > b:
                break
        if holes and default != None:
            int_expr.extend(holes)
        elif holes and default == None:
            raise ValueError, "Called interval evaluation over piecewise " \
                              "function on undefined intervals %s" % \
                              ", ".join([str((h[0], h[1])) for h in holes])

        # Finally run through the intervals and sum the evaluation.
        ret_fun = 0
        for int_a, int_b, expr in int_expr:
            ret_fun += expr._eval_interval(sym,  max(a, int_a), min(b, int_b))
        return mul * ret_fun

    def _eval_derivative(self, s):
        return Piecewise(*[(diff(e, s), c) for e, c in self.args])

    def _eval_subs(self, old, new):
        if self == old:
            return new
        new_args = []
        for e, c in self.args:
            if isinstance(c, bool):
                new_args.append((e._eval_subs(old, new), c))
            else:
                new_args.append((e._eval_subs(old, new), c._eval_subs(old, new)))
        return Piecewise( *new_args )

    @classmethod
    def __eval_cond(cls, cond):
        """Returns S.One if True, S.Zero if False, or None if undecidable."""
        if type(cond) == bool or cond.is_number or (cond.args[0].is_Number and cond.args[1].is_Number):
            if cond: return S.One
            return S.Zero
        return None

