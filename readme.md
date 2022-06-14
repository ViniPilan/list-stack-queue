```python
from ed_implementation import *
```

## Dinamic List, Queue and Stack implementation

All code is stored in *ed_implementation.py*.


### List example

The list functions avaible are:
- find
- insert_begin
- insert_final
- pop
- remove
- remove_all
- size
- visualize


```python
list_example = List()

for element in ['ab', 'bc', 'db', 'ee']:
    list_example.insert_begin(element)
    
    
for element in [1, 3, 4, 5]:
    list_example.insert_final(element)
    
print('\n\nList elements:')
list_example.visualize()
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
print('Poped item: ', list_example.pop(2))

print('\nee: ')
list_example.remove('ee')

print('\n\nList elements:')
list_example.visualize()

print('\nSize: ', list_example.size())
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

The stack functions avaible are:
- push
- pop
- size


```python
stack_example = Stack()

for element in ['ab', 'bc', 'db', 'ee']:
    stack_example.push(element)
    
for i in range(0, stack_example.size()):
    print(f'{i}: ', stack_example.pop())
```

    0:  ee
    1:  db
    2:  bc
    3:  ab
    

### Queue example

The queue functions avaible are:
- push
- pop
- size


```python
queue_example = Queue()

for element in ['ab', 'bc', 'db', 'ee']:
    queue_example.push(element)
    
for i in range(0, queue_example.size()):
    print(f'{i}: ', queue_example.pop())
```

    0:  ab
    1:  bc
    2:  db
    3:  ee
    

### About the autor

Hello!! My name is Vinícius Pilan and I am a computer science student at UNESP, a university in the State of São Paulo, Brazil, and a data science lover. 


Thanks for your view! Please contact me if you want by sending a message to vinipilan@gmail.com. More information about me can be accessed at: https://sites.google.com/view/vinicius-pilan/


```python

```
