import matplotlib.pyplot as plt


class Average:
    def __init__(self,file):
        self.__file=file
        self.__read=list()


    def read(self):
        file=open(self.__file,'r',encoding="utf-8")

        for line in file :
            self.__read.append(line.split())
        file.close()

    def sma(self):
        i=0
        standart=[]
        modified=[]
        value=int(input('Введите количество итераций : '))
        lenght=len(self.__read)

        while i< length:
            standart.append(self.__read[i][1])
            i += 1

        standart=[float(x) for x in standart]

        i=0
        while i<length:
            calc=0
            while i<value:
                modified.append(standart[i])
                i+=1

            for y in range(value):
                calc+=standart[i-y]
            modified.append(calc/value)
            i += 1
        time_list=list(range(0, length))
        return time_list, date, modified, standart

    def HSTG(self,time_list,date,modified,standart):
        plt.figure(figsize=(15, 7))
        plt.xlabel("Промежуток времени", fontsize='16', weight='bold')  # Ось X пишем описание
        plt.ylabel("Цены $", fontsize='16', weight='bold')  # ОСь Y пишем описание
        plt.title('Курс цен на фьючерсы нефти Brent', fontsize='16', weight='bold')  # Заголовок графика
        plt.xticks(time_list, date, fontsize=6, weight='bold')  # Ось X ставим дату
        plt.grid()  # Сетка

        plt.plot(time_list, modified, color='red', linestyle='solid', \
                 label='SMA', marker='o')  # Строим SMA график
        plt.plot(time_list, standart, color='blue', linestyle='solid', \
                 label='Стандартные значения', marker='>')  # Строим начальную график

        plt.legend(loc='upper right')  # Вставляем легенду

        plt.show()  # Отображаем график


def main:
    MA=Average('Oil.txt')
    MA.read()
    time_list, date, modified, standart=MA.sma()
    MA.HSTG(time_list,date,modified,standart)



main()