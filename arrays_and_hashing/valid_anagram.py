class Solution: 
    def isAnagram(self, s: str, t:str) -> bool:
        
        s_dict = {}
        t_dict ={}
        
        if (len(s)!= len(t)):
            return False
        
        #count each character in each string and insert into dictionary
        for i in range(len(s)):
            s_dict [s[i]] = 1 + s_dict.get(s[i],0)
            t_dict [t[i]] = 1 + t_dict.get(t[i],0)
        
        # check if the dictionaries are the same 
        return s_dict == t_dict
def main():
    s = 'anagram'
    t= 'nagaram'
    solution_object = Solution()
    print(solution_object.isAnagram(s,t))

if __name__ == '__main__':
    main()

