# -*- coding: utf-8 -*-
"""Misc unicode tests

Made for Jython.
"""
import re
import sys
import unittest
from test import test_support

class UnicodeTestCase(unittest.TestCase):

    def test_simplejson_plane_bug(self):
        # a bug exposed by simplejson: unicode __add__ was always
        # forcing the basic plane
        chunker = re.compile(r'(.*?)(["\\\x00-\x1f])', re.VERBOSE | re.MULTILINE | re.DOTALL)
        orig = u'z\U0001d120x'
        quoted1 = u'"z\U0001d120x"'
        quoted2 = '"' + orig + '"'
        # chunker re gives different results depending on the plane
        self.assertEqual(chunker.match(quoted1, 1).groups(), (orig, u'"'))
        self.assertEqual(chunker.match(quoted2, 1).groups(), (orig, u'"'))

    def test_parse_unicode(self):
        foo = u'ą\n'
        self.assertEqual(len(foo), 2, repr(foo))
        self.assertEqual(repr(foo), "u'\\u0105\\n'")
        self.assertEqual(ord(foo[0]), 261)
        self.assertEqual(ord(foo[1]), 10)

        bar = foo.encode('utf-8')
        self.assertEqual(len(bar), 3)
        self.assertEqual(repr(bar), "'\\xc4\\x85\\n'")
        self.assertEqual(ord(bar[0]), 196)
        self.assertEqual(ord(bar[1]), 133)
        self.assertEqual(ord(bar[2]), 10)

    def test_parse_raw_unicode(self):
        foo = ur'ą\n'
        self.assertEqual(len(foo), 3, repr(foo))
        self.assertEqual(repr(foo), "u'\\u0105\\\\n'")
        self.assertEqual(ord(foo[0]), 261)
        self.assertEqual(ord(foo[1]), 92)
        self.assertEqual(ord(foo[2]), 110)

        bar = foo.encode('utf-8')
        self.assertEqual(len(bar), 4)
        self.assertEqual(repr(bar), "'\\xc4\\x85\\\\n'")
        self.assertEqual(ord(bar[0]), 196)
        self.assertEqual(ord(bar[1]), 133)
        self.assertEqual(ord(bar[2]), 92)
        self.assertEqual(ord(bar[3]), 110)

    def test_encode_decimal(self):
        self.assertEqual(int(u'\u0039\u0032'), 92)
        self.assertEqual(int(u'\u0660'), 0)
        self.assertEqual(int(u' \u001F\u0966\u096F\u0039'), 99)
        self.assertEqual(long(u'\u0663'), 3)
        self.assertEqual(float(u'\u0663.\u0661'), 3.1)
        self.assertEqual(complex(u'\u0663.\u0661'), 3.1+0j)

    def test_formatchar(self):
        self.assertEqual('%c' % 255, '\xff')
        self.assertRaises(OverflowError, '%c'.__mod__, 256)

        result = u'%c' % 256
        self.assert_(isinstance(result, unicode))
        self.assertEqual(result, u'\u0100')
        if sys.maxunicode == 0xffff:
            self.assertEqual(u'%c' % sys.maxunicode, u'\uffff')
        else:
            self.assertEqual(u'%c' % sys.maxunicode, u'\U0010ffff')
        self.assertRaises(OverflowError, '%c'.__mod__, sys.maxunicode + 1)

    def test_repr(self):
        self.assert_(isinstance('%r' % u'foo', str))

    def test_concat(self):
        self.assertRaises(UnicodeDecodeError, lambda : u'' + '毛泽东')
        self.assertRaises(UnicodeDecodeError, lambda : '毛泽东' + u'')

    def test_join(self):
        self.assertRaises(UnicodeDecodeError, u''.join, ['foo', '毛泽东'])
        self.assertRaises(UnicodeDecodeError, '毛泽东'.join, [u'foo', u'bar'])

    def test_file_encoding(self):
        '''Ensure file writing doesn't attempt to encode things by default and reading doesn't
        decode things by default.  This was jython's behavior prior to 2.2.1'''
        EURO_SIGN = u"\u20ac"
        try:
            EURO_SIGN.encode()
        except UnicodeEncodeError:
            # This default encoding can't handle the encoding the Euro sign.  Skip the test
            return

        f = open(test_support.TESTFN, "w")
        self.assertRaises(UnicodeEncodeError, f, write, EURO_SIGN, 
                "Shouldn't be able to write out a Euro sign without first encoding")
        f.close()

        f = open(test_support.TESTFN, "w")
        f.write(EURO_SIGN.encode('utf-8'))
        f.close()

        f = open(test_support.TESTFN, "r")
        encoded_euro = f.read()
        f.close()
        os.remove(test_support.TESTFN)
        self.assertEquals('\xe2\x82\xac', encoded_euro)
        self.assertEquals(EURO_SIGN, encoded_euro.decode('utf-8'))

def test_main():
    test_support.run_unittest(UnicodeTestCase)


if __name__ == "__main__":
    test_main()
