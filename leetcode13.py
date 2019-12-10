class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        temp=0
        it=iter(s)
        temp=next(it)
        conti=False
        for letter in s:
            try:
                temp = next(it)
            except StopIteration:
                # print(f'end of {s}')
                temp=''
            if conti:
                conti=False
                continue
            if letter is 'I':
                if temp is 'V':
                    count+=4
                    conti=True
                elif temp is 'X':
                    count+=9
                    conti = True
                else:
                    count += 1
            elif letter is 'V':
                count += 5
            elif letter is 'X':
                if temp is 'L':
                    count += 40
                    conti = True
                elif temp is 'C':
                    count += 90
                    conti = True
                else:
                    count += 10
            elif letter is 'L':
                count += 50
            elif letter is 'C':
                if temp is 'D':
                    count += 400
                    conti = True
                elif temp is 'M':
                    count += 900
                    conti = True
                else:
                    count += 100
            elif letter is 'D':
                count += 500
            elif letter is 'M':
                count += 1000
        print(f'count:{count}\ntemp:{temp}')
solu=Solution()
solu.romanToInt('IV')
solu.romanToInt('III')
solu.romanToInt('IX')
solu.romanToInt('LVIII')
solu.romanToInt("MCMXCIV")