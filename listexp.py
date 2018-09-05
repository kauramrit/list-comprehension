#Q.1- Write a python program to print the cube of each value of a list using list comprehension.

list=[1,2,3,4]
l=[i**3 for i in list]
print("cube of no:",l)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.

q=[i for i in range(2,20) if 0 not in [i%j for j in range(2,i)]]
print("prime no:",q)

#Q.3- Write the main differences between List Comprehension and Generator Expression.

LIST COMPREHENSION:  
It is an elegant way of defining and creating a list. List Comprehension allows us to create a list using for loop with lesser code.
GENERATOR EXPRESSION:
Generator Expressions are somewhat similar to list comprehensions, but the former doesn’t construct list object.
Instead of creating a list and keeping the whole sequence in the memory, the generator generates the next element in demand.

The generator yields one item at a time and generates item only when in demand.
Whereas, in a list comprehension, Python reserves memory for the whole list.
Thus we can say that the generator expressions are memory efficient than the lists.

#Q.4- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.

Celsius = [39.2, 36.5, 37.3, 37.8] 
q=list(map(lambda x:x-32*(5/9),Celsius))
print(q)

#Q.5- Apply an anonymous function to square all the elements of a list using map and lambda.

l=[3,7,2,6]
q=list(map(lambda x:x**2,l))
print(q)

#Q.6- Filter out all the primes from a list.

num=[1,2,3,4,5,6,7,8,9] 
for i in range(2,9): 
     num=list(filter(lambda x: x == i or x % i, num))
print(num)

#Q.7- Write a python program to multiply all the elements of a list using reduce.

from functools import *
l=[1,2,3,4]
r=reduce(lambda x,y:x*y,l)
print(r)

