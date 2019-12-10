# import operator
class Solution:
    def absdiff(self,i,j):
        if i >= j:
            return i-j
        else:
            return j-i
    def countArea(self,p1,p2,dist):
        print('{},{},{}'.format(p1,p2,dist))
        if p1 > p2:
            return p2*dist
        else:
            return p1*dist
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ranlist=list(range(len(height)))
        reversedlist = reversed(list(range(len(height))))
        it = iter(ranlist)
        itr = iter(reversedlist)
        ittmp = next(it)
        itrtmp = next(itr)
        print('{},{}'.format(ittmp,itrtmp))
        maxarea = 0
        while(True):
            dist=itrtmp-ittmp
            tmpArea=self.countArea(height[ittmp],height[itrtmp],dist)
            # tmpArea=dist*self.absdiff(ittmp,itrtmp)
            if tmpArea > maxarea: # record max value
                maxarea=tmpArea
            if height[ittmp] > height[itrtmp]: # keep bigger value
                itrtmp = next(itr) # forwards
            else:
                ittmp = next(it)
            print('{},{}'.format(ittmp,itrtmp))
            if ittmp >= itrtmp:
                break
        return maxarea
        print('{}'.format(maxarea))
        # cord=list(zip(ranlist,height))

        # cord.sort(key=operator.itemgetter(1)) #slightly faster, https://stackoverflow.com/questions/8459231/sort-tuples-based-on-second-parameter

        # print(f'{type(cord)},{cord}')

        # dictcord = dict(zip(ranlist,height))
        # print(f'{dictcord},h:{height},ran:{ranlist}')
        # sorted_x = sorted(dictcord.items(), key=operator.itemgetter(1))
        # print(f'{type(sorted_x)}')
        # print(f'{sorted_x[0][1]}')

solu=Solution()
print(f"{solu.maxArea([1,8,6,2,5,4,8,3,7])}")
print(f"{solu.maxArea([2,3,4,5,18,17,6])}")