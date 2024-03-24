class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        integer_to_roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }

        denominator = [1000, 100, 10, 1]
        for d in denominator:
            key = num // d
            if key > 0:
                if key * d in integer_to_roman.keys():
                    roman += integer_to_roman[key * d]
                else:
                    roman += integer_to_roman[d] * key
            num -= key * d
        roman = roman.replace('IIIII', 'V')
        roman = roman.replace('XXXXX', 'L')
        roman = roman.replace('CCCCC', 'D')
        return roman