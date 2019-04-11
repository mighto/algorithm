'''
快速排序
'''


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 基准值
        pivot = arr[0]

        # 小于基准的部分
        less = [i for i in arr[1:] if i <= pivot]
        # 大于基准的部分
        greater = [i for i in arr[1:] if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    mylist = [5, 1, 7, 3, 10, 8, 4, 2, 6, 9]
    print(quicksort(mylist))
