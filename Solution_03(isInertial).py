def isInertial(arr):
    # region Condition (a)
    has_odd = any(x % 2 != 0 for x in arr)
    if not has_odd:
        return 0
    # endregion

    # region Condition (b)
    max_val = max(arr)
    if max_val % 2 != 0:
        return 0
    # endregion

    # region Condition (c)
    odd_values = [x for x in arr if x % 2 != 0]
    even_values = [x for x in arr if x % 2 == 0 and x != max_val]

    if all(odd > even for odd in odd_values for even in even_values):
        return 1
    else:
        return 0
    # endregion

if __name__ == '__main__':
    print(isInertial([12, 11, 4, 9, 2, 3, 10]))