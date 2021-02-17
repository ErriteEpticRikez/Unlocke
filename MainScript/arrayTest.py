from errite.arraytools.parameterMaker import makeParameterArray
# unit test case
import unittest


class TestStringMethods(unittest.TestCase):
    # test function to test the array param creation process
    def test_array(self):
        # This is an example of a command, while Unlocke would never do this. Its to test out parsing arguments.
        test_command = "rsync -avzh root@fakehost:/home/server/unlocke /new_bin"
        test_array = makeParameterArray(test_command)
        # error message in case if test case got failed
        message = "Expected array value was not found"
        # assertEqual() to check equality of first & second value
        self.assertEqual(test_array[0], "rsync", message)
        self.assertEqual(test_array[1], " -avzh", message)
        self.assertEqual(test_array[2], " root@fakehost:/home/server/unlocke", message)
        self.assertEqual(test_array[3], " /new_bin", message)


if __name__ == '__main__':
    unittest.main()
