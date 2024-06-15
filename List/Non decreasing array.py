from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    # Write your code here.
    count=0
    n=len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            count+=1
            if count>1:
                return False
            
            if i>1 and arr[i-2] >arr[i]:
                arr[i]=arr[i-1]
            else:
                arr[i-1]=arr[i]
    return True

    pass
