class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest = i 
        left = 2 * largest + 1
        right = 2 * largest + 2
        
        if (left < n and arr[left] > arr[largest]):
            largest = left
        if (right < n and arr[right] > arr[largest]):
            largest = right
            
        if(largest != i):
            arr[largest],arr[i] = arr[i],arr[largest]
            self.heapify(arr,n,largest)
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
      
       i = (n//2)-1
       while i >= 0:
           self.heapify(arr,n,i)
           i -= 1

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)