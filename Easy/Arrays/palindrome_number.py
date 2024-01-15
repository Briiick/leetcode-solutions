# initial long form solution
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        str_x = str(x)
        spl_str_x = list(str_x)
        half_len = len(spl_str_x)

        for i in range(0, half_len):
            start = spl_str_x[i]
            end = spl_str_x[-1-i]
            check = int(start) - int(end)
            output = True if check == 0 else False
            if output == False:
                return False
        return True
    

# initial short form solution:
def isPalindrome(self, x: int) -> bool:
	if x < 0:
		return False
	
    # reminder... you can do this to a string to just reverse it
	return str(x) == str(x)[::-1]


# without str()
def isPalindrome(self, x: int) -> bool:
    # negative never works
	if x<0:
		return False

    # new num is a function of the previous newNum (starting at 0)
    # and then multiplying it by 10 and adding the x mod 10
    # so for the number 1551
    # first number 1
    # second number 15
    # etc..
	inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x // 10
	return newNum == inputNum
