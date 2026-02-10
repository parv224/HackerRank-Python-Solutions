"""
Problem: Exceptions
Platform: HackerRank
Topic: Exception Handling
Description:
Handle division and input errors using try-except blocks.
"""

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        try:
            a, b = input().split()
            print(int(a) // int(b))
        except Exception as e:
            print("Error Code:", e)
