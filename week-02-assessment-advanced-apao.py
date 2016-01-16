"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""

# @apao start time = 9:07am on Saturday, January 16, 2016
# @apao end time = 9:49am on Saturday, January 16, 2016

# @apao additional 35mins to code Version 2 and 3 of top_characters function


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # VERSION 1 - THE BRUTE FORCE WAY

    # char_counts = set()
    # string_without_whitespace = input_string.replace(" ", "")

    # # Create a set of unique set of tuples a la (char, count of that char) such as ex: ('f', 10)
    # for current_char in string_without_whitespace:
    #     count_of_char = 0
    #     for char_again in string_without_whitespace:
    #         if char_again == current_char:
    #             count_of_char += 1
    #     char_counts.add((current_char, count_of_char))

    # greatest_count = -float("inf")
    # greatest_char = []

    # # See which character count number is the greatest amongst the full set.
    # for char_and_count in char_counts:
    #     char = char_and_count[0]
    #     count = char_and_count[1]
    #     if count >= greatest_count:
    #         greatest_count = count

    # # Because there may be ties, append the char of any tuple where the char count is equal to the greatest count
    # for char_and_count in char_counts:
    #     char = char_and_count[0]
    #     count = char_and_count[1]
    #     if count == greatest_count:
    #         greatest_char.append(char)

    # return sorted(greatest_char)

    # VERSION 2 - USING DICTIONARIES, beginner way

    # char_counts = {}
    # string_without_whitespace = input_string.replace(" ", "")

    # # Create dictionary of every character in string and its respective count in the string, including duplicates
    # # Keys are the character counts and the values are the characters that have that count
    # for current_char in string_without_whitespace:
    #     count_of_char = 0
    #     for char_again in string_without_whitespace:
    #         if char_again == current_char:
    #             count_of_char += 1
    #     # with the character count as dictionary key, set value to list of characters with that count
    #     if char_counts.get(count_of_char):
    #         char_counts[count_of_char].append(current_char)
    #     else:
    #         char_counts[count_of_char] = [current_char]

    # # Remove the duplicates by assigning the values to a set
    # for current_count in char_counts.keys():
    #     char_counts[current_count] = sorted(set(char_counts.get(current_count)))

    # # Find and set the greatest count to the maximum value of dictionary keys
    # greatest_count = max(char_counts.keys())

    # # Return the list version of the values corresponding to the key of greatest count
    # return list(char_counts.get(greatest_count))


    # VERSION 3 - USING DICTIONARIES, slightly more advanced
    char_counts = {}
    inverted_char_counts = {}
    string_without_whitespace = input_string.replace(" ", "")

    # Create dictionary of every character in string and its respective count in the string
    # Keys are the characters and the values are the respective counts
    for current_char in string_without_whitespace:
        current_count = char_counts.get(current_char, 0)
        char_counts[current_char] = current_count + 1

    # Invert the dictionary so that the keys are counts and values are the characters
    for char, count in char_counts.items():
        if inverted_char_counts.get(count):
            inverted_char_counts[count].append(char)
        else:
            inverted_char_counts[count] = [char]

    # Find and set the greatest count to the maximum value of dictionary keys
    greatest_count = max(inverted_char_counts.keys())

    # Return the list version of the values corresponding to the key of greatest count
    return sorted(list(inverted_char_counts.get(greatest_count)))


# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    # Same code from initial skills assessment:
    dict_of_word_lengths = {}

    for current_word in words:
        current_word_length = len(current_word)
        if dict_of_word_lengths.get(current_word_length):
            dict_of_word_lengths[current_word_length].append(current_word)
        else:
            dict_of_word_lengths[current_word_length] = [current_word]

    # Use sorted only once to sort the values list for each key.
    for key in dict_of_word_lengths.keys():
        dict_of_word_lengths[key] = sorted(dict_of_word_lengths.get(key))

    return dict_of_word_lengths.items()


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
