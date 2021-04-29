N , X = map(int,input().split())

MarksSheet = []
for i in range (X):
    MarksSheet.append(map(float,input().split()))
    
for i in  (zip(*MarksSheet)):
    sum_of_no = sum(i)
    total_no_of_subject = len(i)
    average = sum_of_no / total_no_of_subject
    print(average)
