import day1


class TestDay1:

    def test_part1(self):

        # Given
        filename = 'tests/day1.txt'

        # When
        actual_answer = day1.part1(filename)

        # Then
        expected_number_of_larger_elements = 7

        assert actual_answer == expected_number_of_larger_elements, "Helper text here if you want!?!?!"