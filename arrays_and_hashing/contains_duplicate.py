class Solution: 
    def containsDuplicate(self, nums:list[int]) -> bool: 
        dict = {}
        for item in nums:
               dict = {}
        x = 0
        for i in nums:
                dict[i] = x
                x+=1
            
            
        if(len(dict) != len(nums)):
            return True
        else: 
            return False
        
def main():
    solution_object = Solution()
    nums = [1,2,3,4,5,1,2]
    print(solution_object.containsDuplicate(nums))

if __name__ == '__main__':
     main()