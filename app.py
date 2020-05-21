# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# W Python wszystko jest obiektem. Niewazne czy liczba, napis czy struktura opisujaca
# dowolny byt. Mozemy tez latwo sprawdzic do jakiej klasy nalezy dowolny obiekt:

number = 11

print(f'ID OF number = {id(number)}')

print(f'TYPE OF number VARIABLE IS {type(number)}')

# Mozemy tez sprawdzic czy dany obiekt jest konretnym typem
print(f'IS number INSTANCE OF int: {isinstance(number, int)}')

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# PODZIAL OBIEKTOW

# a. IMMUTABLE
# Ich stan / zawartosc nie moga zostac zmienione po utworzeniu
# int, float, long, complex, string, tuple, bool

# b. MUTABLE
# Ich stan / zawartosc moga zostac zmienione po utworzeniu
# list, dict, set, byte array, user-defined class

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# RODZAJE OBSZAROW PAMIECI

# CALL STACK
# Przechowywanie informacji na temat kolejnosci wywolania poszczegolnych funkcji

# STACK
# Przechowywanie danych potrzebnych do wywolania funkcji / metody
# Kiedy dana funkcja jest wywolana wszystkie zwiazane z nia zmienne sa
# umieszczane na stosie. Kiedy funkcja konczy swoje dzialanie CALL STACK
# przechodzi do kolejnej funkcji, a wszystkie powiazane z zakonczona
# funkcja zmienne sa usuwane ze stosu
# Rozmiar stosu jest znany poniewaz jest ustalany podczas kompilacji

# HEAP
# Przechowuje dane, ktorych rozmiar zmienia sie dynamicznie w trakcie dzialania
# aplikacji. Pamiec jest uzywana przez wszystkie funkcje oraz w zakresie
# globalnym - nie tylko w zakresie danej funkcji.
# PYTHON MEMORY MANAGER alokuje prywatny heap. Przechowuje on wszystkie obiekty
# naszej aplikacji, ktore w momencie kiedy nie sa potrzebne sa zwalniane przez
# mechanizm GARBAGE COLLECTOR.
# Zwalniania pamieci odbywa sie dzieki dzialaniu mechanizmu REFERENCE COUNTING.
# Mechanizm zlicza ile referencji pokazuje na dany obszar i jezeli nie ma takich
# referencji GARBAGE COLLECTOR zwalnia ten obszar.

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Kiedy tworzysz napis 'ala' i przypisujesz mu refernecje n_1 a nastepnie utworzysz
# ponownie napis 'ala' i przypiszesz mu referencje n_2 to n_1 oraz n_2 beda reprezentowac
# ten sam obszar pamieci

n_1 = 'ala'
n_2 = 'ala'

print(id(n_1))
print(id(n_2))

# Podobnie dla zmiennej integer
i_1 = 10
i_2 = 10

print(id(i_1))
print(id(i_2))

# mamy rowniez operator is, ktory sprawdza czy jeden obiekt wskazywany przez jedna referencje
# jest tym samym obiektem na ktory wskazuje druga referencja
print(i_1 is i_2)
print(i_1 is not n_2)

# na czym polega IMMUTABILITY?
num_1 = 39
print(id(num_1))
num_1 = num_1 + 1
print(f'ID OF num_1 = {id(num_1)}')  # w tym miejscu obiekt 39 juz nie jest potrzebny, num_1 wskazuje teraz na
# nowy obiekt, ktory zostal utworzony w wyniku przeprowadzonego wyzej dodawania
print(f'ID OF num_1 = {id(num_1)}')

# kolejny przyklad
val_1 = 1000
val_2 = val_1  # val_1 oraz val_2 pokazuja na ten sam obiekt w pamieci
print(f'ID OF val_1 = {id(val_1)}')
print(f'ID OF val_2 = {id(val_2)}')
val_1 = 2000  # val_1 od teraz pokazuje na inny obiekt w pamieci
print(f'ID OF val_1 = {id(val_1)}')
print(f'ID OF val_2 = {id(val_2)}')

# w przypadku typow mutable jest inaczej
numbers_1 = [10, 20, 30]
print(f'ID OF LIST 1 = {id(numbers_1)}')
numbers_1 += [40]
print(f'ID OF LIST 1 = {id(numbers_1)}')
numbers_2 = [10, 20, 30]
print(f'ID OF LIST 2 = {id(numbers_2)}')
numbers_3 = [10, 20, 30]
print(f'ID OF LIST 3 = {id(numbers_3)}')

xx_1 = 257
xx_2 = 257
print(xx_1 is xx_2)

# <-5, 256>



