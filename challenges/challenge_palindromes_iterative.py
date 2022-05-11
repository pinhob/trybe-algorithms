def is_palindrome_iterative(word):
    if word == '':
        return False

    for index, letter in enumerate(word):
        if letter != word[-1 - index]:
            return False

    return True
