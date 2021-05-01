d = int(input())

set_1 = set(map(int,input().split()))
b = int(input())
set_2 = set(map(int,input().split()))
c = len(set_1.symmetric_difference(set_2))
print(c)
