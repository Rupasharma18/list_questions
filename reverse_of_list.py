def reverse(number):
    length = len(number)-1
    i = 0
    empty_list = []
    while length >= 0:
        empty_list.append(number[length])
        length= length-1
    return empty_list
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
print (reverse(places))