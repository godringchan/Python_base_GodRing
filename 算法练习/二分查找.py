# tar_list = [1,2,3,4,5]
# low = 0
# high = len(tar_list)-1
# mid = (high - low)//2
# print(mid)


def binary_search(list0, item):
    low = 0
    high = len(list0)-1

    while low <= high:
        mid = (high + low)//2
        # print(mid)

        guess = list0[mid]
        # print(guess)
        # print(guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    list1 = list(range(51))
    # print(list1)
    index = binary_search(list1, 50)
    print(index)

