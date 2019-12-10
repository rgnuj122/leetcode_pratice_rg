# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    day7count=0
    day7start=0
    moneyspend=0
    for i in range(len(A)):
        a=A[i]
        if day7start == 0:
            day7start=a
            continue
        if a - day7start < 7:
            day7count +=1
        if a - day7start >= 7 or i == len(A)-1:
            if day7count > 3:
                moneyspend+=7
            else:
                moneyspend += (day7count+1)*2
            day7start = a
            day7count=0
    return moneyspend

    pass


print("{}".format(solution([1,2,4,5,7,29,30])))