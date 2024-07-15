question = """
Lelouch's group of followers has grown significantly recently, and he's looking to improve the interconnectivity between the members. Luckily, his prior studying in Data Structures and Algorithms helps him perceive this as another abstract problem to solve! He has identified a pattern in which his followers can be represented as numbers, and has devised a way to represent them. This is ordered such that the first appearing members are prioritised in gaining a new connection.

He has prepared an array A of n members, where each member represents a node with a natural number value. There exists a connection between two members if their value is not coprime (i.e. their greatest common divisor is not 1). We can determine the influence array influence (where len(influence) == len(A)) where influence[i] represents the influence of the ith member. We define the "influence" of a member as the sum of its degree, plus the sum of all of its neighbors' degrees.

During the organizational restructuring, he's looking to create k new connections between two members, intending to maximize the lexicographical size of the influence array. Sadly, this is where his skillset ends, he's really struggling to solve this. Thus, Lelouch vi Britannia orders you to implement the function max_influence(arr: list[int], k: int) to find the lexicographically largest influence array possible after adding up to k new connections.

Brute-force/naive solutions should not be accepted.
"""

def max_influence(arr: list[int], k: int) -> list[int]:
    pass


arr = [27, 87, 3, 56, 76]
k = 1
ans = [9, 7, 7, 6, 3]
assert max_influence(arr, k) == ans


arr = [87, 148, 165, 99, 176, 67]
k = 2
ans = [16, 10, 14, 14, 16, 0]
assert max_influence(arr, k) == ans


arr = [163, 101, 197, 166, 133, 115, 157, 13, 100, 137]
k = 2
ans = [7, 0, 0, 7, 0, 4, 0, 0, 8, 0]
assert max_influence(arr, k) == ans

arr = [17, 47, 32, 54, 23, 21, 49, 58, 11, 38, 15, 55, 62, 39, 26]
k = 3
ans = [25, 0, 40, 52, 0, 22, 5, 37, 3, 37, 23, 7, 37, 28, 44]
assert max_influence(arr, k) == ans


arr = [19, 55, 13]
k = 1
ans = [2, 2, 0]
assert max_influence(arr, k) == ans