"""You are given a non-empty set s and a number of commands.
Each command performs one of the following operations:
pop() → Removes an arbitrary element from the set.
remove(x) → Removes element x from the set. Raises error if not present.
discard(x) → Removes element x if present. Does nothing if not present.
After executing all commands, print the sum of elements remaining in the set."""


n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))
