from typing import List
# Write any import statements here
  
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  """
  Discussion:
  
  Possible number of seats N is prohibitively large, we can't just allocate an array of N elements to mark occupied/mandatory reserved seats.
  
  Number of already-seated diners M is reasonably sized, but we need an effective way to traverse the list of diners to find the gaps.
  => Sort list of diners M
  
  Need a way of calculating optimal number of seats given [start, end] seat positions, inclusive, and spacing K between diners.
  
  Time:
  - O(M*lg(M)) sort
  - O(M) to iterate through the M diners and calculate max diners between each pair
  - => O(M*lg(M)) for sufficiently large M
  
  Space:
  - => O(1) to keep track of diners

  >>> getMaxAdditionalDinersCount(10, 1, 2, [2, 6])
  3
  >>> getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14])
  1
  """
  S.sort()

  dinerCount = 0
  
  # calculate from 1 ... S[0] - (K+1)
  dinerCount += numOptimalDiners(1, S[0] - (K + 1), K)
  # print(f"{dinerCount}")
  # calculate from S[N] + (K+1) ... N
  dinerCount += numOptimalDiners(S[-1] + (K + 1), N, K)
  # print(f"{dinerCount}")

  # for each pair of diners i, j in S, where i and j are consecutive and i >= 1 and j <= N,
  #   calculate the next available seat from S[i] and the earliest available seat from S[j] using K
  #   determine optimal diners in that space
  i = 0
  j = 1
  while j < M:
    startSeat = S[i] + (K + 1)
    endSeat = S[j] - (K + 1)
    dinerCount += numOptimalDiners(startSeat, endSeat, K)
    # print(f"{dinerCount}")
    i += 1
    j += 1
  return dinerCount

  
"""
Calculates the number of diners that can optimally fit between [start, end] inclusive of both, with K seats between them.

numOptimalDiners(0, 5, 1) = 5 ([0, 2, 4] or [1, 3, 5])
numOptimalDiners(0, 1, 1) = 0
numOptimalDiners(5, 9, 2) = 2 ([5, 8] or [6, 9])

numOptimalDiners(start, end, space) = (end - start) // (space + 1) + 1
"""
def numOptimalDiners(start: int, end: int, K: int) -> int:
  # print(f"start={start}, end={end}")
  if (end - start) < 0:
    return 0
  return (end - start) // (K + 1) + 1

if __name__ == '__main__':
  import doctest
  doctest.testmod()
