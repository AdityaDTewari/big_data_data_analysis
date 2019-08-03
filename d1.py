def myfunc(a, b, z=None):
    if(z==None):
        return a+b
    else:
        return b+a+z
print(myfunc(1, 2, 3))

x=(1, 'a', 2, 'b')
type(x)
x

x=[1, 'a', 2, 'b']
type(x)
x
x.append(3.3)

for item in x:
    print(item)

i=0
while( i != len(x) ):
    print(x[i])
    i=i+1

[1, 2] + [3, 4]
[1,2]*3

1 in [1, 2, 3]

x = 'this is a string'
print(x[0])
print(x[0:1])
print(x[0:2])
print(x[-1])
print(x[-4:-2])
print(x[3:])
print(x[:5])

firstname = 'aditya'
lastname = 'tewari'
print('aditya' in firstname)

firstname = 'aditya dev tewari'.split(' ')[0]
lastname = 'aditya dev tewari'.split(' ')[-1]
print(firstname)
print(lastname)

x={'first': 'thisisthefirst', 'second': 'thisisthesecond'}
x['first']
x['third']= None
for name in x:
    print(x[name])
for em in x.values():
    print(em)
for name,em in x.items():
    print(name)
    print(em)

x = ('aditya', 'dev', 'tewari')
fn, mn, ln = x
print(fn)
print(ln)
print(mn)

sales_rec = {'price':3.24, 'num_items':4, 'person': 'aditya'}
sales_stat = '{} brought {} item(s) at a price of {} each for a total of {}'
print(sales_stat.format(sales_rec['person'],sales_rec['num_items'],sales_rec['price'], sales_rec['num_items']*sales_rec['price']))