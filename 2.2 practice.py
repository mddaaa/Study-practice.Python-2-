class students:
    def __init__(self,name,age,group,evaluations):
        self.name = name
        self.age = age
        self.group = group
        self.evaluations = evaluations

    def display_info(self):
        print(f"Name: {self.name}")
    # def display_info(self):
    #     print(f"Name:{} Age: {}Group: {}Evaluations:{}")


students = [("Alexander", '07-05-2006' ,643,[4,5,3,4,3,5]),
("Artur", '20-12-2005' , 645 , [4,5,3,4,3,5]),
("Denis", '15-05-2001' , 644 ,[4,5,3,4,3,5])
]
# print(Alexander.name)
# print(Alexander.age)
# print(Alexander.group)
# print(Alexander.evaluations)

# inpt = 1
# while inpt != 'stop':
#     print('ведите 0 чтобы завершить:')
#     inpt = input('введите имя которое хотите изменить: ')
print(students.name)
