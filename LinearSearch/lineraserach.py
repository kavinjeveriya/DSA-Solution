# creating data 
data1 = [1,3,5,7,9,2,4,6,8,10,12,14,16,18,20,19,17,15,13,11]

#fucntion defination for linear search
def linear_search(data,num,n):
    for i in range(0,n):
        if data[i] == num:
            return i
    return -1

#function calling 
result = linear_search(data1,11,len(data1))
if result == -1:
    print("Number is not Found in the data...!!!")
else:
    print("Number found at index:",result)