class Solution(object):
    def twoSum(self, nums, target):
        
        dict = {}
        result = [] 

        for i in range(len(nums)):

            # determine the difference between the target and the current integer in nums 
            diff = target - nums[i]

            # check to see if the difference is stored in the dictionary 
            # if it is then append the position of current integer in the array 
            # and the value of the diff (key) in the dictionary 

            if(diff in dict):
                result.append(i)
                result.append(dict[diff])

                # if the diff is not in the dictionary, store the current integer in nums in the dictionary 
                # and it's position in the array 
            else:
                dict[nums[i]] = i 
                
        return result   

def main():
    nums = [3,2,4]
    target = 6
    solution_object = Solution()
    print(solution_object.twoSum(nums,target))

if __name__ == '__main__':
    main()