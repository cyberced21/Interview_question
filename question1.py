def coordOverlap(x1,x2):
    if isinstance(x1,tuple) and isinstance(x2,tuple):
        if ((x1[0] >= x2[0] and x1[0] <= x2[1]) or (x1[1] >= x2[0] and x1[1] <= x2[1])) and ((x2[0] >= x1[0] and x2[0] <= x2[1]) or (x2[1] >= x1[0] and x2[1] <= x1[1])):
            return True
    return False

# (1,2) (2,3) True one of the
# (5,6) (7,9) False
# (1,5) (6,2) True
print(coordOverlap((1,2),(2,3))) #true
print(coordOverlap((5,6),(7,9))) #False
print(coordOverlap((1,5),(6,2))) #true they overlap
print(coordOverlap((1,5),(6,12))) #false
print(coordOverlap(123,123))#false
print(coordOverlap("213","123"))#false


# everything is linked with the second pair of coordinate,
# if any of the 2 x coordinate of the seconde pair is equal to or beetween the first pair they overlap
# they also overlap if one of the number is before or after while the other is the oposite (x2[1] is before and the other is after, and vice versa)
