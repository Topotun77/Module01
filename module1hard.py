grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
stud_list = list(sorted(students))
#print(stud_list)
student_dic = {}
for i_stud in range(len(students)):
    grade = grades[i_stud].split()
    sum=0
    for i_grad in range(len(grade)):
        sum += int(grade[i_grad])
    #print(i_stud, grade, sum/len(grade))
    student_dic[stud_list[i_stud]] = sum/len(grade)
print(student_dic)