def checkIfPalindrome(inputString, printResult=0):
    """
    Func checks if the inputString is a palidrome.
    Length of inputString must be longer than 1.

    :param inputString:
    :param printResult: 0 -> without print(), 1 -> including print()
    :return: True if palindrome
    """
    if printResult == 0 or printResult == 1:
        if len(inputString) <= 1:
            if printResult == 1: print("NOT PALINDROME.")
            return False
        else:
            reversedInputString = inputString[::-1]
            if inputString == reversedInputString:
                if printResult == 1: print("THIS IS PALINDROME.")
                return True
            else:
                if printResult == 1: print("NOT PALINDROME")
                return False
    else:
        print("WRONG printResult=? argument")

checkIfPalindrome("aaa", printResult=1)


