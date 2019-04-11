'''
选择排序
'''


# 获取数组中的最小值
def findSmallest(arr):
    # 存储最小的值
    smallest = arr[0]
    # 存储最小元素的索引
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        # 找到数组中最小的元素，并加入新数组中
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == "__main__":
    mylist = [1, 5, 7, 3, 9, 6, 2, 10]
    print(selectionSort(mylist))
