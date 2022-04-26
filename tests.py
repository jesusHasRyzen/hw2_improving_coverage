# Jesus Ponce
# April 19
# CS 362_400


# running test to achieve 100% Branch and Condition
# coverage. this means that for each conditional statement,
# you need to have a test case for each combination of
# conditions. Using white box testing techniques

# source code :
# def contrived_func(val):
#     # This function serves no logical purpose
#     # DO NOT try to make sense of it!
#     # Just make sure your tests cover everything requested
#     # val is a numerical value
#     if val < 150 and val > 100:
#         return True
#     elif val * 5 < 361 and val / 2 < 24:
#         if val == 6:
#             return False
#         else:
#             return True
#     elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:
#         return True
#     else:
#         return False
import unittest
from contrived_func import contrived_func


class HomeWork2(unittest.TestCase):

    #     if val < 150 and val > 100:
    #         return True

    # test value 101 which validates as true for condition
    # one and condition two
    def test1(self):
        val = 101
        self.assertTrue(contrived_func(val))
    # test value 99 which is true for first condition one
    # and false for condiiton two

    def test2(self):
        val = 99
        self.assertFalse(contrived_func(val))
    # test value 151 which is false for condition one, no
    # need to test condition two

    def test3(self):
        val = 151
        self.assertFalse(contrived_func(val))

    #     elif val * 5 < 361 and val / 2 < 24:
    #         if val == 6:
    #             return False
    #         else:
    #             return True

    # testing value 35 which is true for condition one
    # and two, then checks if equal to 6 which it is not
    def test4(self):
        val = 35
        self.assertTrue(contrived_func(val))

    # testing value 50 which is true for the first condition
    # and not for the second condition
    def test5(self):
        val = 50
        self.assertFalse(contrived_func(val))

    # testing value 6 which is true for condition one
    # and two, then true for the next if statement val == 6
    def test6(self):
        val = 6
        self.assertFalse(contrived_func(val))

    #     elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:
    #         return True

    # testing value 100 which is true for condition one
    # and two, and also for condition 3
    def test7(self):
        val = 100
        self.assertTrue(contrived_func(val))

    # testing value 76, which is true for condition one,
    #  but fails condition 3, val**val % 5 == 0
    def test8(self):
        val = 76
        self.assertFalse(contrived_func(val))

    # testing value 73 which is false for all if statements,
    # printing the last else statement in the code
    def test9(self):
        val = 73
        self.assertFalse(contrived_func(val))


if __name__ == '__main__':
    unittest.main(verbosity=2)
