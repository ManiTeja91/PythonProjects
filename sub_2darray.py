N,M = map(int, input().split())
Arr1 = []
Arr2 = []
for i in range(N):
    Arr1.append(list(map(int, input().split())))

for i in range(N):
    Arr2.append(list(map(int, input().split())))
for i in range(N):
    ele = []
    for j in range(M):
        ele.append(Arr2[i][j] - Arr1[i][j])
    print(' '.join(map(str, ele)))