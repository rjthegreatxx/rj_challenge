import re

class Solution(object):
    def validate(self, input):
        for i in range(len(input)):
                if i == 0:
                    continue
                num = input[i]
                test1 = bool(re.match(r"^[456]\d{15}$", num)) #It must start with a 4,5, or 6. &&  It must contain exactly 16 digits.
                test2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num)) #It must only consist of digits (0-9) && It must start with a 4,5, or 6. &&  It may have digits in groups of , separated by one hyphen "-"
                num = num.replace("-", "")
                test3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num)) #It must only consist of digits (0-9) && It must NOT use any other separator like ' ' , '_', etc. && It must NOT have 4 or more consecutive repeated digits.
                if (test1 or test2) and test3:
                    print("Valid")
                else:
                    print("Invalid")


def main():
    input = ["6","4123456789123456","5123-4567-8912-3456","61234-567-8912-3456","4123356789123456","5133-3367-8912-3456","5123 - 3567 - 8912 - 3456"]

    solution = Solution()
    result = solution.validate(input)


if __name__ == "__main__":
    main()
