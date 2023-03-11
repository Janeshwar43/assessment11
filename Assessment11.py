#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Problem 1: Stack
#Implement a stack data structure in Python. The stack should support the following operations:
#push(item) - Add an item to the top of the stack.
#pop() - Remove and return the item on the top of the stack.
#peek() - Return the item on the top of the stack without removing it.
#is_empty() - Return True if the stack is empty, else False.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# In[5]:


#Problem 2: Queue
#Implement a queue data structure in Python. The queue should support the following operations:
#enqueue(item) - Add an item to the back of the queue.
#dequeue() - Remove and return the item at the front of the queue.
#peek() - Return the item at the front of the queue without removing it.
#is_empty() - Return True if the queue is empty, else False.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


# In[ ]:


#Problem 3: Binary Search Tree
#Implement a binary search tree (BST) data structure in Python. The BST should support the following operations:
#insert(item) - Insert an item into the tree.
#delete(item) - Remove an item from the tree.
#search(item) - Return True if the item is in the tree, else False.
#size() - Return the number of nodes in the tree.
#class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
                self.size += 1
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
                self.size += 1
            else:
                self._insert(value, current_node.right)
        else:
            
            pass

    def delete(self, value):
        if self.root is not None:
            self.root, removed = self._delete(value, self.root)
            if removed:
                self.size -= 1

    def _delete(self, value, current_node):
        if current_node is None:
            return current_node, False
        elif value < current_node.value:
            current_node.left, removed = self._delete(value, current_node.left)
            return current_node, removed
        elif value > current_node.value:
            current_node.right, removed = self._delete(value, current_node.right)
            return current_node, removed
        else:
            if current_node.left is None and current_node.right is None:
                return None, True
            elif current_node.left is None:
                return current_node.right, True
            elif current_node.right is None:
                return current_node.left, True
            else:
                successor = self._find_min(current_node.right)
                current_node.value = successor.value
                current_node.right, removed = self._delete(successor.value, current_node.right)
                return current_node, removed

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def size(self):
        return self.size

    def _find_min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


# In[6]:


#Problem 1: Anagram Checker
##Write a Python function that takes in two strings and returns True if they are anagrams of each other, else False. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#def is_anagram(s1, s2):

    # Convert strings to lowercase and remove whitespaces
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')
    if len(s1) != len(s2):
        return False

    
    dict_s1 = {}
    dict_s2 = {}

   
    for letter in s1:
        if letter in dict_s1:
            dict_s1[letter] += 1
        else:
            dict_s1[letter] = 1

    # Count letters in the second string and store in dictionary
    for letter in s2:
        if letter in dict_s2:
            dict_s2[letter] += 1
        else:
            dict_s2[letter] = 1

    # Compare the dictionaries to check if they are equal
    if dict_s1 == dict_s2:
        return True
    else:
        return False


# In[ ]:


#Problem 2: FizzBuzz
#Write a Python function that takes in an integer n and prints the numbers from 1 to n. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz" instead of the number. For multiples of both 3 and 5, print "FizzBuzz" instead of the number.
#def fizz_buzz(num):

    if num%3==0 and num%5==0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    else:
        return num

for n in range(1,100):
    print(fizz_buzz(n))


# In[17]:


#Problem 3: Fibonacci Sequence
#Write a Python function that takes in an integer n and returns the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number after the first two is the sum of the two preceding ones.

def fibonacci(n):
   
    if n <= 1:
        return n
   
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# In[ ]:




