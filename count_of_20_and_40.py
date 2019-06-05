numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index = 0
count_20 = 0
count_40 = 0
while index < len(numbers):
    if 20 <= numbers[index]:
        count_20 = count_20 + 1
    if 40 >= numbers[index]:
        count_40 = count_40 + 1
    index = index+1
print ("count_20:-"+str(count_20),"count_40:-"+ str(count_40))        