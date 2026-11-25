numbers=[1,2,3,4,5,6,7,8,9,10]

target=5

low=0
high=len(numbers)-1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index ", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:  
    print(" Element not found")