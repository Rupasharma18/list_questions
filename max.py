# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
def max_number(number):
    i = 0
    max_num = number[0]
    while i < len(number):
        if number[i] > max_num:
            max_num= number[i]
        i = i +1
    return max_num
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
print (max_number(numbers) )       