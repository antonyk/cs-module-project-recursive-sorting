a=3
b='123'
print(a*b)

list_1 = [1,2,4]
list_2 = [1,3,5]

# combined = list(set(list_1.extend(list_2)))
# print(combined)

list_12 = [1,2,4]
list_22 = [1,3,5]
list_12.extend(list_22)
combined2 = list(set(list_12))
print(combined2)

class Parent(object):
  def fun(self):
    print('Hi')

class Child(Parent):
  def fun(self):
    print('Bye')

c = Child()
c.fun()