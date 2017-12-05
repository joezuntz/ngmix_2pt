"""
Example unit tests for ngmix_2pt package
"""
import unittest
import desc.ngmix_2pt

class ngmix_2ptTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'

    def tearDown(self):
        pass

    def test_run(self):
        foo = desc.ngmix_2pt.ngmix_2pt(self.message)
        self.assertEquals(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, desc.ngmix_2pt.ngmix_2pt)
        foo = desc.ngmix_2pt.ngmix_2pt(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
