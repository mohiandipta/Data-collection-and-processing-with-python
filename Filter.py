def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 5, 6, 7, 0]))


#####---------using filter function------#####
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 ==0 , nums)
    return list(new_seq)

print(keep_evens([2, 3, 5, 6, 7, 0]))