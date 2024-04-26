class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        current=1
        count=1
        for i in range(1,n):
            if((arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i-1]%2==0 and arr[i]%2!=0)):
                count+=1
                current=max(count,current)
            else:
                count=1
        return current
