def Dsort(left, right):
    if left < right:
        mid = (left + right) // 2
        Dsort(left, mid)
        Dsort(mid+1, right)
        p1 = left
        p2 = mid+1
        temp = []
        while p1 <= mid and p2 <= right:
            if arr[p1] <= arr[p2]:
                temp.append(arr[p1])
                p1+=1
            else:
                temp.append(arr[p2])
                p2+=1
        if p1 <= mid:
            temp = temp + arr[p1:mid+1]
        else:
            temp = temp + arr[p2:right+1]
        for i in range(len(temp)):
            arr[left+i] = temp[i]

if __name__=="__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print(f"Before sort : {arr}")
    Dsort(0,len(arr)-1)
    print(f"After sort : {arr}")

