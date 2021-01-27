nums = [4, 1, 6, 3, 3, 2, 7, 8]
n = 1
while n < len(nums):
    for i in range(len(nums) - n):
        if nums[i] > nums[i + 1]:
            nums[i + 1], nums[i] = nums[i], nums[i + 1]
    n += 1
string = str(nums)
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(string) - el - 1]
    symbols[len(string) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse[1:-1])
