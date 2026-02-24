## string split and join ##
## Task
## You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
## Function Description
## Complete the split_and_join function in the editor below.
## split_and_join has the following parameters:
## string line: a string of space-separated words ##

## string split and join ##

def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    user_input_string = input()
    result = split_and_join(user_input_string)
    print(result)
