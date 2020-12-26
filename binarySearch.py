def binarySearch(arr,targ):
    #Initlizing the pointers
    firstPointer=0
    lastPointer=len(arr)
    while(firstPointer<=lastPointer):
        #dividing at midpoint
        midPointer=(firstPointer+lastPointer)//2
        if arr[midPointer]==targ:
            #if value at midpoint equals target variable
            return midPointer
        elif arr[midPointer]>targ:
            #if value at midpoint greater than target variable
            lastPointer=midPointer-1
        elif arr[midPointer]<targ:
            #if value at midpoint less than target variable
            firstPointer=midPointer+1

print(binarySearch([1,2,3,4,5,6],5))