 ## List comprehensions ##
## Input Format
## Four integers i,j,k  and n, each on a separate line.
## Constraints
## Print the list in lexicographic increasing order.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [
        [i, j, k]
        for i in range (x + 1)
        for j in range (y + 1)
        for k in range (z + 1)
        if i + j + k != n        
        ]
        
    print(coordinates)
