# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:14:15 2019

@author: Aditya
"""

class Person:
    department = 'School of Information Technology'
    
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('aditya tewari')
person.set_location('india')
print( '{} lives in {} and works in the department of {}'.format(person.name, person.location,person.department))

store1 = {10.00, 11.00, 12.34, 2.34}
store2 = {9.00, 11.10, 12.34, 2.01}
cheapest = map(min, store1, store2)
cheapest

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)
list(map(split_title_and_name, people))

#lambda
my_func = lambda a,b,c : a + b
my_func(1, 2, 3)

#list comprehensions
my_list = [number for number in range(0,1000) if number % 2 ==0]
my_list
