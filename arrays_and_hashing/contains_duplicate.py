class Solution: 
    def containsDuplicate(self, nums:list[int]) -> bool: 
        dict = {}

        #push items into dictionary and set it's value to 1 
        for i in nums:

            # if the item is seen again increment its value by 1 
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1 
        
        #check to see if an item showed up more than once in the nums list 
        #by checking if value of the key is > 1 
        for key in dict:
            if(dict[key] > 1):
                return True 
        
        return False 

        
def main():
    solution_object = Solution()
    nums = [1,2,3,4,5]
    print(solution_object.containsDuplicate(nums))

if __name__ == '__main__':
     main()