num_one = input("Input first number: ")
num_two = input("Input second number: ")


def get_summ(num_one, num_two):
    try:
            num_one = int(num_one)
            num_two = int(num_two)
            summ = num_one + num_two
            return f"Итого: {summ}"    

    except ValueError:
        return "Введите цифровое значение"     
                   
    
    


result = get_summ(num_one, num_two)
print(result)