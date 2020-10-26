# Программа запускается из консоли или из терминала
# Читайте README
import argparse # Импортируем библиотеку argparse

# Класс POLI состоит из методов инициализации (__init__),
# обработки(process), проверки(check), преобразователья на цифр (nums) и вычислений(calc)
class POLI: # Создать класс POLI
    def __init__(self,list): # Метод инициализации атрибута
        self.__list=list

    def process(self):  # Метод обработки
        lists=list(self.__list.split(','))  # Создаем список из строковых данных отделяя через запятую
        num=len(lists)  # Получем  длину списка
        if lists[num-1]=='':    # Если последний элемент списка пустой
            del lists[num-1]    # Удаляем этот элемент
        self.__list=lists   # Присваивать атрибуту список


    def check(self,number): # Метод проверки строк на принадлежность цифрам
        try:
            float(number)
            return True
        except Exception:
            return False

    def get_list(self):
        return self.__list

    def nums(self,list):    # Метод преобразования стороковых данных на числовых
        n_list=[]   # Пустой список для чисел
        for x in list: # Считаем каждый элемент
            n_list.append(float(x)) # И добавляем в переменную(список) преобразуя на число
        return n_list   # Возращаем список чисел

    def calculate(self,numbers):    # Метод вычисление
        try:    # Обрабатывем исключение (ошибку)
            i=0
            result=0
            while i<len(numbers): # Пока i меньше длины списка цикл продолжится
                result+=1/(numbers[i]*2)    # Результат
                i+=1    # Увелечение i с каждым циклом
            return result   # Возвращаем результат
        except Exception as err:    # Если было вызвано исключение(ошибка)
            print(err)  # Выводим ошибку
            exit()  # Завершить программу
# В главном методе используем библиотеку argparse чтобы получить данные из консоли или терминала
# Создаем обьект на основе класса POLI и вычисляем
def main ():
    parser = argparse.ArgumentParser(description='Strings')
    parser.add_argument('-p', action='store', dest='count', type=str)
    args = parser.parse_args()  # Получаем данные введенные пользователем
    Object1=POLI(args.count)    # Создать обьект
    Object1.process()   # Используем метод обработки
    lists=Object1.get_list()    # Получаем список данных
    for num in lists:   # Считаем каждый элемент списка
        flag=Object1.check(num) # Проверяем данные введенные пользователем
        if not flag:    # Если не правильно
            print('Вы ввели неправильные данные')
            exit()
            # Иначе
    nums=Object1.nums(lists) # Преобразуем в цифры
    result=Object1.calculate(nums) # И вычисляем
    print(result)

main()  # Выполнить программу