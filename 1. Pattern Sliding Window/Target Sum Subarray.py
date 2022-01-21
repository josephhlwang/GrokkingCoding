def ans(arr, targ):
    left_index = cur_sum = 0

    for i in range(len(arr)):
        cur_sum += arr[i]

        while cur_sum >= targ:
            if cur_sum == targ:
                return True
            cur_sum -= arr[left_index]
            left_index += 1

    return False


arr = [3, 2, 7]
print(ans(arr, 12))
