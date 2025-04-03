class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        bigstring = ["Thousand","Million","Billion"]
        result = self.notoword(num % 1000)
        num = num // 1000

        for i in range(len(bigstring)):
            if num % 1000 > 0:
                result = self.notoword(num % 1000) + bigstring[i] + " " + result
            num = num // 1000

        return result.strip()

    def notoword(self, num):
        digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""
        if num > 99:
            result += digitString[num // 100] + " Hundred "
        
        num = num % 100

        if num > 9 and num < 20:
            result += teenString[num - 10] + " "
        else:
            if num >= 20:
                result += tenString[num // 10] + " "
            num = num % 10
            if num > 0:
                result += digitString[num] + " "
        return result 


