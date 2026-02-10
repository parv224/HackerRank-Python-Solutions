"""
Problem: Find the Runner-Up Score
Platform: HackerRank
Topic: Lists
Description:
Find the second highest unique score from the list.
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = list(set(arr))   
    unique_scores.sort()

    print(unique_scores[-2])
