# TODO Найдите количество книг, которое можно разместить на дискете
quantity_page = 100 #количество страниц
quantity_symbol = 25 #количество символов
quantity_line = 50 #количество строк
volume_symbol = 4 #объем символа
volume_disk = 1.44 * 1024 * 1024
volume_book = quantity_line * quantity_page * quantity_symbol * volume_symbol
quantity_books = volume_disk / volume_book
print("Количество книг, помещающихся на дискету:", round(quantity_books))