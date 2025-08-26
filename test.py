
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        Even = 0
        ODD = 0
      
        for x in range(2,n*2+1,2):
            Even += x
        
        print("This is even- ",Even)

        for x in range(1,n*2,2):
            ODD += x
        print("This is Odd",ODD)
        max1 = 0
        for x in range(1,max(Even,ODD)+1):
            if Even%x == 0 and ODD%x == 0 and max1 < x:
                max1 = x
        print(max1)
        return max1




sol = Solution()
k = int(input("Enter a number: "))
print("GCD of odd and even sums:", sol.gcdOfOddEvenSums(k))
