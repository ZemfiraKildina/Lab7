from itertools import chain
def unpack(n):
    r = []
    q = [n] # "очередь" для хранения информации
    while len(q) > 0: # пока в списке q есть хоть что то
        n = q[-1] # последний элемент их q и сохраняем его в n
        del q[-1] # удаляем из q
        match type(n).__name__:#определяем тип элемента
            case 'list' | 'tuple' | 'set':
                q.extend(n) # добавляем в q
            case 'dict': #все ключи и значения добавляем в q
                q.extend(list(n.keys()))
                q.extend(list(n.values()))
            case _:
                r.append(n)
    print(n)
    return r[::-1] # последний пришел 1

print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))