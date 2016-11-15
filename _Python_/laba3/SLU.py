import library
import codecs
import sys
string = open('C:\open.txt', 'rb')
WorkString = string.read()
WorkString = WorkString.decode("cp1251")
print(WorkString)
print("Введите x1: ")
x = input()
print("ВВедите Решение1: ")
solution = input()
print("Введите x2: ")
x2 = input()
print("Введите Решение2: ")
solution2 = input()
print('a%d + b = %d') %(x , solution)
print('a%d + b = %d') %(x2 , solution2)
print(x,x2)
if x > x2:
    a = x - x2
    solution3 = solution - solution2
else:
    a = x2 - x
    solution3 = solution2 - solution
if a < 0 or a > 31:
    a = a % 32
if solution3 < 0 or solution3 > 31:
    solution3 = solution3 % 32
revers = library.gcd(32,a,1,1)
alpha = solution3 * revers
if alpha < 0 or alpha > 31:
    alpha = alpha % 32
print(solution,x,alpha)
beta = (solution - x * alpha) % 32
alpha = library.gcd(32,alpha,1,1)
print("a = %d, b = %d") % (alpha, beta)
out = []

