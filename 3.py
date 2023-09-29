a = input().split()
for i in range(len(a)):
    if int(a[i]) > int(a[i-1]):
            print(a[i])