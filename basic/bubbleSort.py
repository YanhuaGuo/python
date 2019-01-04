# --* coding: utf-8 *--
'''
env python2.7.1
'''
def bubbleSort(arr):
    length = len(arr)
    if length <= 1:
        return
    
    i = 0
    while(i < length):
        isTrans = False

        j = 0
        while(j < (length - i - 1)):
            
            if(arr[j] > arr[j+1]):
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                isTrans = True
            
            j += 1 # end while 2
        
        i += 1
        if isTrans == False:
            break
        # end while 1
    return #function end


import string as Str

if '__main__' == __name__:
     
    array = [99,54,54,12,9,4,7,1,0]

    bubbleSort(array)

    print array
