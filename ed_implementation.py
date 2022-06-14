
""" 

Dinamic List, Queue and Stack implementation

 """


class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        
        
class List:

    def __init__(self):
        self.__head = ListNode()

    def insert_begin(self, element) -> None:
        """ Recieves a header list and a element, so insert the element in the begin of this list. """
        
        if self.__head.next is None:
            self.__head.next = ListNode(element)
            
        else:
            no = ListNode(element, self.__head.next)
            self.__head.next = no
            
            
    def insert_final(self, element) -> None:
        """ Recieves a header list and a element, so insert the element in the final of this list. """
        
        if self.__head.next is None:
            self.__head.next = ListNode(element)
            
        else:
            no = self.__head.next
            
            while no.next is not None:
                no = no.next
                
            no.next = ListNode(element)
            
            
    def visualize(self) -> None:
        """ Recieves a header list and show all elements of this list. """
        
        if self.__head.next is None:
            print('Empty list...')
            
        else:
            no = self.__head.next
            
            while no is not None:
                print(no.val)
                no = no.next
        
        
    def find(self, element) -> bool:
        """ Recieves a header list and a element, so try to find this element in list. Return the Node Adress if found, else False. """
        
        if self.__head.next is None:
            print('Empty list...')
            return False
            
        else:
            no = self.__head.next
            
            while no is not None:
                if no.val == element:
                    return no
                
                no = no.next
                    
            return False
        
        
    def remove(self, element) -> bool:
        """ Recieves a header list and a element, so try to find this element in list and remove him (just in the first element 
        appears. Return True if the remove was done else False. """
        
        if self.__head.next is None:
            print('Empty list...')
            return False
            
        else:
            no_0 = self.__head.next
            no_1 = no_0
            
            if no_1.val == element:
                self.__head.next = no_1.next
                print('The element was removed!')
                return True
            
            no_1 = no_1.next
            
            while no_1 is not None:
                if no_1.val == element:
                    no_0.next = no_1.next
                    print('The element was removed!')
                    return True
                
                no_1 = no_1.next
                no_0 = no_0.next
                
            print('The element is not in the list...')
            return False
        
    
    def pop(self, element_pos:int) -> int:
        """ Drops (remove and return) element with the given position. """
        i = 0
        
        if self.__head.next is None:
            return None
            
        if element_pos+1 > self.size():
            return None
        
        else:
            no_0 = self.__head.next
            no_1 = no_0
            
            if element_pos == 0:
                self.__head.next = no_1.next
                return no_1.val
            
            no_1 = no_1.next
            
            while no_1 is not None:
                i+=1
                if i == element_pos:
                    no_0.next = no_1.next
                    return no_1.val
                
                no_1 = no_1.next
                no_0 = no_0.next
                
            return None
        
        
    def remove_all(self, element) -> None:
        """ Recieves a header list and a element, so try to find this element in list and remove him (for all element 
        appears. Return True for each element removed and return False if the element had not found. """

        flag = True
        
        while flag:
            flag = self.remove(head, element)
            
    
    def size(self) -> int:
        """ Recieves a header list and return the lenght of the list. """
        
        if self.__head.next is None:
            return 0
        
        else:
            no = self.__head.next
            count = 0
            while no is not None:
                count += 1
                no = no.next
            
            return count



class Stack:
    def __init__(self):
        self.__stack = List()
    
    def push(self, element):
        """ Insert a element into the stack. """
        self.__stack.insert_final(element)
        
    def pop(self):
        """ Pop a element from the stack. """
        n = self.size()
        return self.__stack.pop(n-1)
        
    def size(self):
        """ Return the stack size. """
        return self.__stack.size()

    
class Queue:
    def __init__(self):
        self.__queue = List()
    
    def push(self, element):
        """ Insert a element into the queue. """
        self.__queue.insert_final(element)
        
    def pop(self):
        """ Pop a element from the queue. """
        n = self.size()
        return self.__queue.pop(0)
        
    def size(self):
        """ Return the queue size. """
        return self.__queue.size()