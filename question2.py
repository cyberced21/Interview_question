def versionCompare(vers1,vers2):
    """
    Like pretty much every function that I write, the doctest had to be writen first.

    My challenge personal challenge was to make the code as clean as possible.

    Here I decided to implement character catching because the question mentionned :
    "Please provide all test cases you could think of."
    I also implemented doctests for ease of developpment during my code writing session.


    >>> print(versionCompare("1.2","1.2"))
    1.2 is equal to 1.2
    >>> print(versionCompare("1.2","1.2.1"))
    1.2 is lesser than 1.2.1
    >>> print(versionCompare("1.2.2","1.2.1"))
    1.2.2 is greater than 1.2.1
    >>> print(versionCompare("1","2"))
    1 is lesser than 2
    >>> print(versionCompare("A","A"))
    Error, not a standard version string.
    >>> print(versionCompare("1.2.2.1.2.3.4.5.5","1.2.1"))
    1.2.2.1.2.3.4.5.5 is greater than 1.2.1
    >>> print(versionCompare("1.2.0.0.0.0.0.0.1","1.2.0.0.0.0.0.0.2"))
    1.2.0.0.0.0.0.0.1 is lesser than 1.2.0.0.0.0.0.0.2
    >>> print(versionCompare("1.2.0.0.0.0.0.0.1","1.2.0.0.0.0.0.0.1"))
    1.2.0.0.0.0.0.0.1 is equal to 1.2.0.0.0.0.0.0.1

    """

    # we get "arrays" of the numbers
    vers1_lst=vers1.split('.')
    vers2_lst=vers2.split('.')

    # if any of the character in the in the array is no numeric we return an error
    for chr in vers1_lst:
        if not chr.isnumeric():
            return "Error, not a standard version string."

    for chr in vers2_lst:
        if not chr.isnumeric():
            return "Error, not a standard version string."


    # if the 2 strings are equal the version numbers are the same
    if vers1 == vers2:
        return vers1 + " is equal to " + vers2

    # if the version numbers are unequal than we fill them with zeros
    if len(vers1_lst) < len(vers2_lst):
        while(not len(vers1_lst)==len(vers2_lst)):
            vers1_lst.append("0")
    elif len(vers1_lst) > len(vers2_lst):
        while(not len(vers2_lst)==len(vers1_lst)):
            vers2_lst.append("0")

    # loops over the size of the strings since they are equal now
    for i in range(len(vers1_lst)):
        # for each iteration, if the numbers are equals we do nothing
        # otherwise the version numbers is greater or lesser than its opposite
        if vers1_lst[i] == vers2_lst[i]:
            continue
        if vers1_lst[i] < vers2_lst[i]:
            return vers1+" is lesser than "+vers2
        if vers1_lst[i] > vers2_lst[i]:
            return vers1+" is greater than "+vers2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
