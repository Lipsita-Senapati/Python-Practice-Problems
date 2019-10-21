import array
arr  = array.array('i',[1,2,3,4,5])
n = 1

for i in range(len(arr)-1):
    if arr[i] == n:
        arr -= arr[i]
        

for i in range(len(arr)):
    print(arr[i])
