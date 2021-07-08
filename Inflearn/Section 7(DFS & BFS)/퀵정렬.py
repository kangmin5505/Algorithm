def Qsort(left, right):
    if left < right:
        pos = left
        pivot = arr[right]
        for i in range(left, right):
            if arr[i] <= pivot:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        arr[pos], arr[right] = arr[right], arr[pos]
        Qsort(left, pos-1)
        Qsort(pos+1, right)

if __name__=="__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print(f"Before sort : {arr}")
    Qsort(0,len(arr)-1)
    print(f"After sort : {arr}")

