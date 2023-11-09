#r1,c1 = map(int, input().split())
r1,c1 = 3,3
r2,c2 = 3,3
Arr1 = [[1,1,1],[2,2,2]]
Arr2 = [[1,1,1],[2,2,2],[3,3,3]]
result = []
for i in range(r1):
    result1 = []
    for j in range(c2):
        result1.append(0)
    result.append(result1)
print(result)

#for i in range(r1):
 #   Arr1.append(list(map(int, input().split())))

#r2,c2 = map(int, input().split())
#for i in range(r1):
 #   Arr2.append(list(map(int, input().split())))

for i in range(len(Arr1)):
   # iterate through columns of Y
   for j in range(len(Arr2[0])):
       # iterate through rows of Y
       for k in range(len(Arr2)):
           result[i][j] += (Arr1[i][k]) * (Arr2[k][j])
           

for r in result:
   print(' '.join(map(str, r)))

    
      