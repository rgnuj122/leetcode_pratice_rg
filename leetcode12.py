# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# IV            4
# IX            9
# XL            40
# XC            90
# CD            400
# CM            900
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=""
        valuelist=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbollist=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i=0
        while(True):
            if valuelist[i] > num:
                i+=1
                continue
            num-=valuelist[i]
            ans += symbollist[i]

            # for i,val in enumerate(valuelist):
            #     if val <= num:
            #         num-=val
            #         ans+=symbollist[i]
            #         print(f"num:{num}, ans:{ans}")

            if num <1:
                break
        return ans
solu=Solution()
print(f"{solu.intToRoman(3)}")
print(f"{solu.intToRoman(4)}")
print(f"{solu.intToRoman(9)}")
print(f"{solu.intToRoman(58)}")
print(f"{solu.intToRoman(1994)}")