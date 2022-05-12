import random #для генерации токена
import string #для очистки списка от ненужных символов


'''Переменные'''
TokenLenght = 1 #длина токена
shortLink = " " #короткая ссылка
infinity = True #переменная для продолжения работы программы
token = []      #созданный токен


'''Список для вывода токена https://.../<токен>'''
list_values = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
              'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 
              'c', 'd', 'e', 'f', 'g', 'h', 'i', 
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 
              'q', 'r', 's', 't', 'u', 'v', 'w', 
              'x', 'y', 'z', '1', '2', '3', '4', 
              '5', '6', '7', '8', '9', '0' ]


'''Вырезалка'''
print()
print("-- Введите вашу исходную ссылку, а я ее сокращу --")
while infinity == True:
    inputURL = input(str("('q' для выхода): ")) #вставка оригинальной ссылки

    #Убираем лишнее кроме "https://"
    if inputURL[0:4] == 'http': 
        if inputURL[4] == 's': 
            spicok = inputURL.split('/')        #забираются прямые слеши
            spicok[1] = '//'                    #во второй элемент добавляется двойной слеш
            del spicok[3:]                      #удаляем остальную часть списка
            domen_name = spicok[2]              #передаем переменной доменное имя
            index = 0                           #объявляем для прохода по элементам строки доменного имени
            short_domen = ''                    #объявляем будущий короткий домен

            #Производим операцию по удалению лишних символов из доменного имени
            for elem in domen_name:
                if elem == '.':
                    pass
                    index = -2
                if index > 1:
                    pass
                else:
                    short_domen += elem
                index+=1

            spicok[2] = short_domen             #закидываем в список короткий домен
            spicok.append('/')                  #добавлем прямой слэш для отделения доменного имени от токена

            while TokenLenght <= 6: #генерация токена
                token.append(random.choice(list_values))
                TokenLenght+=1

            ''' Вывод сокращенной ссылки'''    
            shortLink = spicok + token
            print("Сокращенная ссылка > " + "".join(shortLink))
            token.clear()
            TokenLenght = 0
            print()

        #Убираем лишнее кроме "http://". Алгоритм аналогичен
        elif inputURL[4] != 's':            
            spicok = inputURL.split('/') #забираются прямые слеши
            spicok[1] = '//'
            del spicok[3:]
            domen_name = spicok[2]              
            index = 0                          
            short_domen = ''                    

            for elem in domen_name:
                if elem == '.':
                    pass
                    index = -2
                if index > 1:
                    pass
                else:
                    short_domen += elem
                index+=1

            spicok[2] = short_domen             
            spicok.append('/')                  

            while TokenLenght <= 6: #генерация токена
                token.append(random.choice(list_values))
                TokenLenght+=1         

            ''' Вывод сокращенной ссылки'''
            shortLink = spicok + token 
            print("Сокращенная ссылка > " + "".join(shortLink))
            token.clear()
            TokenLenght = 0
            print()
    elif inputURL == 'q': #Выход из программы
        infinity = False
        print() 
    else: #Ошибка
        print()
        print("Введите полную ссылку, начиная с 'http(s)'")
