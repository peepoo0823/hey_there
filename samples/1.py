Question = """
You are boring now and want to play a game with your friend.

Your friend will give you an array arr and you must count the number of different permutations of this array such that the sum of every two consecutive elements is square.

Write a function num_of_permutations that takes an array arr, and returns the number of different permutations such that the sum of every two consecutive elements is square.

Read the following example for better clarification :-

If arr = [5, 5, 11, 4, 5].
(1) [5, 11, 5, 4, 5] is valid
(2) [5, 4, 5, 11, 5] is valid
So the answer is 2.
"""

def num_od_permutations(arr:list[int]) -> int:
    pass

assert num_of_permutations([5, 5, 11, 4, 5]) == 2
assert num_of_permutations([1, 1, 1, 1, 1]) == 0
assert num_of_permutations([2, 2, 2, 2, 2]) == 1
assert num_of_permutations([1, 2, 3, 4, 5]) == 0
assert num_of_permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
