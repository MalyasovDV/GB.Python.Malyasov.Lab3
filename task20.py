def countPoints(dictionary, word):
    sumOfPoints = 0
    for letter in word.upper():
        sumOfPoints += dictionary[letter]
    return sumOfPoints


oneDictionary = dict.fromkeys(["A", "E", "I", "O","U","L","N","S","T","R","А","В","Е","И","Н","О","Р","С","Т"], 1)
twoDictionary = dict.fromkeys(["D","G","Д","К","Л","М","П","У"], 2)
threeDictionary = dict.fromkeys(["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"], 3)
fourDictionary = dict.fromkeys(["F", "H", "V", "W", "Y" , "Й", "Ы"], 4)
fiveDictionary = dict.fromkeys(["K", "Ж", "З", "Х", "Ц", "Ч"], 5)
eightDictionary = dict.fromkeys(["J", "X", "Ш", "Э", "Ю"], 8)
tenDictionary = dict.fromkeys(["Q", "Z", "Ф", "Щ", "Ъ"], 10)
dictionary = oneDictionary | twoDictionary | threeDictionary | fourDictionary | fiveDictionary | eightDictionary | tenDictionary

word = input()
print(countPoints(dictionary, word))


