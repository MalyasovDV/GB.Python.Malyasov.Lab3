def fillList(someList, n):
    for i in range(n):
        someList.append(int(input()))

def countNumber(someList, number):
    count = 0
    for element in someList:
        if (element == number):
            count += 1
    return count

print("Введите количество чисел")
n = int(input())
numberList = []

print("Введите числа")
fillList(numberList, n)

print("Введите искомое число")
number = int(input())
print(f"Количество введенного числа {number} встречено: {countNumber(numberList,number)}")