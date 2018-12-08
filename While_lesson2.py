




def ask_user():

    
    while True:
        ask_user_1 = (input("Как дела? "+"\n")).lower()

        for key in dic:
            if ask_user_1 == key.lower():
                print (dic.get(key))


        if ask_user_1 == ("Хорошо").lower():
            print ("Пока!")
            break   

dic = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Много сделал?" : " Не очень", "Что проходишь?" : "Циклы"}
example = ask_user()
