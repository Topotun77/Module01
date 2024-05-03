grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
stud_list = list(sorted(students))
student_dic = {}

grades_set = list(map(lambda x : list(map(int, x.split())), grades))
#print(grades_set)

student_dic = dict(map(lambda x, y : (x, sum(y)/len(y)), stud_list, grades_set))
print(student_dic)