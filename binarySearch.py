pos = 1
def search(list1,num):
    first_index = 0
    last_index = len(list1)-1
    while first_index <= last_index:
        mid = (first_index+last_index)//2
        if list1[mid] == num:
            print (list1[mid])
            globals()['pos'] = mid
            return True
        else:    
            if list1[mid] < num:
                print (list1[mid])
                first_index = mid+1
            else:
                last_index = mid+1
    return False            
list1 = [21,3,4,5,6,7,8,4,33,24]
num = 33
if search(list1, num):
    print ("found it:-", pos+1)
else:
    print ('not found')    