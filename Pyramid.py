""" Pyramid Generator

This module prints a right aligned pyramid of hashes to a specified height.
"""


def is_int(value):
    """
    Checks if a given value is an integer or not

    :param value: The value to check
    :return: returns True if value is an int, False otherwise
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

def check_height(height):
    """
    Validates the height of the pyramid requested by the user.
    Performs bounds checking between 1 & 23

    :param height: The height value provided by the user
    :returns: the height value as an integer or -1
    """
    if is_int(height) and int(height) > 0 and int(height) <= 23:
        return int(height)
    else:
        return -1

def build_line(line, height):
    """
    Constructs the specified line for a pyramid of the given height

    :param line: the specific line to generate
    :param height: the overall height of the pyramid
    :return: returns a string constructed of a number of spaces and hash symbols
    """
    hash_count = 2 + (line - 1)
    spaces = height - hash_count + 1
    output = "".ljust(spaces) + "".rjust(hash_count, "#")
    return output

def main():
    """
    Requests input from user until valid input is given.
    With valid input, prints pyramid of given size to console.
    """
    valid_input = False

    while valid_input is False:
        print "Enter the height of the pyramid: "
        in_height = raw_input()
        height = check_height(in_height)
        if height > -1:
            valid_input = True
    print height

    for line in xrange(1, height+1):
        print build_line(line, height)

if __name__ == "__main__":
    main()
