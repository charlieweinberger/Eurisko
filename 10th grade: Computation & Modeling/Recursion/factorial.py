# main method:
def factorial(n):
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)

# alternate method:
def alt_factorial(n):
    nums = [num for num in range(n)]
    sum = 0
    for num in range(len(nums) - 1):
        sum = nums[num] * nums[num + 1]
    return sum