# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    str=''
    while A+B >0:
        if str.endswith('aa'):
            str += 'b'
            B-=1
        elif str.endswith('bb'):
            str += 'a'
            A -= 1
        elif A >= B:
            str += 'a'
            A-=1
        elif A < B:
            str += 'b'
            B-=1
    return str


    pass

print("{}".format(solution(5,3)))
print("{}".format(solution(3,3)))
print("{}".format(solution(1,4)))
