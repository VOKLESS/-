# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44 #объем памяти дискеты в Мб
sheets = 100
lines = 50
symbols = 25
v_symbol = 4 #объем одного символа в байтах

#Размер одной книги
v_symbol_mb = (v_symbol / 1024) / 1024
book = v_symbol_mb * symbols * lines * sheets

itog = disk // book
int_itog = int(itog)

print("Количество книг, помещающихся на дискету:", int_itog)