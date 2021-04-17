No_of_element_set_A = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for i in range(N):
    operation_name, No_of_element_set_A = input().split()
    s2 = set(map(int, input().split()))
    if(operation_name == "intersection_update"):
        s1.intersection_update(s2)
    elif(operation_name == "update"):
        s1.update(s2)
    elif(operation_name == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(operation_name == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))