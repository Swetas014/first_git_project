#accept the list from user&find the factoraila of each no
# acceptf a character list from user and convert it into ASCII values
# accpept a string from user and  reverse the string and word as well
#     *
#     * *
#     * * *
#     * * * *


# def factorial(n):
#     fac = 1
#     while n!=1:
#         fac = fac*n
#         n = n-1
#     return fac
#
# if __name__ == "__main__":
#     num = eval(input("enter the list:"))
#     for item in num :
#         result = factorial(item)
#         print("factorial of number %d = %d" %(item, result))



# def ascii(ch):
#     l = [ord(ch) for item in ch]
#     return l
#
# if __name__ == "__main__":
#     ch = eval(input("enter the list:"))
#     for item in ch:
#         result = ascii(item)
#         print("ascii value of character ",result)


if __name__ == "__main__":
    ch = input("enter the string:")
    L = ch.split(" ")
    L.reverse()
    s1 = ' '.join(L)
    print(s1)

