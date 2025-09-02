def main():
    nums = [2,7,11,15]
    print(twoSum(nums,9))
def twoSum(nums,target):
    for index,number in enumerate(nums):
        for i in range(len(nums)) :
            if (nums[i] + number == target) & (i != index):
                return index, i


    
main()
