""" tuples using hash """

n = int(input())
numbers_str = input()
numbers = tuple(map(int, numbers_str.replace(',', ' ').split()))
print(abs(hash(numbers)))
