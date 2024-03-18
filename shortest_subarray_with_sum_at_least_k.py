import collections

""" for only positive values """

def shortest_subarray_with_sum_at_least_k(arr, k):
    n = len(arr)
    left = 0
    min_length = float('inf')
    sum_so_far = 0

    for right in range(n):
        print("right: ",right)
        sum_so_far += arr[right]
        while sum_so_far >= k:
            min_length = min(min_length, right - left + 1)
            sum_so_far -= arr[left]
            left += 1
            print("left: ",left)
    return min_length if min_length != float('inf') else -1


# print(shortest_subarray_with_sum_at_least_k([2,-1,2],3))

""" for handling negative values """

def shortest_subarray_with_sum_at_least_k(nums, k):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    left = right = 0
    res = float("inf")
    deq = collections.deque()
    
    for i, p in enumerate(prefix):
        while deq and prefix[deq[-1]] > p:
            deq.pop()
        while deq and p - prefix[deq[0]] >= k:
            res = min(res, i - deq.popleft())
        deq.append(i)
    return res if res != float("inf") else -1

print(shortest_subarray_with_sum_at_least_k([2,-1,2],3))