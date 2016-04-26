def Powerset(s):
    A=[[]]
    # Reverse through array
    for x in s[::1]:
        print 'x:', x
        # Append self to every element in the current array
        A+=[[x]+y for y in A]
        print 'A:', A
    return A

print Powerset([1, 2, 3])