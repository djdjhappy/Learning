def factorial(num):
    return 1 if num <= 1 else num * factorial(num - 1)
#print(factorial(3))
def bunnyEars(num):
    return 0 if num == 0 else bunnyEars(num - 1) + 2
##print(bunnyEars(2))
def fibonacci(num):
    return num if num < 2 else fibonacci(num - 2) + fibonacci(num - 1)
##print(fibonacci(0))
##print(fibonacci(1))
##print(fibonacci(2))
##print(fibonacci(3))
##print(fibonacci(4))
##print(fibonacci(5))
##print(fibonacci(6))
##print(fibonacci(7))
def bunnyEars2(num):
    return 0 if num == 0 else bunnyEars2(num - 1) + 3 - num % 2
def triangle(rows):
    return rows if rows <= 1 else triangle(rows - 1) + rows
def sumDigits(num):
    return num if num < 10 else sumDigits(num // 10) + num % 10
##print(sumDigits(12345))
def count7(n):
    if n == 0:return 0
    cnt = 1 if n % 10 == 7 else 0
    return count7(n // 10) + cnt
##print(count7(17747676777))
def count8(n, last = 0):
    if n == 0:return 0
    is8 = n % 10 == 8#这个数末位是否为8
    cnt = last + 1 if is8 else 0
    if is8:
        cnt2 = count8(n // 10, last + 1)
    else:
        cnt2 = count8(n // 10, 0)
    return cnt + cnt2
#print(count8(88888))
def powerN(base, n):
    return base * powerN(base, n - 1) if n > 0 else 1
#print(powerN(5, 3))
def countX(string):
    if not string:return 0
    count = int(string[0] == 'x')
    return count + countX(string[1:])
def countHi(string):
    if not string:return 0
    count = int(string[:2] == 'hi')
    return count + countHi(string[2:] if count else string[1:])
##print(countHi("ihiihihixhi"))
def changeXY(string):
    if not string:return string
    prefix = "y" if string[0] == 'x' else string[0]
    return prefix + changeXY(string[1:])
##print(changeXY("3x4xfxddx;7x"))
def changePi(string):
    if not string:return string
    if string[:2] == "pi":
        return "3.14" + changePi(string[2:])
    return string[0] + changePi(string[1:])
##print(changePi("pipi1.pipi;xnodspip["))
def noX(string):
    if not string:return string
    prefix = '' if string[0] == 'x' else string[0]
    return prefix + noX(string[1:])
##print(noX("xy1x3sx;5x.67x"))
def array6(nums, index):
    if index >= len(nums):return False
    if nums[index] == 6:return True
    return array6(nums, index + 1)
##print(array6([0, 5, 1, 7, 6, 3, 0], 0))
def array11(nums, index):
    if index >= len(nums):return 0
    cnt = int(nums[index] == 11)
    return cnt + array11(nums, index + 1)
##print(array11([1, 0, 11, 4, 3, 11, 1, 11], 0))
def array220(nums, index):
    if index >= len(nums) - 1:return False
    if nums[index] * 10 == nums[index + 1]:return True
    return array220(nums, index + 1)
##print(array220([1, 0, 3, 0, 4, 41, 1, 0], 0))
def allStar(string):
    if len(string) <= 1:return string
    return string[0] + '*' + allStar(string[1:])
##print(allStar("1234567890"))
def pairStar(string):
    if len(string) <= 1:return string
    if string[0] == string[1]:
        return string[0] + "*" + pairStar(string[1:])
    return string[0] + pairStar(string[1:])
##print(pairStar("Hello, worldddxx"))
def endX(string):
    if len(string) <= 1:return string
    if string[0] == 'x':
        return endX(string[1:]) + 'x'
    return string[0] + endX(string[1:])
##print(endX("11x31fxx3"))
def countPairs(string):
    if len(string) < 3:return 0
    cnt = int(string[0] == string[2])
    return cnt + countPairs(string[1:])
##print(countPairs("ihihhh"))
def countAbc(string):
    if len(string) < 3:return 0
    cnt = int(string[:3] == 'abc' or string[:3] == 'aba')#两种子串可重复
    return cnt + countAbc(string[1:])
##print(countAbc("heababcbabbcbabc"))
def count11(string):
    #子串不允许重复
    if len(string) < 2:return 0
    if string[:2] == "11":
        return 1 + count11(string[2:])
    return count11(string[1:])
##print(count11("abc11x11x11"))
def stringClean(string):
    if len(string) < 2:return string
    prefix = "" if string[0] == string[1] else string[0]
    return prefix + stringClean(string[1:])
##print(stringClean("Hello Bookkeeper"))
def countHi2(string):
    if len(string) < 2:return 0
    if string[:3] == 'xhi':
        return countHi2(string[3:])
    if string[:2] == 'hi':
        return 1 + countHi2(string[2:])
    return countHi2(string[1:])
##print(countHi2("xhihihix"))
def parenBit(string):
    if not string:return string
    if string[0] != '(':
        return parenBit(string[1:])
    if string[-1] != ')':
        return parenBit(string[:-1])
    return string
##print(parenBit("1234(cbkio)r4xcnjki"))
def nestParen(string):
    if not string:return True
    if string[0] == '(' and string[-1] == ')':
        return nestParen(string[1:-1])
    return False
##print(nestParen("(((())))"))
def strCount(string, sub):
    slen = len(sub)
    if len(string) < slen:return 0
    if string[:slen] == sub:
        return 1 + strCount(string[slen:], sub)
    return strCount(string[1:], sub)
##print(strCount("cacatcowcat", "cat"))
def strCopies(string, sub, n):
    #子串可以重复
    slen = len(sub)
    if len(string) < slen:
        return n <= 0
    if string[:slen] == sub:
        return strCopies(string[1:], sub, n - 1)
    return strCopies(string[1:], sub, n)
##print(strCopies("ijiiiiiij", "iiii", 3))
def strDist(string, sub):
    subl = len(sub)
    stringl = len(string)
    if stringl < subl:
        return 0
    if string[:subl] != sub:
        return strDist(string[1:], sub)
    if string[stringl - subl:] != sub:
        return strDist(string[:-1], sub)
    return stringl
##print(strDist("catcowcat", "cat"))
##print(strDist("catcowcat", "cow"))
##print(strDist("cccatcowcatxx", "cat"))

