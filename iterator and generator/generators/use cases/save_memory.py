import sys

# # without a generator, the complete sequence has to be stored here in a list
# def firstn(n):
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
print(sys.getsizeof(firstn(1000000)), "bytes")
