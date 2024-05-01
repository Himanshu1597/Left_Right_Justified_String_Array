#Code for Left Right Justified String Array

import sys;

"""
    This is the driver function that executes the logic and returns the value
    Parameters:
        paragraph: Actual paragraph given as input
        page_width: Taken as input.
"""
def create_left_and_right_justified_page(paragraph, page_width):

    words = paragraph.split()
    lines = []
    words_in_current_line = []
    current_line_length = 0

    """
         This method adds the justified_line (LEFT and RIGHT) to the lines array.
         Parameter:
            justified_line: Line to be added into the final array
    """

    def add_justified_line_and_reset_the_values(justified_line):
        lines.append(justified_line)
        words_in_current_line.clear()
        return "", 0

    """
        This method fills equal number of gaps between words in a line so as to justify left and right.

        Parameters:
            words_in_current_line: Array that contains individual words to be put in a line
            no_of_gaps: Number that tells the function to place this many spaces/gaps between words in the line.
    """
    def create_justified_line_with_equal_gaps_between_each_word(words_in_current_line, no_of_gaps):
        justified_line = ""

        if (len(words_in_current_line) == 1):
            justified_line += words_in_current_line[0]
        else:
            for i, word in enumerate(words_in_current_line):
                if i == len(words_in_current_line) - 1:
                    justified_line += word
                else:
                    justified_line += word + " " * int(no_of_gaps)
        return add_justified_line_and_reset_the_values(justified_line)

    """
        This method distributes gaps between individual words unequally so as to justify the line left and right.

        Parameters:
            words_in_current_line: Array that contains words to be put in a line
            first_set_of_gaps_to_be_placed: Number of spaces/gaps to be placed between first few words
            number_of_first_set_gaps: Tells the function that first_set_of_gaps_to_be_placed is to be placed between how many words
            second_set_of_gaps_to_be_placed: Tells the function to put this many number of spaces/gaps to be placed between spaces among remaining words in the line
    """
    def create_justified_line_with_two_unequal_sets_of_gaps_between_words(
        words_in_current_line, first_sets_of_gaps_to_be_placed, number_of_first_set_gaps, second_sets_of_gaps_to_be_placed
        ):
        justified_line = ""
        count_of_first_set_of_gaps_placed = 0
        set_first_set_of_gaps = True if number_of_first_set_gaps > 0 else False
        for i, word in enumerate(words_in_current_line):
            if(i == len(words_in_current_line) - 1):
                justified_line += word
            else:
                if set_first_set_of_gaps:
                    justified_line += word + " " * int(first_sets_of_gaps_to_be_placed)
                    count_of_first_set_of_gaps_placed += 1
                    if count_of_first_set_of_gaps_placed == number_of_first_set_gaps:
                        set_first_set_of_gaps = False
                else:
                    justified_line += word + " " * int(second_sets_of_gaps_to_be_placed)

        return add_justified_line_and_reset_the_values(justified_line)

    """
        This method calculates and analyses the distribution of gaps among words in a line.
        Calls function based on whether the words should have equal number of gaps placed between them
        or has to be distributed unequally, respectively, so as to justify the line left and right


        Parameters:
            words_in_current_line: Array of words to be put in a line
            current_line_length: total number of spaces (from page width) taken by the words alone.
            Used to calculate how many remaining spaces/gaps to be put so as to justify the line from left and right.
    """

    def justify_line_left_and_right(words_in_current_line, current_line_length):
        if(len(words_in_current_line) == 1):
            return create_justified_line_with_equal_gaps_between_each_word(words_in_current_line, 0)
        elif(len(words_in_current_line) == 2 and page_width - current_line_length > 0):
            return create_justified_line_with_equal_gaps_between_each_word(words_in_current_line, page_width - current_line_length)

        no_of_words_in_current_line = len(words_in_current_line)
        no_of_gaps_required_between_each_word = page_width - current_line_length

        if no_of_gaps_required_between_each_word == no_of_words_in_current_line - 1:
            return create_justified_line_with_equal_gaps_between_each_word(words_in_current_line, 1)

        elif no_of_gaps_required_between_each_word < no_of_words_in_current_line - 1:
            number_of_first_set_gaps = no_of_gaps_required_between_each_word
            first_set_of_gaps_to_be_placed = 1
            second_set_of_gaps_to_be_placed = 0
            return create_justified_line_with_two_unequal_sets_of_gaps_between_words(
                words_in_current_line, first_set_of_gaps_to_be_placed, number_of_first_set_gaps, second_set_of_gaps_to_be_placed)

        else:
            total_no_of_spaces_between_words = no_of_words_in_current_line -1

            if(no_of_gaps_required_between_each_word % total_no_of_spaces_between_words == 0):
                no_of_gaps_between_each_word = int(no_of_gaps_required_between_each_word / total_no_of_spaces_between_words)
                return create_justified_line_with_equal_gaps_between_each_word(words_in_current_line, no_of_gaps_between_each_word)

            else:
                no_of_first_set_gaps = total_no_of_spaces_between_words - 1
                first_set_of_gaps_to_be_placed = no_of_gaps_required_between_each_word / total_no_of_spaces_between_words
                second_set_of_gaps_to_be_placed = int(first_set_of_gaps_to_be_placed) + (no_of_gaps_required_between_each_word % total_no_of_spaces_between_words)
                return create_justified_line_with_two_unequal_sets_of_gaps_between_words(
                    words_in_current_line, first_set_of_gaps_to_be_placed, no_of_first_set_gaps, second_set_of_gaps_to_be_placed)

    for word in words:

        if len(word) > page_width:
            return True, "Word length is greater than page_width. Erroneous input."

        if current_line_length + (len(word) + 1) <= page_width:

            words_in_current_line.append(word + " ")
            current_line_length += len(word) + 1

        elif current_line_length + len(word) == page_width:

            words_in_current_line.append(word)
            current_line_length += len(word)

        else:
            # Check if the last element of words_in_current_line has a trailing space and adjust that
            if(words_in_current_line[-1].endswith(" ")):
                words_in_current_line[-1] = words_in_current_line[-1].rstrip()
                current_line_length -= 1
            justified_line, current_line_length = justify_line_left_and_right(words_in_current_line, current_line_length)
            if(len(word) < page_width):
                words_in_current_line.append(word + " ")
                current_line_length += len(word) + 1
            else:
                words_in_current_line.append(word)
                current_line_length += len(word)
                justified_line, current_line_length = justify_line_left_and_right(words_in_current_line, current_line_length)

    if len(words_in_current_line) > 0:
        justify_line_left_and_right(words_in_current_line, current_line_length)

    return False , lines

# Paragraph and page_width to be taken as argument in the mentioned order

if(len(sys.argv) < 3):
    print("Arguments Missing: Usage: python <file_name>.py <first_argument_paragraph> <second_argument_page_width>")
    sys.exit(1)

paragraph = sys.argv[1]
page_width = int(sys.argv[2])


is_erroneous, response = create_left_and_right_justified_page(paragraph, page_width)
if is_erroneous:
    print(response)
else:
    for i, line in enumerate(response):
        print("Array[" + str(i + 1) + "] = " + line)
