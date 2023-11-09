#N, M = map(int, input().split())
N, M = 3, 4
Arr = [[1, 7, 5, 4], [8, 6, 3, 4], [2, 9, 4, 3]]
#for i in range(N):
 #   Arr.append(list(map(int, input().split())))
    
print(Arr)
if N == M: 
    for i in range(N):
        string1 = ""
        for j in range(M):
            string1 = string1 + str(Arr[j][i]) + " "
        print(string1)


#no. of rows more than columns
elif N >= M:
    for i in range(M): #giving column numbers to i(we will go to column one by one)
        String = ""
        for j in range(N): #giving row number to j (we will take all row elements in a single column)
            String = String + str(Arr[j][i]) + " "
        print(String)
        

elif N <= M:
    for i in range(M): #giving column numbers to i(we will go to column one by one)
        String = ""
        for j in range(N): #giving row number to j (we will take all row elements in a single column)
            String = String + str(Arr[j][i]) + " "
        print(String)