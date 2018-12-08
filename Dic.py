dic = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Много сделал?" : " Не очень", "Что проходишь?" : "Циклы"}

ask_user_1 = (input()).lower()

for key in dic:
    if ask_user_1 == key.lower():
        print (dic.get(key))