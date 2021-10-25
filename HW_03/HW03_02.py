# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# firstname = input("Введите ваше имя: ")
# lastname = input("Введите вашу фамилию: ")
# birth_year = input("Введите ваш город проживания: ")
# city = input("Введите ваш город: ")
# email = input("Введите ваш адрес электронной почты: ")
# phone = input("Введите ваш телефон: ")

def user_info(firstname, lastname, birth_year, city, email, phone):
    return ' '.join([firstname, lastname, birth_year, city, email, phone])


print(user_info(firstname='Kate', lastname='Pupok', birth_year='1990', city='Mosk', email='htoya@mail.ru',
              phone='89005553535'))