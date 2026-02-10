"""
Problem: Designer Door Mat
Platform: HackerRank
Topic: Pattern Printing
Description:
Print a door mat pattern using '.|.' symbols with 'WELCOME'
displayed at the center.
"""

if __name__ == '__main__':
    n, m = map(int, input().split())

    # Top half
    for i in range(n // 2):
        print(('.|.' * (2*i + 1)).center(m, '-'))

    # Center
    print('WELCOME'.center(m, '-'))

    # Bottom half
    for i in range(n // 2 - 1, -1, -1):
        print(('.|.' * (2*i + 1)).center(m, '-'))
