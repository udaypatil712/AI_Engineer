arr = [1,2,3,4]
ans = []
print(arr)

for ind , val in enumerate(arr):
    print(ind , val)
    ans.append(ind)  #its adds put the value that particular list


# ans.insert(1 , 22)  its puts the value of that particular index that you gave 
# print(ans)


for i in range(len(arr) - 1):
    print(i+1)

arr.sort()
print(arr)


print(arr[1:3])  #slicing starting index to end - 1

