a = [1, 3, 5, 6]
target = 4
found = False
for i in range(len(a)):
    if a[i] == target:
        print(i)
        found = True
        break
    elif a[i] > target:
        print(i)
        found = True
        break

if not found:
    print(len(a))
