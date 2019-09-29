import random


# Создание тестовых файлов
def test_one(module_fixture):
    """Вызов фикстуры Модуль"""


# Операции со строками
def test_str(function_fixture):
    """Сложение строк и проверка полученного результата"""
    a = 'py'
    b = 'th'
    c = 'on'
    d = a + b + c
    print('Hello, ' + (d) + '!')
    assert d == 'python'


# операции с числами
def test_number():
    """сложение чисел, после преобразования из строки и проверка результата"""
    a = '25'
    assert int(a) + 1 == 26


def test_numtwo():
    """Сложение рандомных чисел из заданного диапазона"""
    a = random.randint(1, 2)
    k = random.randint(3, 4)
    c = a + k
    if c < 5:
        print('с=4')
    elif c == 5:
        print('c=5')
    else:
        print('c=7')


# операции со списком
def test_list(function_fixture):
    """Формирование списка и проверка его длины"""
    list1 = ['a', 'b']
    list1.pop(1)
    list1.insert(1, 'pp')
    list1.append('e')
    list1.insert(3, 'le')
    print(list1)
    assert len(list1) == 4


# операции со словарями
def test_dict(function_fixture):
    """Добавление значения в словарь. Вывод всех значений словаря"""
    d = {'Leningradskaya oblast': 'St.Peterburg', "Moskovskaja oblast": "Moskva"}
    d['Voronezhskaja oblast'] = 'Voronezh'
    print(d)


# операции с кортежами
def test_tuple(function_fixture):
    """Формирование и вывод типа кортеж"""
    a = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
    b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    print('Список "a" имеет - ', type(a))
    print('Список "b" имеет тип - ', type(b))
    print('Кортеж "a" преобразован в список и имеет тип- ', type(list(a)))


# операции с множествами
def test_set(function_fixture):
    """Формирование множества. Проверка вхождения одного множества в другое"""
    s = set('11223344556677889900')
    s1 = 'a' in s
    print(s)
    assert s == set('1234567890')
    print(s1, '- Вхождение символа "а" в множество', s)
    print(s == set('1234567890'), '- Вхождение множества "1234567890" в множество "11223344556677889900"')


def test_three(random_fixture):
    """Вызов фикстуры, которая формирут рандомное значение в диапазоне от 1 до 1200"""
    print(random_fixture)


def test_two(session_fixture):
    """Вызов фикстуры Сессия"""
    pass
