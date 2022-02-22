import random #для генерации токена
import string #для очистки списка от ненужных символов


'''Переменные'''
TokenLenght = 1 #длина токена
shortLink = " " #короткая ссылка
infinity = True
token = []

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
while infinity == True:
    inputURL = input(str(": ")) #вставка оригинальной ссылки

    if inputURL[0:4] == 'http': 
        #Убираем лишнее кроме "https://"
        if inputURL[4] == 's': 
            spicok = inputURL.split('/') #забираются прямые слеши
            spicok[1] = '//' #во второй элемент добавляется двойной слеш
            count_elem_spicok = len(spicok) #кол-во элементов в списке

            if count_elem_spicok > 2:
                del spicok[2:count_elem_spicok]
                spicok.append('tinyref.org/')

                while TokenLenght <= 6: #генерация токена
                    token.append(random.choice(list_values))
                    TokenLenght+=1

                ''' Вывод сокращенной ссылки'''    
                shortLink = spicok + token
                print("Сокращенная ссылка > " + "".join(shortLink))
                token.clear()
                TokenLenght = 0
                print()

        elif inputURL[4] != 's':
            #Убираем лишнее кроме "http://"
            spicok = inputURL.split('/') #забираются прямые слеши
            spicok[1] = '//' #во второй элемент добавляется двойной слеш
            count_elem_spicok = len(spicok) #кол-во элементов в списке

            if count_elem_spicok > 2:
                del spicok[2:count_elem_spicok]
                spicok.append('tinyref.org/')

                while TokenLenght <= 6: #генерация токена
                    token.append(random.choice(list_values))
                    TokenLenght+=1

                ''' Вывод сокращенной ссылки'''
                shortLink = spicok + token 
                print("Сокращенная ссылка > " + "".join(shortLink))
                token.clear()
                TokenLenght = 0
                print()
    else:
        print("Введите полную ссылку, начиная с 'http(s)'")

