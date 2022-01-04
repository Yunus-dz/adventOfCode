from math_utils import adder


class TestMathUtils:

    def test_adder(self):

        # Given - I read in some data / oro I set some inputs
        number1 = 5
        number2 = 7

        # When - I run my function
        actual_answer = adder(number1, number2)

        # Then - I expect this outcome
        expected_answer = 12

        assert actual_answer == expected_answer, "Should add numbers in the expected way"

    def test_other(self):
        # TODO - if I wanted to add another test
        assert True