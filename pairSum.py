def has_pair_with_sum(arr,target):
    seen=set()
    for num in arr:
        complement=target-num
        if complement in seen:
            return True
        seen.add(num)
    return False
arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target sum: "))

if has_pair_with_sum(arr, target):
    print("Pair with given sum exists!")
else:
    print("No pair with given sum found.")