Lecture 5
Regex
------------------------------------------------
Чаще всего регулярные выражения используются для:
поиска в строке;
разбиения строки на подстроки;
замены части строки.
------------------------------------------------
import re
re.match(pattern, string)
result = re.match("test", "test programming technologies")
result.group(0)
result.start()
result.end()
result = re.match(r"test", "test programming technologies")
result = re.match(r'programming', 'test programming technologies')
------------------------------------------------
Метод search() ищет по всей строке, но возвращает только первое найденное совпадение
re.search(pattern, string)
result = re.match(r'programming', 'test programming technologies')
------------------------------------------------
re.split(pattern, string, [maxsplit=0])
result = re.split(",","1,2,3,4,5")
------------------------------------------------
re.sub(pattern, repl, string)
result = re.split(",", " ", "1,2,3,4,5")
------------------------------------------------
re.compile(pattern, repl, string)
pattern = re.compile("test")
pattern.findall("hi test hi test")
pattern.findall("hi test")
------------------------------------------------
.	    -- Один любой символ, кроме новой строки \n
?	    -- 0 или 1 вхождение шаблона слева
+	    -- 1 и более вхождений шаблона слева
*	    -- 0 и более вхождений шаблона слева
\w	  -- Любая буква (то, что может быть частью слова), а также цифры и _
\W	  -- Любая не-буква, не-цифра и не подчёркивание
\d    -- Любая цифра (ab\d\d - ab34, ab56)
\D    -- Любой символ, кроме цифры
\s	  -- Любой пробельный символ (пробел, табуляция, конец строки и т.п.),  \S -- Любой непробельный символ
\b	  -- Граница слова
[..]	-- Один из символов в скобках, а также любой символ из диапазона a-b	[0-9][0-9A-Fa-f]
[^..]	-- Любой символ, кроме перечисленных
^ и $	-- Начало и конец строки соответственно
{n,m}	-- От n до m вхождений ({,m} — от 0 до m)
a|b	  -- Соответствует a или b
\t, \n -- Символ табуляции и новой строки соответственно

Задача 1: Вернуть первое слово из строки
* Сначала попробуем вытащить каждый символ (используя .)
result = re.findall(r'.', 'test programming technologies test')

* Для того, чтобы в конечный результат не попал пробел, используем вместо . \w.
result = re.findall(r'\w', 'test programming technologies test')

* Теперь попробуем достать каждое слово (используя * или +)
result = re.findall(r'\w*', 'test programming technologies test')
result = re.findall(r'\w+', 'test programming technologies test')

* Теперь вытащим первое слово, используя ^:
result = re.findall(r'^\w+', 'test programming technologies test')

* Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:
result = re.findall(r'\w+$', 'test programming technologies test1')
------------------------------------------------
Задача 2: Вернуть первые два символа каждого слова
* Вариант 1: используя \w, вытащить два последовательных символа, кроме пробельных, из каждого слова:
result = re.findall(r'\w\w', 'hello world programming technologies')

* Вариант 2: вытащить два последовательных символа, используя символ границы слова (\b):
result = re.findall(r'\b\w\w', 'hello world programming technologies')
------------------------------------------------
Задача 3: вернуть список доменов из списка адресов электронной почты
abc.test@gmail.com, xyz@mail.ru, a.akshabayev@kbtu.kz

* Сначала вернем все символы после «@»
re.findall(r'@\w+', 'abc.test@gmail.com, xyz@mail.ru, a.akshabayev@kbtu.kz')

* части «.com», «.in» и т. д. не попали в результат. Изменим наш код:
re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@mail.ru, a.akshabayev@kbtu.kz')

* Второй вариант — вытащить только домен верхнего уровня, используя группировку — ():
re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@mail.ru, a.akshabayev@kbtu.kz')
------------------------------------------------
Задача 4: Извлечь дату из строки
* Используем \d для извлечения цифр.
result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')

* вывести только год (месяц, день)
result = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
------------------------------------------------
Задача 5: Извлечь все слова, начинающиеся на гласную (aeiouAEIOU)
* Найдем все слова
result = re.findall(r'\w+', 'abc tatt eia a bobb')

