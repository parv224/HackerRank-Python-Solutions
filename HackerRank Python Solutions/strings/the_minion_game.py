"""
Problem: The Minion Game
Platform: HackerRank
Topic: Strings
Description:
Two players (Kevin and Stuart) create substrings from a given string.
Kevin scores for substrings starting with vowels.
Stuart scores for substrings starting with consonants.
The player with the higher score wins.
"""

def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    # Count substrings starting from each position
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    # Determine the winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input().strip()
    minion_game(s)
