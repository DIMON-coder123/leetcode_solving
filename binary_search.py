n = [1, 3, 5, 6]
target = 5
left = 0
right = len(n) - 1

while left <= right:
    mid = (left + right) // 2
    if n[mid] == target:
        print(mid)
        break
    elif n[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
print(left)