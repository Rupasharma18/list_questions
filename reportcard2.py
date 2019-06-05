marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
i = 0
while i < len(marks):
    j = 0
    sum1 = 0
    while j < len(marks):
        sum1 = sum1 + marks[i][j]
        j = j + 1
    store = sum1
    aver = store//j
    print (aver)    
    i = i + 1        
