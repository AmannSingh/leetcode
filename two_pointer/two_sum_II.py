class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        result = []
        right = len(numbers) - 1
        left = 0

        numbers.sort()

        while left < right:

            sum = numbers[right] + numbers[left]

            if sum == target:
                result.append(left+1)
                result.append(right+1)

                return result

            if sum < target:
                left += 1

            elif sum > target:
                right -= 1

        return result

def main():
    solution_object = Solution()

    numbers = [1, 2, 10, 4, 15, 7, 8, 12, 11]
    target = 17
    print(solution_object.twoSum(numbers, target))


if __name__ == "__main__":

    main()
