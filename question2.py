def versionCompare(vers1,vers2):
    """
    Like pretty much every function that I write, the doctest had to be writen first.

    the challenge here is the number of possible combinations,
    because I have up to 3 possible level of versions and that gives me alot of possibilities to  consider.

    My challenge personal challenge was to make the code as clean as possible.

    Here I decided to implement exceptions because the question mentionned :
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
    """



    vers1_lst=vers1.split('.')
    vers2_lst=vers2.split('.')

    for chr in vers1_lst:
        if not chr.isnumeric():
            return "Error, not a standard version string."

    for chr in vers2_lst:
        if not chr.isnumeric():
            return "Error, not a standard version string."


    if vers1 == vers2:
        return vers1 + " is equal to " + vers2

    if len(vers1_lst) == 1  and len(vers2_lst) == 1 and vers1_lst[0] == vers2_lst[0] and vers1_lst[1] == vers2_lst[1]:
        return vers1 + " is equal to " + vers2

    if vers1_lst[0] < vers2_lst[0]:
        return vers1+" is lesser than "+ vers2




if __name__ == "__main__":
    import doctest
    doctest.testmod()
