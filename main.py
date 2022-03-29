from itertools import permutations

try:
    words = input("Podaj dwa wyrazy: ")

    x = words.split()

    word1 = str(x[0])
    word2 = str(x[1])

    result = ""
    for i in word2: 
        if i in word1:
            result += i

    def words(letters):
        for n in range(1, len(letters)+1):
            yield from map(''.join, permutations(letters, n))

    for word in words(result):
        set_words = list(words(result))

    result_list_of_words = []
    for i in set_words:
        if i in word1:
            if i in word2: 
                result_list_of_words.append(i)

    print(max(result_list_of_words, key=len))

except:
    print("Nie znaleziono części wspólnej!")
