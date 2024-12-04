class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = (m + n) - 1 
        j = n - 1
        while i >= m:
            

def main():
    solution_object = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3 
    nums2 = [2, 5, 6]
    n = 3
    solution_object.merge(nums1, m, nums2, n)


if __name__ == "__main__":

    main()