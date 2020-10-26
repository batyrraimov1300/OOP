import matplotlib.pyplot as plt     # Импортируем библиотеку для графика

class dictionary:

    def __init__(self,file):    # Определьяем атрибуты данных
        self.__file= file   # Атрибут имени файла
        self.__dictionary=dict()    # Словарь
        self.__spammers=list()
        self.__name=list()

    def reading(self):  # Метод чтобы получить адреса и количество писем
        file = open(self.__file,'r',encoding='utf-8')
        lines= file.readlines()

        for line in lines:
            line_split=line.split(' ')

            if line_split[0]=='From':
                if line_split[1] in self.__dictionary.keys():
                    self.__dictionary[line_split[1]]+=1
                else:
                    self.__dictionary[line_split[1]]=1
        file.close()

    def X_DSPAM_Conf(self,name):    # Метод определьяющий спамеров по параметру Confidence
        file=open(self.__file,'r',encoding='utf-8')
        for x in file:
            y=x
            if 'X-DSPAM-Confidence' in x:
                i=0
                while i<5:
                    x=file.readline()
                    i+=1
                    if 'Author:' in x:
                        for n in name:
                            if n in x:
                                s=y.split()
                                length=len(s)
                                value=float(s[length-1])

                                if value>0.99:
                                    self.__spammers.append(n)
                                    num=name.index(n)
                                    del name[num]
        self.__name=name

    def date(self,name):    # Оаредельяем по количеству писем за 1 час
        file=open(self.__file,'r',encoding='utf-8')
        lists=[]
        for x in file:
            if 'Author:' in x :
                i=0
                while i<len(name):
                    if name[i] in x :
                        lists.append(x)
                        x=file.readline()
                        y=x.split(':')
                        lists.append(y[1])
                    i+=1
        spam_name=[]
        for n in name:
            date=[]
            i=0
            while i<len(lists):
                if n in lists[i]:
                    date.append(lists[i+1])
                    for el in date:

                        j=0
                        total=0
                        while j<len(date):
                            if el==date[j]:
                                total+=1
                                if total>5:
                                    spam_name.append(n)
                            j+=1
                i+=1
        sets=set()
        sets.update(spam_name)
        return sets
#################################################################################
    def get_nm_sp(self):    # Метод возврата значении
        return self.__spammers,self.__name
#############################################
    def __str__(self):  # Метод возврата значении
        return  self.__dictionary
#################################################################################

class Histogramm:   # Класс гистограмма
    def __init__(self,messages,name):
        self.__messages=messages
        self.__name=name

    def build(self):    # Метод графика

        plt.figure(figsize=(12,6))
        left_edges=[0]*46
        i=0
        for x in range(3,141,3):
            left_edges[i]=x
            i+=1
        heights=[]
        for x in self.__messages:
            heights.append(x)

        y_tick=[]
        for yt in range(0,205,5):
            y_tick.append(yt)
        s_yticks=[]
        for yt in y_tick:
            ys=str(yt)
            s_yticks.append(ys)
        plt.yticks(y_tick,s_yticks,fontsize=8)

        xtick=[]
        for num in range(3,141,3):
            xtick.append(num)
        s_xtick=[]
        for x in range(1,47):
            s_xtick.append(x)
        plt.xticks(xtick,s_xtick,fontsize=9)

        plt.title('Гистограмма по отправителям')  # Заголовок
        plt.xlabel('Отправители')  # Отправители на оси X
        plt.ylabel('Количество Писем')  # Количество писемь на оси Y

        print('Электронные почты по номеру на Гистограмме')
        print('--------------------------------------')
        for i, x in enumerate(self.__name):
            print(i + 1, '\t', '--------', x)

        plt.bar(left_edges, heights, 1)  # Создаем гистограмму
        plt.show()  # Выводим гистограмму на экран

#########################################################################################
def main ():    # Главная функция
    Dict_Object=dictionary('mbox.txt')  # Создаем обьект
    Dict_Object.reading()
    Dictionary=Dict_Object.__str__()    # Получаем словарь с эл.адресами
    Name=[]
    Messages=[]
    space= []

    for n,m in Dictionary.items():  # Раздельяем имена и количество сообщений
        Name.append(n)
        Messages.append(m)
    hist_names=space+Name

    Dict_Object.X_DSPAM_Conf(Name)
    Conf_Spam,names_dsp=Dict_Object.get_nm_sp()     # Получаем адреса спамеров
    date_sp=Dict_Object.date(names_dsp)
    date_sp.update(Conf_Spam)   # Общая множества спамеров
    for y,x in enumerate(date_sp):  # Печатаем имена спамеров
        print(y+1,' ',x,'//////спамер')
    histogramm=Histogramm(messages=Messages,name=hist_names)    # Создаем обьект гистограммы
    histogramm.build()  # Строим Гистограмму
main()  # Вызов функции
#########################################################################################