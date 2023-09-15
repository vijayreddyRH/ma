def insertionSort(arr):
 if (n := len(arr)) <= 1:
 return
 for i in range(1, n):
 key = arr[i]

 j = i - 1
 while j >= 0 and key < arr[j]:
 arr[j + 1] = arr[j]
 j -= 1
 arr[j + 1] = key
# sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)




#############################3333



class Solution(object):
 def romanToInt(self, s):
 roman = 
{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
 i = 0
 num = 0
 while i < len(s):
 if i+1<len(s) and s[i:i+2] in roman:
 num+=roman[s[i:i+2]]
 i+=2
 else:
 num+=roman[s[i]]
 i+=1
 return num
ob1 = Solution()
print(ob1.romanToInt("III"))
print(ob1.romanToInt("CDXLIII"))




