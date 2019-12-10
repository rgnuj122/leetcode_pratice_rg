# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(ranks):
    # write your code in Python 3.6
    single=[]
    superior_count=0
    for item in ranks:
        if item not in single:
            single.append(item)
    for item in ranks:
        if (item+1) in single:
            superior_count +=1

    return superior_count
    pass


print("{}".format(solution([3,4,3,0,2,2,3,0,0])))
print("{}".format(solution([4,2,0])))
print("{}".format(solution([4,4,3,3,1,0])))
