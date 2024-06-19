# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать
# вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие даннные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом
# будет имя ученика, а значением - его средний балл.

grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}

#student_dic = {}
#stud_list = list(sorted(students))
#grades_set = list(map(lambda x : list(map(int, x.split())), grades))
#student_dic = dict(map(lambda x, y : (x, sum(y)/len(y)), stud_list, grades_set))

# ========== Вариант №1 ============

student_dic = dict(map(lambda x, y: (x, sum(list(map(int, y.split())))/len(list(map(int, y.split())))),
                       list(sorted(students)), grades))
print(student_dic)

# ========== Вариант №2 ============

grades_set = list(map(lambda x: sum(list(map(int, x.split())))/len(list(map(int, x.split()))), grades))
student_dic2 = dict(zip(list(sorted(students)), grades_set))

print(student_dic2)

# ========== Вариант №3 ============

student_dic3 = dict(zip(list(sorted(students)), grades_set))

print(student_dic3)