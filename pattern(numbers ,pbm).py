#n = int(input())
n = 5
arr = []
#Added the increasing order of elements in the list
for i in range(1, n+1):
    arr_element = []
    j = 1
    while j <= i:
        arr_element.append(j)
        j += 1
    arr.append(arr_element)
print(arr)
    
#To add decreasing order of elements in the list
ind = 0
for i in range(1, n + 1):
    j = i
    while j > 0:
        if j-1 != 0:
            arr[ind].append(j-1)
        j -= 1
    ind += 1
m = n + n-1
for i in range(n):
    row = ''.join(map(str, arr[i]))
    print(row.center(m, " "))
 
#instead of making a string,how about creating a 2D list in which i can append all the elements in the order \
    # and then join them as astring and print them using for loop
        