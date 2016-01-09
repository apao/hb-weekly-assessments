"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    # @apao's First Try:

    # odd_nums = []

    # for num in number_list:
    #     if num % 2 != 0:
    #         odd_nums.append(num)

    # return odd_nums

    # Then, realized that this code could be simplified and written as a list comprehension.
    # @apao's Second Try:
    return [num for num in number_list if num % 2 != 0]


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    # @apao's First Try:
    # even_nums = []

    # for num in number_list:
    #     if num % 2 == 0:
    #         even_nums.append(num)

    # return even_nums

    # Then, also realized that this code could be simplified and written as a list comprehension.
    # @apao's Second Try:
    return [num for num in number_list if num % 2 == 0]


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    # @apao's First Try, using range to mimic the index of each item:
    # for index in range(len(my_list)):
    #     print index, my_list[index]

    # Then, read up on enumerate(), which was mentioned in lecture, and realized we could unpack each tuple inline:
    for index, item in enumerate(my_list):
        print index, item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    # @apao's First Try:
    return [word for word in word_list if len(word) > 4]


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    # Initialize the smallest_num to be the largest possible comparable number infinity
    smallest_num = float("inf")

    # If the input list is NOT empty, check to see if each item is less than smallest_num.
    # If yes, set smallest_num to that item. 
    # Then check the next item until the end of the list.
    if len(number_list) > 0:
        for num in number_list:
            if num < smallest_num:
                smallest_num = num
    
    # If the input list is empty, return None
    else:
        smallest_num = None

    return smallest_num


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    # Same logic as the smallest_int function, except to initialize largest_num
    # with negative infinity, as we want the function to set largest_num to the
    # first item in the input list initially in the for loop.
    largest_num = -float("inf")

    if len(number_list) > 0:
        for num in number_list:
            if num > largest_num:
                largest_num = num
    else:
        largest_num = None

    return largest_num


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    # To make sure that the result does not round off, made num a float 
    # to guarantee the quotient is a float, not a rounded off integer.
    return [float(num)/2 for num in number_list]


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    # @apao's First Try:
    # return [len(word) for word in word_list]

    # @apao's Second Try - without using len(), loop through each word in the
    # input list, then loop through each character in each word to determine the
    # character count of each word:
    
    lengths_of_words = []

    for word in word_list:
        char_count = 0
        for character in word:
            char_count += 1
        lengths_of_words.append(char_count)

    return lengths_of_words




def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    final_sum = 0

    for num in number_list:
        final_sum += num

    return final_sum



def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """

    final_product = 1

    for num in number_list:
        final_product *= num

    return final_product


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    final_string = ""

    for word in word_list:
        final_string += word

    return final_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    # @apao's First Try - utilizing previously written sum_numbers function above:
    # return float(sum_numbers(number_list)) / float(len(number_list))

    # @apao's Second Try - without using len():
    total_sum = float(sum_numbers(number_list))
    total_count = 0

    for num in number_list:
        total_count += 1

    return total_sum / total_count


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    final_string = ""

    # for each index of the input list, check to see if the item is the last item in the list.
    for idx in range(len(list_of_words)):
        word = list_of_words[idx]

        # if not, add the item to the final string with a comma and space after it
        if idx != len(list_of_words) - 1:
            final_string += word + ', '
        # if yes, add the item to the final string without a comma and space after it
        else:
            final_string += word

    return final_string


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
