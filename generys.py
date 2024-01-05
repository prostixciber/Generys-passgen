import random
import string

def generate_passwords(generation_type, letter_case, include_symbols, password_length, num_passwords, example_password):
    passwords = []
    
    for _ in range(num_passwords):
        password = ''
        
        if generation_type == '1':
            password = ''.join(random.choices(string.digits, k=password_length))
        elif generation_type == '2':
            if letter_case == '1':
                password = ''.join(random.choices(string.ascii_uppercase, k=password_length))
            elif letter_case == '2':
                password = ''.join(random.choices(string.ascii_lowercase, k=password_length))
            elif letter_case == '3':
                password = ''.join(random.choices(string.ascii_letters, k=password_length))
        elif generation_type == '3':
            if letter_case == '1':
                characters = string.ascii_uppercase + string.digits
            elif letter_case == '2':
                characters = string.ascii_lowercase + string.digits
            elif letter_case == '3':
                characters = string.ascii_letters + string.digits
            if include_symbols == '1':
                characters += string.punctuation
            password = ''.join(random.choices(characters, k=password_length))
        else:
            password = example_password
        
        passwords.append(password)
    
    return passwords

def generate_password_from_example(password, example_password):
    generated_password = ''
    
    for char in example_password:
        if char.isalpha():
            if char.isupper():
                generated_password += random.choice(string.ascii_uppercase)
            else:
                generated_password += random.choice(string.ascii_lowercase)
        elif char.isdigit():
            generated_password += random.choice(string.digits)
        else:
            generated_password += random.choice(string.punctuation)
    
    return generated_password

def print_logo():
    logo = '''
   .g8"""bgd                                                            
 .dP'     `M                                                            
 dM'       `   .gP"Ya  `7MMpMMMb.   .gP"Ya  `7Mb,od8 `7M'   `MF',pP"Ybd 
 MM           ,M'   Yb   MM    MM  ,M'   Yb   MM' "'   VA   ,V  8I   `" 
 MM.    `7MMF'8M""""""   MM    MM  8M""""""   MM        VA ,V   `YMMMa. 
 `Mb.     MM  YM.    ,   MM    MM  YM.    ,   MM         VVV    L.   I8 
   `"bmmmdPY   `Mbmmd' .JMML  JMML. `Mbmmd' .JMML.       ,V     M9mmmP' 
                                                        ,V              
                                                     OOb"               
    '''
    print(logo)
    print("by misterX\n")

def select_language():
    print("In what language do you want to continue working?")
    print("1. Русский [Rus]")
    print("2. English [Eng]")
    language = input("Выберите язык (1/2): ")
    if language == '1':
        return 'rus'
    elif language == '2':
        return 'eng'
    else:
        print("Неверный выбор. Пожалуйста, выберите язык снова.")
        return select_language()

def get_generation_type(language):
    if language == 'rus':
        print("Выберите тип генерации:")
        print("1. Цифры")
        print("2. Буквы")
        print("3. Комбинированный пароль")
        generation_type = input("Выберите тип генерации (1/2/3): ")
    elif language == 'eng':
        print("Select generation type:")
        print("1. Digits")
        print("2. Letters")
        print("3. Mixed password")
        generation_type = input("Select generation type (1/2/3): ")
    else:
        generation_type = input("Select generation type (1/2/3): ")
    return generation_type

def get_letter_case(language):
    if language == 'rus':
        print("Какой регистр выбираете:")
        print("1. Верхний")
        print("2. Нижний")
        print("3. Комбинированный")
        letter_case = input("Выберите регистр (1/2/3): ")
    elif language == 'eng':
        print("Select letter case:")
        print("1. Upper")
        print("2. Lower")
        print("3. Mixed")
        letter_case = input("Select letter case (1/2/3): ")
    else:
        letter_case = input("Select letter case (1/2/3): ")
    return letter_case

def get_include_symbols(language):
    if language == 'rus':
        print("Добавить символы в пароли:")
        print("1. Да")
        print("2. Нет")
        include_symbols = input("Выберите вариант (1/2): ")
    elif language == 'eng':
        print("Include symbols in passwords:")
        print("1. Yes")
        print("2. No")
        include_symbols = input("Select option (1/2): ")
    else:
        include_symbols = input("Select option (1/2): ")
    return include_symbols

def get_password_length(language):
    if language == 'rus':
        password_length = int(input("Какой длины должны быть пароли (от 4 до 12 символов): "))
    elif language == 'eng':
        password_length = int(input("What should be the length of passwords (from 4 to 12 characters): "))
    else:
        password_length = int(input("What should be the length of passwords (from 4 to 12 characters): "))
    if password_length < 4:
        password_length = 4
    elif password_length > 12:
        password_length = 12
    return password_length

def get_num_passwords(language):
    if language == 'rus':
        num_passwords = int(input("Введите количество паролей для генерации от 1000 до 10000000: "))
    elif language == 'eng':
        num_passwords = int(input("Enter the number of passwords to generate (from 1000 to 10000000): "))
    else:
        num_passwords = int(input("Enter the number of passwords to generate (from 1000 to 10000000): "))
    if num_passwords < 1000:
        num_passwords = 1000
    elif num_passwords > 10000000:
        num_passwords = 10000000
    return num_passwords

def get_example_password(language):
    if language == 'rus':
        example_password = input("Введите пример пароля (оставьте пустым, если не нужно): ")
    elif language == 'eng':
        example_password = input("Enter an example password (leave blank if not needed): ")
    else:
        example_password = input("Enter an example password (leave blank if not needed): ")
    return example_password

def generate_passwords_file(passwords):
    with open('generated_passwords.txt', 'w') as file:
        file.write('\n'.join(passwords))

def main():
    print_logo()
    language = select_language()
    generation_type = get_generation_type(language)
    if generation_type == '2' or generation_type == '3':
        letter_case = get_letter_case(language)
    else:
        letter_case = '0'
    include_symbols = get_include_symbols(language)
    password_length = get_password_length(language)
    num_passwords = get_num_passwords(language)
    example_password = get_example_password(language)

    passwords = generate_passwords(generation_type, letter_case, include_symbols, password_length, num_passwords, example_password)

    generate_passwords_file(passwords)

    if language == 'rus':
        print(f"Сгенерированные пароли сохранены в файле 'generated_passwords.txt'.")
    elif language == 'eng':
        print(f"Generated passwords are saved in the file 'generated_passwords.txt'.")
    else:
        print(f"Generated passwords are saved in the file 'generated_passwords.txt'.")

if __name__ == "__main__":
    main()
