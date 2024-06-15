def maximumElement(arr):
    Max = float('-inf')  
    for i in arr:
        if i > Max:
            Max = i
    return Max

def minimumElement(arr):
    MIN = float('inf')  
    for i in arr:
        if i < MIN:
            MIN = i
    return MIN
arr = [1, 3, 5, 2, 7, 4, 8]
max_value = maximumElement(arr)
min_value = minimumElement(arr)

print("Maximum element:", max_value)
print("Minimum element:", min_value)