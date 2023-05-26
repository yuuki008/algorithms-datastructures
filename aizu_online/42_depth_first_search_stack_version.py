n = 6
G = [
[1, 2, 2, 3],
[2, 2, 3, 4],
[3, 1, 5],
[4, 1, 6],
[5, 1, 6],
[6, 0],
]
M = [[False for _ in range(n+1)] for _ in range(n+1)]
D = [[] for _ in range(n+1)]
color = ['WHITE' for _ in range(n+1)]
stack = []

# わからんまた再挑戦する