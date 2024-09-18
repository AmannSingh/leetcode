class Solution:
    def remove_non_alphanumeric(self, s):

        str = ""
        for c in s:
            if c.isalnum():
                str += c

        return str

    def isPalindrome(self, s):

        s = s.lower()

        new_str = self.remove_non_alphanumeric(s)

        left = 0
        right = len(new_str) - 1

        while left < right:

            if new_str[left] == new_str[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


def main():

    solution_object = Solution()

    s = "A man, a plan, a canal: Panama"

    print(solution_object.isPalindrome(s))


if __name__ == "__main__":
    main()
