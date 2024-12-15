# Лабораторная №7
## Описание проделанной работы
### Задание 1
#### Условие
Условие Функция для распаковки списка, содержащего другие объекты (`int`, `str`, `list`, `tuple`, `dict`, `set`) произвольной вложенности.
#### Решение:
* С рекурсией
```python
from itertools import chain #обьединяет несколько обьектов в один
def unpack(x):
    def f(z):
        if type(z)==list:
            return list(chain.from_iterable([f(i) for i in z])) #обьединение в один список
        return [z] # оборачиваем в список
    match type(x).__name__: #если список кортедж или множество то делаем из этого список
        case 'list' | 'tuple' | 'set': #объединить несколько литералов в один шаблон с помощью | («или»):
            return f([unpack(i) for i in x])
        case 'dict': #для словаря
            return [[unpack(i), unpack(x[i])] for i in x.keys()] #создается список списков(для ключа и его значения и затем распаковываем)
        case _: #если ничему не соответсвует
            return x

print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))
```
- Результат

<image src = 1_withRec.png alt="результат программы">

* Без Рекурсии
```python
from itertools import chain
def unpack(n):
    r = []
    q = [n] # очередь для хранения информации
    while len(q) > 0: # пока в списке q есть хоть что то
        n = q[-1] # последний элемент их q и сохраняем его в n
        del q[-1] # удаляем из q
        match type(n).__name__:#определяем тип элемента
            case 'list' | 'tuple' | 'set': q.extend(n) # добавляем в q
            case 'dict': #все ключи и значения добавляем в q
                q.extend(list(n.keys()))
                q.extend(list(n.values()))
            case _: r.append(n)
    return r[::-1] # последний пришел 1

print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))
```
- Результат

<image src = 1_outRec.png alt="результат программы">

### Задание 2
#### Условие
<image src = task.png alt="результат программы">

#### Решение:
* С рекурсией
```python
def w(i):
    if i ==1:
        return 0.3
    if i ==2:
        return -1.5
    return w(i-1)*w(i-2)*(i-2)**2/(i+1)**3

for i in range(1,100):
    print(w(i))
```
- Результат

<image src = 2_withRec.png alt="результат программы">

* Без рекурсии
```python
def w(i):
    if i == 1: return 0.3
    if i == 2: return -1.5
    p = -1.5
    pp = 0.3
    for i in range(3, i+1):
        t = p*pp*(i-2)**2/(i+1)**3
        pp = p
        p = t
    return p

for i in range(1, 10):
    print(w(i))
```
- Результат

<image src = 2_outRec.png alt="результат программы">


## Ссылки на используемые ресурсы
* [Лабораторная №7](https://evil-teacher.on.fleek.co/prog_pm/term1/lab07/)
* [Recursion in Programming - Full Course - freeCodeCamp.org](https://youtu.be/IJDJ0kBx2LM)
* [Самоучитель по Python для начинающих. Часть 13: Рекурсивные функции - proglib.io](https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23)
* [Как работает рекурсия – объяснение в блок-схемах и видео - Хабр](https://habr.com/ru/articles/337030/)

