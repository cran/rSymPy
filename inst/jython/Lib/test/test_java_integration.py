import os
import unittest
import subprocess
import sys
import re
 
from test import test_support

from java.lang import (ExceptionInInitializerError, String, Runnable, System, Runtime, Math, Byte)
from java.math import BigDecimal
from java.io import (FileInputStream, FileNotFoundException, FileOutputStream, FileWriter,
    OutputStreamWriter, UnsupportedEncodingException)
from java.util import ArrayList, Date, HashMap, Hashtable, StringTokenizer, Vector

from java.awt import Dimension, Color, Component, Container
from java.awt.event import ComponentEvent
from javax.swing.tree import TreePath

from org.python.core.util import FileUtil
from org.python.tests import BeanImplementation, Listenable

class InstantiationTest(unittest.TestCase):
    def test_cant_instantiate_abstract(self):
        self.assertRaises(TypeError, Component)

    def test_no_public_constructors(self):
        self.assertRaises(TypeError, Math)

    def test_invalid_self_to_java_constructor(self):
        self.assertRaises(TypeError, Color.__init__, 10, 10, 10)

    def test_str_doesnt_coerce_to_int(self):
        self.assertRaises(TypeError, Date, '99-01-01', 1, 1)

class BeanTest(unittest.TestCase):
    def test_shared_names(self):
        self.failUnless(callable(Vector.size),
                'size method should be preferred to writeonly field')

    def test_multiple_listeners(self):
        '''Check that multiple BEP can be assigned to a single cast listener'''
        m = Listenable()
        called = []
        def f(evt, called=called):
            called.append(0)

        m.componentShown = f
        m.componentHidden = f

        m.fireComponentShown(ComponentEvent(Container(), 0))
        self.assertEquals(1, len(called))
        m.fireComponentHidden(ComponentEvent(Container(), 0))
        self.assertEquals(2, len(called))
    
    def test_bean_interface(self):
        b = BeanImplementation()
        self.assertEquals("name", b.getName())
        self.assertEquals("name", b.name)


class SysIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.orig_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.orig_stdout

    def test_stdout_outputstream(self):
        out = FileOutputStream(test_support.TESTFN)
        sys.stdout = out
        print 'hello',
        out.close()
        f = open(test_support.TESTFN)
        self.assertEquals('hello', f.read())
        f.close()
                
class IOTest(unittest.TestCase):
    def test_io_errors(self):
        "Check that IOException isn't mangled into an IOError"
        self.assertRaises(UnsupportedEncodingException, OutputStreamWriter, System.out, "garbage")
        self.assertRaises(IOError, OutputStreamWriter, System.out, "garbage")

    def test_fileio_error(self):
        self.assertRaises(FileNotFoundException, FileInputStream, "garbage")

    def test_unsupported_tell(self):
        fp = FileUtil.wrap(System.out)
        self.assertRaises(IOError, fp.tell)


class JavaReservedNamesTest(unittest.TestCase):
    "Access to reserved words"

    def test_system_in(self):
        s = System.in
        self.assert_("java.io.BufferedInputStream" in str(s))
             
    def test_runtime_exec(self):
        e = Runtime.getRuntime().exec
        self.assert_(re.search("method .*exec", str(e)) is not None)
                       
    def test_byte_class(self):
        b = Byte(10)
        self.assert_("java.lang.Byte" in str(b.class))

class Keywords(object):
    pass

Keywords.in = lambda self: "in"
Keywords.exec = lambda self: "exec"
Keywords.class = lambda self: "class"
Keywords.print = lambda self: "print"
Keywords.and = lambda self: "and"
Keywords.as = lambda self: "as"
Keywords.assert = lambda self: "assert"
Keywords.break = lambda self: "break"
Keywords.continue = lambda self: "continue"
Keywords.def = lambda self: "def"
Keywords.del = lambda self: "del"
Keywords.elif = lambda self: "elif"
Keywords.else = lambda self: "else"
Keywords.except = lambda self: "except"
Keywords.finally = lambda self: "finally"
Keywords.from = lambda self: "from"
Keywords.for = lambda self: "for"
Keywords.global = lambda self: "global"
Keywords.if = lambda self: "if"
Keywords.import = lambda self: "import"
Keywords.is = lambda self: "is"
Keywords.lambda = lambda self: "lambda"
Keywords.pass = lambda self: "pass"
Keywords.print = lambda self: "print"
Keywords.raise = lambda self: "raise"
Keywords.return = lambda self: "return"
Keywords.try = lambda self: "try"
Keywords.while = lambda self: "while"
Keywords.with = lambda self: "with"
Keywords.yield = lambda self: "yield"

