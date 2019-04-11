'''
二分查找
'''


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    if item < 0:
        return None
    while low <= high:
        # 地板除，获取商的整数部分
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 3, 5, 6, 7, 9, 10, 13]
    print(binary_search(my_list, 5))
