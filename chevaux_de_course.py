import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input())
P = []
for i in range(N):
    P.append(int(input()))
    
P.sort()
best_diff = -1
for i in range(N - 1):
    diff = P[i + 1] - P[i]
    if diff < best_diff or best_diff == -1:
        best_diff = diff
print(best_diff)
