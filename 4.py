a = input().split()
for i in range(len(a)):
    if (int(a[i]) > 0  and  int(a[i-1]) > 0) or int(a[i]) < 0  and  int(a[i-1]) < 0:
            print(a[i], a[i-1])