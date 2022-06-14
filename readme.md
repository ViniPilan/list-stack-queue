```python
from ed_implementation import *
```

### List example


```python
lista = List()

for element in ['ab', 'bc', 'db', 'ee']:
    lista.insert_begin(element)
    
    
for element in [1, 3, 4, 5]:
    lista.insert_final(element)
    
print('\n\nList elements:')
lista.visualize()
```

    
    
    List elements:
    ee
    db
    bc
    ab
    1
    3
    4
    5
    


```python
print('Poped item: ', lista.pop(2))

print('\nee: ')
lista.remove('ee')

print('\n\nList elements:')
lista.visualize()

print('\nSize: ', lista.size())
```

    Poped item:  bc
    
    ee: 
    The element was removed!
    
    
    List elements:
    db
    ab
    1
    3
    4
    5
    
    Size:  6
    

### Stack example


```python
pilha = Stack()

for element in ['ab', 'bc', 'db', 'ee']:
    pilha.push(element)
    
for i in range(0, pilha.size()):
    print(f'{i}: ', pilha.pop())
```

    0:  ee
    1:  db
    2:  bc
    3:  ab
    

### Queue example


```python
fila = Queue()

for element in ['ab', 'bc', 'db', 'ee']:
    fila.push(element)
    
for i in range(0, fila.size()):
    print(f'{i}: ', fila.pop())
```

    0:  ab
    1:  bc
    2:  db
    3:  ee
    
