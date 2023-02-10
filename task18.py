def fillList(someList, n):
    for i in range(n):
        someList.append(int(input()))

def findNumber(someList, number):
    diff = abs(someList[0] - number)
    closestNumber = someList[0]
    for element in someList:
        if (abs(element - number) < diff):
            closestNumber = element
            diff = abs(element - number)
    return closestNumber


print("Введите количество чисел")
n = int(input())
numberList = []

print("Введите числа")
fillList(numberList, n)

print("Введите число X")
number = int(input())
print(f"Самое близкое число для введенного числа {number}: {findNumber(numberList, number)}")