def fibonacci_pattern(n):
    t = [0, 1]
    for i in range(2,n):
        t.append((t[i-1])+(t[i-2]))
    for i in range(len(t)):
        s = ' '
        for j in range(i+1):
            s = s + " " + str(t[j])
        print(s)           
        
        
if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    fibonacci_pattern(n)