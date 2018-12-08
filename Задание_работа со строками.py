
# Вывести последнюю букву в слове
word = 'Архангельск'
print("Последняя буква: " + word[-1] + '\n')
# ???


# Вывstr(ести коли)чество букв а в слове
word = 'Архангельск'
print("Длина строки: " + str(len(word)) + '\n')
# ???


# Вывstr(ести коли)чество гласных букв в слове
word = 'Архангельск'
num_values = 0
vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
for letter in word.lower():
    if letter in vowels: 
        num_values+=1

print("Количество гласных: " + str(num_values) + '\n')

# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
split_sentence = sentence.split()
print ("Количество слов: " + str(len(split_sentence)) + '\n')

# ???


# Вывести первую букву каждого слова на отдельной строке
sentence_new = 'Мы приехали в гости'
split_new_sentence = sentence_new.split()
for word in split_new_sentence:
    letter = word[0]
    print ("Первая буква в слове: " + letter + '\n')


# Вывести усреднённую длину слова.
lenght=0
sentence = 'Мы приехали в гости'
new_list = sentence.split()
for new_word in new_list:
    lenght = lenght + len(new_word)
    average = lenght/len(new_list)
print ("Средняя длина слова: " + str(average) + '\n')


# ???