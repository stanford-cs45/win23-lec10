from numbers_lib import get_ten

def return10():
    """
    This function should return 10, but instead it returns 0. Fix it!
    """
    return get_ten()


def buildList():
    """
    Improve the style of this function by replacing the while loop
    with a for loop. The header of the loop should look like this:
    for i in range(10)
    """
    the_list = []

    for i in range(10):
        the_list.append(i)

    return the_list


def isPalindrome(name):
    """
    Help decompose palindromeNames! Copy the marked lines into this function
    """
    for i1 in range(len(name) // 2):
        i2 = len(name) - 1 - i1
        if name[i1] != name[i2]:
            return False
    
    return True


def palindromeNames(nameList):
    """
    Filters the passed-in list so it only emits names that are palindromes.
    Help decompose palindromeNames! Copy the marked lines into isPalindrome,
    then make the adjustments listed in the comments.
    """
    outputList = []

    for name in nameList:
        if isPalindrome(name):
            outputList.append(name)

    return outputList
