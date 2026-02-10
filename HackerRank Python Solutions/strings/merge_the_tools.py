"""
Problem: Merge the Tools
Platform: HackerRank
Topic: Strings
Description:
Split the string into equal parts of length k and remove duplicate
characters from each part while maintaining order.
"""

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        result = ""

        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)


if __name__ == '__main__':
    string = input().strip()
    k = int(input())
    merge_the_tools(string, k)
