question = """
The General Election is over, and you're in charge of deciding the final budget for the next fiscal year! The only problem is that the list of projects is large, and the relationships between them can be complicated. To solve this, you've decided to implement an algorithm to help you decide.

You're presented with n projects with their respective socioeconomic effects effects. Your analysts have evaluated each project, giving a quantitative value to each, such that the ith project has effect effect[i].

However, one project may conflict with another and affect its actual effect. You're also given a list of edges edges, where each edge (i, j, multiplier) shows how project i will affect project j. More specifically, for an edge (i, j, m) picking i will cause effects[j] *= m prior to the summation.

You can support up to k projects. Implement a function max_effect to determine the maximum total effect you can achieve.

Brute-force solutions should not be accepted
"""

def max_effect(effects: list[int], edges: list[tuple[int, int, int]], k: int) -> int:
    pass


arr = [34, 37, 43, -10, -7]
edges = [(3, 3, 1), (3, 1, 2), (0, 3, -2), (0, 0, 0), (2, 1, 2)]
k = 2
ans = 117
assert max_effect(arr, edges, k) == ans


arr = [15, 3, -2, -1, 10, 41, 6, 41, -5]
edges = [(0, 2, 3), (0, 1, -3), (5, 3, -3), (6, 0, -1), (1, 1, 0), (2, 4, 3), (6, 3, -2), (4, 2, 0), (0, 4, -5)]
k = 3
ans = 97
assert max_effect(arr, edges, k) == ans


arr = [21, 46, -9, -9, 29, 31, 47, 25, 28, 45, 1, 36, 8]
edges = [(0, 3, 5), (9, 10, 4), (11, 4, 6), (4, 4, -3), (4, 4, -8), (4, 3, -10), (7, 5, 5), (0, 1, -5), (9, 3, 0), (5, 0, 1), (2, 4, 2), (0, 3, -2), (10, 0, 7)]
k = 3
ans = 8379
assert max_effect(arr, edges, k) == ans

arr = [25, 20, 49, -7, 8, 36, 25, 10, 7, 40, 17, 4, 31, 48, -9, 26, 0]
edges = [(3, 0, -3), (2, 3, 0), (0, 6, 0), (6, 3, 6), (2, 3, 0), (4, 0, -5), (6, 0, 5), (2, 3, -6), (2, 3, -5), (0, 0, 0), (3, 0, -2), (2, 0, 4), (3, 4, 5), (6, 0, 4), (3, 5, 3), (4, 6, -5), (1, 5, -3)]
k = 5
ans = 245
assert max_effect(arr, edges, k) == ans