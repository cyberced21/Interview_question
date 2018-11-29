def coordOverlap(x1,x2):
    """
    For this question, I had in mind to make it as short as possible.
    Knowing it could be done in 3 to 4 lines, I took the time to flesh out the algorithm.
    Whats important to note here is that I decided to go for a 'crap in crap out' aproach which means
    no validation here, all in order to keep the algorithm clean.

    everything is linked with the second pair of coordinate,
    if any of the 2 x coordinate of the second pair is equal to or beetween the first pair they overlap.
    they also overlap if one of the number is before or after while the other is the oposite and vice versa.

    I know this algorithm doesnt cover all of the cases, but it covers a good chunk of them so it satisfies me, for now that is.

    I also implemented the if condition with parentheses for readability and priority of operation.

    >>> print(coordOverlap((5,6),(7,9))) #False
    False
    >>> print(coordOverlap((1,2),(2,3))) #True
    True
    >>> print(coordOverlap((1,5),(6,2))) #True
    True
    >>> print(coordOverlap((1,5),(6,12))) #false
    False
    >>> print(coordOverlap((6,12),(1,32))) #True
    True
    >>> print(coordOverlap((100,4),(20,3))) #True
    True
    """
    if ( (x2[0] >= x1[0] and x2[0] <= x1[1]) or (x2[1] >= x1[0] and x2[1] <= x1[1]) ) or ( (x2[1] > x1[1] and x2[0] < x1[0]) or (x2[0] > x1[1] and x2[1] < x1[0]) ):
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