* А теперь — только те, которые начинаются на определенные буквы
result = re.findall(r'[aeiouAEIOU]\w+', "abc tatt eia a bobb")

* Выше мы видим обрезанные слова, Для того, чтобы убрать их, используем \b для обозначения границы слова
result = re.findall(r'\b[aeiouAEIOU]\w+', "abc tatt eia a bobb")

* Также мы можем использовать ^ внутри квадратных скобок для инвертирования группы:
result = re.findall(r'\b[^aeiouAEIOU]\w+', "abc tatt eia a bobb")

* В результат попали слова, «начинающиеся» с пробела. Уберем их, включив пробел в диапазон в квадратных скобках:
result = re.findall(r'\b[^aeiouAEIOU ]\w+', "abc tatt eia a bobb")
------------------------------------------------
* Задача 6: Проверить телефонный номер 
text = '+7-777-5673443, +7-772-2344343 abc'
result = re.findall(r'\+7-[0-9]{3}-[0-9]{5}', text)
------------------------------------------------
Задача 7: Разбить строку по нескольким разделителям
line = 'asdf fjdk;afed,fjek,asdf,foo'
# String has multiple delimiters (";",","," ").

result = re.split(r'[;, ]', line)

Также мы можем использовать метод re.sub() для замены всех разделителей пробелами:
result = re.sub(r'[;, ]', ' ', line)
------------------------------------------------
simple text ---	В точности текст «simple text»

\d{5}	--- Последовательности из 5 цифр, \d --- означает любую цифру {5} — ровно 5 раз
\d\d/\d\d/\d{4}	--- Даты в формате ДД/ММ/ГГГГ (и прочие куски, на них похожие, например 98/76/5432)
\b\w{3}\b	--- Слова в точности из трёх букв \b означает границу слова \w — любая буква, {3} — ровно три раза
[-+]?\d+ ---	Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули) [-+]? — либо -, либо +, либо пусто \d+ — последовательность из 1 или более цифр
-------------------------------------
^ - Caret
^a	a	1 match
    abc	1 match
    bac	No match
^ab	abc	1 match
    acb	No match (starts with a but not followed by b)
-----------------------------
$ - Dollar
a$	a	1 match
    formula	1 match
    cab	No match
-----------------------------
ma*n	mn	1 match
      man	1 match
      maaan	1 match
      main	No match (a is not followed by n)
      woman	1 match
-----------------------------
\b - Matches if the specified characters are at the beginning or end of a word.

\bfoo	football	Match
      a football	Match
      afootball	No match

foo\b	the foo	Match
      the afoo test	Match
      the afootest	No match
-----------------------------

{n}	Ровно n повторений
{m,n}	От m до n повторений включительно
{m,}	Не менее m повторений
{,n}	Не более n повторений
?	Ноль или одно вхождение, синоним {0,1}
*	Ноль или более, синоним {0,}
+	Одно или более, синоним {1,}

re.fullmatch(pattern, string) --	Проверить, подходит ли строка string под шаблон pattern;

re.finditer(pattern, string)	Итератор всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты);
--------------------------------
Вывести все числа в строке
import re
string = 'hello 12 hi 89. Test 34'
pattern = '\d+'
result = re.findall(pattern, string) 
print(result)
--------------------------------
import re 

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') 

match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 
print(match[0] if match else 'Not found') 


match = re.fullmatch(r'\d\d\D\d\d', r'12-12') 
print('YES' if match else 'NO') 

match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12') 
print('YES' if match else 'NO') 


print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 


print(re.findall(r'\d\d\.\d\d\.\d{4}', r'test 19.01.2018, test 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Дата рождения 13.02.1920, сегодня 08.02.2020'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 
------------------------------
Пример с чеком (raw.txt):
------------------------------
pattern = r"(Порядковый номер чека)(.*)"

f = open('row.txt', 'r')
text = f.read()

print(re.search(pattern, text).group())
# print(re.search(pattern, text).group(2))
------------------------------
pattern = r"(Стоимость)\n{1}(.*)"
------------------------------
pattern = r"\n{1}(?P<raw_count>.*)\n{1}(?P<price>.*)\n{1}(Стоимость)\n{1}(?P<price2>.*)"
------------------------------------------------------------
