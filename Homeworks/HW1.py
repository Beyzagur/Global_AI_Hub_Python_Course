# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11E8DW1ZzWdYCm1gOZaH0qd4t-7DxhVNl
"""

import random

def isPrime(number):
  for i in range(2,number):
    if (number % i)==0:
      n=random.randint(2,100)
      return isPrime(n)
    
  return number

matrix = [[0 for x in range(3)] for y in range(3)]

for i in range(3):
  for j in range(3):
    n=random.randint(2,100)
    matrix[i][j]=isPrime(n)

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    print(matrix[i][j],end=' ')
  print()