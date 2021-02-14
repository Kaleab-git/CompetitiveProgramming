# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):



#working version
class Solution:
    def firstBadVersion(self, n):
        l = 0; h = n
        while l < h:
            mid = (l+h)//2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid+1
        return l

        
        
        
        
        
        
        
    def firstBadVersion(self, n):
        versions = [version for version in range(1,n+1)]
        return self.quadi(versions, 0, len(versions))
        # return self.binSearch(versions, 0, len(versions))
    #active length range x and y
    def quadi(self, array, x, y):
        activeRange = y-x
        step = activeRange//5
        a = x + step
        b = x + 2*step
        c = x + 3*step
        d = x + 4*step
        while activeRange >= 10:
            if isBadVersion(array[a]):
                y = a
            elif isBadVersion(array[b]):
                x = a
                y = b
            elif isBadVersion(array[c]):
                x = b
                y = c
            else:
                x = d
            activeRange = y-x
            step = activeRange//5
            a = x + step
            b = x + 2*step
            c = x + 3*step
            d = x + 4*step
        for i in range(x, y+1):
            if isBadVersion(array[i]):
                return array[i]

    def quad(self, array, x, y):
        activeRange = y-x
        step = activeRange//5
        a = x + step
        b = x + 2*step
        c = x + 3*step
        d = x + 4*step
        
        if activeRange<=10:
            for i in range(x, y+1):
                if isBadVersion(array[i]):
                    return array[i]

        if isBadVersion(array[a]):
            return self.quad(array, x, a)
        elif isBadVersion(array[b]):
            return self.quad(array, a, b)
        elif isBadVersion(array[c]):
            return self.quad(array, b, c)
        else:
            return self.quad(array, d, y)
        
        
    
        
        
        
        
    def binSearch(self, array, l, h):
        mid = (h+l)//2
        if isBadVersion(array[mid]):
            if l!=mid and isBadVersion(array[mid-1]):
                while isBadVersion(array[mid-1]):
                    mid -= 1
                return array[mid]
            else:
                return array[mid]
        else:
            return self.binSearch(array, mid+1, h)

        
               
    def bin_search(self, array, l, h):
        mid = (h+l)//2
        if isBadVersion(array[mid]):
            if l!=mid and isBadVersion(array[mid-1]):
                return self.bin_search(array, l, mid-1)
            else:
                return array[mid]
        else:
            return self.bin_search(array, mid+1, h)