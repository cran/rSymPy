from sympy.concrete.products import Product
from sympy.concrete.summations import Sum
from sympy.core.function import Derivative
from sympy.core.numbers import Integer, Rational, Real
from sympy.core.relational import Rel
from sympy.core.symbol import symbols
from sympy.functions import sin
from sympy.integrals.integrals import Integral
from sympy.series.order import Order

from sympy.printing.precedence import precedence, PRECEDENCE

x, y = symbols("xy")

def test_Add():
    assert precedence(x+y) == PRECEDENCE["Add"]
    assert precedence(x*y+1) == PRECEDENCE["Add"]

def test_Function():
    assert precedence(sin(x)) == PRECEDENCE["Atom"]
    assert precedence(Derivative(x,y)) == PRECEDENCE["Atom"]

def test_Integral():
    assert precedence(Integral(x,y)) == PRECEDENCE["Atom"]

def test_Mul():
    assert precedence(x*y) == PRECEDENCE["Mul"]
    assert precedence(-x*y) == PRECEDENCE["Add"]

def test_Number():
    assert precedence(Integer(0)) == PRECEDENCE["Atom"]
    assert precedence(Integer(1)) == PRECEDENCE["Atom"]
    assert precedence(Integer(-1)) == PRECEDENCE["Add"]
    assert precedence(Integer(10)) == PRECEDENCE["Atom"]
    assert precedence(Rational(5,2)) == PRECEDENCE["Mul"]
    assert precedence(Rational(-5,2)) == PRECEDENCE["Add"]
    assert precedence(Real(5)) == PRECEDENCE["Atom"]
    assert precedence(Real(-5)) == PRECEDENCE["Add"]

def test_Order():
    assert precedence(Order(x)) == PRECEDENCE["Atom"]

def test_Pow():
    assert precedence(x**y) == PRECEDENCE["Pow"]
    assert precedence(-x**y) == PRECEDENCE["Add"]
    assert precedence(x**-y) == PRECEDENCE["Pow"]

def test_Product():
    assert precedence(Product(x,(x,y,y+1))) == PRECEDENCE["Atom"]

def test_Relational():
    assert precedence(Rel(x+y,y,"<")) == PRECEDENCE["Relational"]

def test_Sum():
    assert precedence(Sum(x,(x,y,y+1))) == PRECEDENCE["Atom"]

def test_Symbol():
    assert precedence(x) == PRECEDENCE["Atom"]
