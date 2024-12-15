from itertools import chain #обьединяет несколько обьектов в один
def unpack(x):
    def f(z):
        if type(z)==list:
            return list(chain.from_iterable([f(i) for i in z])) #обьединение в один список
        return [z] # оборачиваем в список
    match type(x).__name__:
        #если список кортедж или множество то делаем из этого список
        case 'list' | 'tuple' | 'set': #объединить несколько литералов в один шаблон с помощью | («или»):
            return f([unpack(i) for i in x])
        case 'dict': #для словаря
            return [[unpack(i), unpack(x[i])] for i in x.keys()] #осздается список списков(для ключа и его значения и затем распаковываем)
        case _: #если ничему не соответсвует
            return x

print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))