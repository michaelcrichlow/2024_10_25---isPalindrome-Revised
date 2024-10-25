# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# original code
def isPalindrome(s: str) -> bool:
    # make everything lowercase
    test_string = s.lower()

    # remove characters that aren't valid
    for val in test_string:
        if val not in "abcdefghijklmnopqrstuvwxyx0123456789":
            test_string = test_string.replace(val, "")

    # main logic - parse string
    j = len(test_string) - 1
    for i in range(len(test_string)):
        if j < i:
            break
        if test_string[i] != test_string[j]:
            return False
        j -= 1

    return True


# revised, more efficient code
def isPalindrome_02(s: str) -> bool:
    # set up variables for main loop
    L = 0
    R = len(s) - 1

    # parse string while doing checks for both alphanumeric
    # and lowercase
    while L < R:
        if not s[L].isalnum():
            L += 1
            continue

        if not s[R].isalnum():
            R -= 1
            continue

        if s[L].lower() != s[R].lower():
            return False

        L += 1
        R -= 1

    return True


def main() -> None:
    assert (isPalindrome_02("A man, a plan, a canal: Panama") == True)
    assert (isPalindrome_02("race a car") == False)
    assert (isPalindrome_02("") == True)
    print("All tests passed!")


if __name__ == '__main__':
    main()
