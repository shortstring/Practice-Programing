# using a binary search
def firstBadVersion(n):
    mid = n//n
    my_return = mid

    print(n)
    for i in range(mid):
        if isBadVersion(mid) == True:
            my_return = True


def isBadVersion(arg):
    return True
