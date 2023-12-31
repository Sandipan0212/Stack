# -*- coding: utf-8 -*-
"""stack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3O0-TiEo31wbuA6LeiwSZZHus9Ql2IR
"""

### for stack implementation
# push
#pop
#top
#size
#isEmpty

class stack():

  def __init__(self):
    self.__data = []

  def push(self,item):
    self.__data.append(item)

  def pop(self):
    if self.isEmpty():
      return
    return self.__data.pop()

  def top(self):
    if self.isEmpty():
      return
    return self.__data[len(self.__data)-1]

  def size(self):
    return len(self.__data)

  def isEmpty(self):
    return self.size() == 0

s = stack()
s.push(13)
s.push(14)
s.push(15)

while s.isEmpty() == False:
  print(s.pop())

class Node():
  def __init__(self,data):
    self.data = data
    self.next = None

class stackLL():

  def __init__(self):
    self.__head = None
    self.__count = 0

  def push(self,element):
    newnode = Node(element)
    newnode.next = self.__head
    self.__head = newnode
    self.__count = self.__count + 1

  def pop(self):
    if self.isEmpty() is True:
      print("empty")
      return
    data = self.__head.data
    self.__head = self.__head.next
    self.__count = self.__count - 1
    return data

  def top(self):
    if self.isEmpty() is True:
      print("empty")
      return
    return self.__head.data

  def size(self):
    return self.__count

  def isEmpty(self):
    return self.size() == 0

S = stackLL()
S.push(10)
S.push(11)
S.push(12)

while S.isEmpty() is False:
  print(S.pop())

S.top()