"""
A photography set consists of NN cells in a row, numbered from 11 to NN in
order, and can be represented by a string CC of length NN. Each cell ii is one
of the following types (indicated by CiCi​, the iith character of CC):

    If CiCi​ = “P”, it is allowed to contain a photographer If CiCi​ = “A”, it is
    allowed to contain an actor If CiCi​ = “B”, it is allowed to contain a
    backdrop If CiCi​ = “.”, it must be left empty

A photograph consists of a photographer, an actor, and a backdrop, such that
each of them is placed in a valid cell, and such that the actor is between the
photographer and the backdrop. Such a photograph is considered artistic if the
distance between the photographer and the actor is between XX and YY cells
(inclusive), and the distance between the actor and the backdrop is also
between XX and YY cells (inclusive). The distance between cells ii and jj is
∣i−j∣∣i−j∣ (the absolute value of the difference between their indices).

Determine the number of different artistic photographs which could potentially
be taken at the set. Two photographs are considered different if they involve a
different photographer cell, actor cell, and/or backdrop cell.

>>> getArtisticPhotographCount(5, 'APABA', 1, 2)
1
>>> getArtisticPhotographCount(5, 'APABA', 2, 3)
0
>>> getArtisticPhotographCount(8, '.PBAAP.B', 1, 3)
3
"""
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    return getArtisticPhotographCount1(N, C, X, Y)

PHOTOGRAPHER = 'P'
ACTOR = 'A'
BACKDROP = 'B'
FORWARDS = True
BACKWARDS = False

"""
Attempt to define a set of nested methods that does something like:
- Find photographers
- From photographer position, find valid actors
- From actor position, find valid backdrops

Time:
- O(n) to look for photographers
- O(n*2(Y-X)) to look for actors for each photographer
- O(n*2(Y-X)*2(Y-X)) to look for backdrops for each actor
- => O(n*y^2) ?

Space:
- O(1) at most 3 levels of stack need to maintain
"""
def getArtisticPhotographCount1(N: int, C: str, X: int, Y: int) -> int:
    # find photographer
    totalArtisticPhotoCount = 0
    for i in range(N):
        if C[i] == PHOTOGRAPHER:
            localArtisticPhotoCount = 0
            # TODO look forwards and backwards
            localArtisticPhotoCount += \
                getValidActorAndBackdrop(N, C, X, Y, i, FORWARDS)
            localArtisticPhotoCount += \
                getValidActorAndBackdrop(N, C, X, Y, i, BACKWARDS)
            totalArtisticPhotoCount += localArtisticPhotoCount
    return totalArtisticPhotoCount

def getValidActorAndBackdrop(N: int, C: int, X: int, Y: int, pIdx: int, direction: bool) -> int:
    count = 0
    # first find valid actor, then find valid backdrop
    # range where valid actors should be is
    #
    #     forwards:  pIdx (photographer index) + X <= aIdx <= pIdx + Y (inclusive)
    #     backwards: pIdx - Y <= aIdx <= pIdx - X

    if direction == FORWARDS:
        for i in range(pIdx + X, pIdx + Y + 1):
            if i < N and C[i] == ACTOR:
                localCount = 0
                localCount += getValidBackdropCount(N, C, X, Y, i, direction)
                count += localCount
    else:
        for i in range(pIdx - X, pIdx - Y - 1, -1):
            if i >= 0 and C[i] == ACTOR:
                localCount = 0
                localCount += getValidBackdropCount(N, C, X, Y, i, direction)
                count += localCount
                # print(f"Contribution from backwards backdrop count: {localCount} i={i}")
    return count

def getValidBackdropCount(N: int, C: int, X: int, Y: int, aIdx: int, direction: bool) -> int:
    count = 0
    if direction == FORWARDS:
        for i in range(aIdx + X, aIdx + Y + 1):
            if i < N and C[i] == BACKDROP:
                count += 1
    else:
        for i in range(aIdx - X, aIdx - Y - 1, -1):
            if i >= 0 and C[i] == BACKDROP:
                count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