class PyReservedNamesTest(unittest.TestCase):
    "Access to reserved words"

    def setUp(self):
        self.kws = Keywords()

    def test_in(self):
        self.assertEquals(self.kws.in(), "in")
    
    def test_exec(self):
        self.assertEquals(self.kws.exec(), "exec")

    def test_class(self):
        self.assertEquals(self.kws.class(), "class")

    def test_print(self):
        self.assertEquals(self.kws.print(), "print")

    def test_and(self):
        self.assertEquals(self.kws.and(), "and")

    def test_as(self):
        self.assertEquals(self.kws.as(), "as")

    def test_assert(self):
        self.assertEquals(self.kws.assert(), "assert")

    def test_break(self):
        self.assertEquals(self.kws.break(), "break")

    def test_continue(self):
        self.assertEquals(self.kws.continue(), "continue")

    def test_def(self):
        self.assertEquals(self.kws.def(), "def")

    def test_del(self):
        self.assertEquals(self.kws.del(), "del")

    def test_elif(self):
        self.assertEquals(self.kws.elif(), "elif")

    def test_else(self):
        self.assertEquals(self.kws.else(), "else")

    def test_except(self):
        self.assertEquals(self.kws.except(), "except")

    def test_finally(self):
        self.assertEquals(self.kws.finally(), "finally")

    def test_from(self):
        self.assertEquals(self.kws.from(), "from")

    def test_for(self):
        self.assertEquals(self.kws.for(), "for")

    def test_global(self):
        self.assertEquals(self.kws.global(), "global")

    def test_if(self):
        self.assertEquals(self.kws.if(), "if")

    def test_import(self):
        self.assertEquals(self.kws.import(), "import")

    def test_is(self):
        self.assertEquals(self.kws.is(), "is")

    def test_lambda(self):
        self.assertEquals(self.kws.lambda(), "lambda")

    def test_pass(self):
        self.assertEquals(self.kws.pass(), "pass")

    def test_print(self):
        self.assertEquals(self.kws.print(), "print")

    def test_raise(self):
        self.assertEquals(self.kws.raise(), "raise")

    def test_return(self):
        self.assertEquals(self.kws.return(), "return")

    def test_try(self):
        self.assertEquals(self.kws.try(), "try")

    def test_while(self):
        self.assertEquals(self.kws.while(), "while")

    def test_with(self):
        self.assertEquals(self.kws.with(), "with")

    def test_yield(self):
        self.assertEquals(self.kws.yield(), "yield")

class ImportTest(unittest.TestCase):
    def test_bad_input_exception(self):
        self.assertRaises(ValueError, __import__, '')

    def test_broken_static_initializer(self):
        self.assertRaises(ExceptionInInitializerError, __import__, "org.python.tests.BadStaticInitializer")

class ColorTest(unittest.TestCase):
    def test_assigning_over_method(self):
        self.assertRaises(TypeError, setattr, Color.RED, "getRGB", 4)

    def test_static_fields(self):
        self.assertEquals(Color(255, 0, 0), Color.RED)
        # The bean accessor for getRed should be active on instances, but the static field red 
        # should be visible on the class
        self.assertEquals(255, Color.red.red)
        self.assertEquals(Color(0, 0, 255), Color.blue)

    def test_is_operator(self):
        red = Color.red
        self.assert_(red is red)
        self.assert_(red is Color.red)

class TreePathTest(unittest.TestCase):
    def test_overloading(self):
        treePath = TreePath([1,2,3])
        self.assertEquals(len(treePath.path), 3, "Object[] not passed correctly")
        self.assertEquals(TreePath(treePath.path).path, treePath.path, "Object[] not passed and returned correctly")

class BigDecimalTest(unittest.TestCase):
    def test_coerced_bigdecimal(self):
        from javatests import BigDecimalTest
        x = BigDecimal("123.4321")
        y = BigDecimalTest().asBigDecimal()

        self.assertEqual(type(x), type(y), "BigDecimal coerced")
        self.assertEqual(x, y, "coerced BigDecimal not equal to directly created version")

class JavaStringTest(unittest.TestCase):
    def test_string_not_iterable(self):
        x = String('test')
        self.assertRaises(TypeError, list, x)

class JavaDelegationTest(unittest.TestCase):
    def test_list_delegation(self):
        for c in ArrayList, Vector:
            a = c()
            self.assertRaises(IndexError, a.__getitem__, 0)
            a.add("blah")
            self.assertTrue("blah" in a)
            self.assertEquals(1, len(a))
            n = 0
            for i in a:
                n += 1
                self.assertEquals("blah", i)
            self.assertEquals(1, n)
            self.assertEquals("blah", a[0])
            a[0] = "bleh"
            del a[0]
            self.assertEquals(0, len(a))

    def test_map_delegation(self):
        m = HashMap()
        m["a"] = "b"
        self.assertTrue("a" in m)
        self.assertEquals("b", m["a"])
        n = 0
        for k in m:
            n += 1
            self.assertEquals("a", k)
        self.assertEquals(1, n)
        del m["a"]
        self.assertEquals(0, len(m))

    def test_enumerable_delegation(self):
        tokenizer = StringTokenizer('foo bar')
        self.assertEquals(list(iter(tokenizer)), ['foo', 'bar'])

    def test_vector_delegation(self):
        class X(Runnable):
            pass
        v = Vector()
        v.addElement(1)
        v.indexOf(X())# Compares the Java object in the vector to a Python subclass
        for i in v:
            pass

class SecurityManagerTest(unittest.TestCase):
    def test_nonexistent_import_with_security(self):
        policy = test_support.findfile("python_home.policy")
        script = test_support.findfile("import_nonexistent.py")
        self.assertEquals(subprocess.call([sys.executable,  "-J-Dpython.cachedir.skip=true",
            "-J-Djava.security.manager", "-J-Djava.security.policy=%s" % policy, script]),
            0)

def test_main():
    test_support.run_unittest(InstantiationTest, 
                              BeanTest, 
                              SysIntegrationTest,
                              IOTest,
                              JavaReservedNamesTest,
                              PyReservedNamesTest,
                              ImportTest,
                              ColorTest,
                              TreePathTest,
                              BigDecimalTest,
                              JavaStringTest,
                              JavaDelegationTest,
                              SecurityManagerTest)

if __name__ == "__main__":
    test_main()
