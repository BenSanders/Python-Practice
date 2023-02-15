from collections import namedtuple

Car = namedtuple('Car',['make','model','price','horsepower','seats'])

car1 = Car('Ford','F150',30000,'1,000','2')
car2 = Car('Kia','Sadona',25000,'1,000','4')

print(car1.price + car2.price)