import random
import string

def generate_passwords(generation_type, letter_case, include_symbols, password_length, example_password):
    passwords = []
    
    if generation_type == '1':
        for i in range(10 ** password_length):
            password = str(i).zfill(password_length)
            passwords.append(password)
    else:
        characters = ''
        if letter_case == '1':
            characters += string.ascii_uppercase
        elif letter_case == '2':
            characters += string.ascii_lowercase
        elif letter_case == '3':
            characters += string.ascii_letters
        if include_symbols == '1':
            characters += string.punctuation
        
        example_characters = [ch for ch in example_password if ch.isalpha() or ch.isdigit() or ch in string.punctuation]

        for _ in range(len(characters) ** password_length):
            password = ''.join(random.choices(characters, k=password_length))
            new_password = ""
            for ch in example_characters:
                if ch.isalpha():
                    if ch.isupper():
                        new_password += random.choice(string.ascii_uppercase)
                    else:
                        new_password += random.choice(string.ascii_lowercase)
                elif ch.isdigit():
                    new_password += random.choice(string.digits)
                else:
                    new_password += random.choice(string.punctuation)
            passwords.append(new_password)

    random.shuffle(passwords)
        
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
    language = input("\nВыберите язык (1/2): ")
    if language == '1':
        return 'rus'
    elif language == '2':
        return 'eng'
    else:
        print("Неверный выбор. Пожалуйста, выберите язык снова.\n")
        return select_language()

def get_generation_type(language):
    if language == 'rus':
        print("\nВыберите тип генерации:")
        print("1. Цифры")
        print("2. Буквы")
        print("3. Комбинированный пароль")
        generation_type = input("\nВыберите тип генерации (1/2/3): ")
    elif language == 'eng':
        print("\nSelect generation type:")
        print("1. Digits")
        print("2. Letters")
        print("3. Mixed password")
        generation_type = input("\nSelect generation type (1/2/3): ")
    else:
        generation_type = input("\nSelect generation type (1/2/3): ")
    return generation_type

def get_letter_case(language):
    if language == 'rus':
        print("\nКакой регистр выбираете:")
        print("1. Верхний")
        print("2. Нижний")
        print("3. Комбинированный")
        letter_case = input("\nВыберите регистр (1/2/3): ")
    elif language == 'eng':
        print("\nSelect letter case:")
        print("1. Upper")
        print("2. Lower")
        print("3. Mixed")
        letter_case = input("\nSelect letter case (1/2/3): ")
    else:
        letter_case = input("\nSelect letter case (1/2/3): ")
    return letter_case

def get_include_symbols(language):
    if language == 'rus':
        print("\nДобавить символы в пароли:")
        print("1. Да")
        print("2. Нет")
        include_symbols = input("\nВыберите вариант (1/2): ")
    elif language == 'eng':
        print("\nInclude symbols in passwords:")
        print("1. Yes")
        print("2. No")
        include_symbols = input("\nSelect option (1/2): ")
    else:
        include_symbols = input("\nSelect option (1/2): ")
    return include_symbols

def get_password_length(language):
    if language == 'rus':
        password_length = int(input("\nКакой длины должны быть пароли (от 4 до 12 символов): "))
    elif language == 'eng':
        password_length = int(input("\nWhat should be the length of passwords (from 4 to 12 characters): "))
    else:
        password_length = int(input("\nWhat should be the length of passwords (from 4 to 12 characters): "))
    if password_length < 4:
        password_length = 4
    elif password_length > 12:
        password_length = 12
    return password_length

def get_example_password(language):
    if language == 'rus':
        example_password = input("\nВведите пример пароля (оставьте пустым, если не нужно): ")
    elif language == 'eng':
        example_password = input("\nEnter an example password (leave blank if not needed): ")
    else:
        example_password = input("\nEnter an example password (leave blank if not needed): ")
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
    example_password = get_example_password(language)

    passwords = generate_passwords(generation_type, letter_case, include_symbols, password_length, example_password)

    generate_passwords_file(passwords)

    if language == 'rus':
        print(f"\nСгенерированные пароли сохранены в файле 'generated_passwords.txt'.")
    elif language == 'eng':
        print(f"\nGenerated passwords are saved in the file 'generated_passwords.txt'.")
    else:
        print(f"\nGenerated passwords are saved in the file 'generated_passwords.txt'.")

if __name__ == "__main__":
    main()
