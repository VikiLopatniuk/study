# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?" \
"That depends a good deal on where you want to get to," said the Cat. \
"I don\'t much care where ——" said Alice. \
"Then it doesn\'t matter which way you go," said the Cat. \
"—— so long as I get somewhere," Alice added as an explanation. \
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_scuare = 436402
azov_sea_square = 37800
total_seas_squares = black_sea_scuare + azov_sea_square
print(total_seas_squares)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_stocks = 3
total_products = 375291
products_first_second_stocks = 250449
products_second_third_stocks = 222950
first_stock = total_products - products_second_third_stocks
second_stock = products_first_second_stocks - first_stock
third_stock = total_products - products_first_second_stocks
print(first_stock, second_stock, third_stock)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_month_payment = 1179
total_monthes = 18
total_pc_price = one_month_payment * total_monthes
print(total_pc_price)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(a, b, c, d, e, f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274 * 4
medium_pizza = 218 * 2
juice = 35 * 4
cake = 350
water = 21 * 3
total_price = big_pizza + medium_pizza + juice + cake + water
print(total_price)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
one_page = 8
total_pages = total_photos / one_page
print(total_pages)    
# враховуючи ваші зауваження щодо уількості сторінок хочу наголосити що в умові задачі йдеться 
# про сторінки, а не про аркуши. Кожен аркуш має 2 сторінки, тому з математичної точки зору
# раіняння виконане правильно. Якщо говорити про кількість аркушів - то їх буде 30.

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_route = 1600
fuel_every_100_km = 9
possible_fuel_tank = 48
needed_fuel = ( total_route * fuel_every_100_km ) / 100
stops = needed_fuel / possible_fuel_tank
print(needed_fuel, stops)