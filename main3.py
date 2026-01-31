import matplotlib.pyplot as plt

students_name = ['sam','phil','samanthan','alex','john','elena','stefan','julie']
students_marks = [35,40,25,42,30,28,20,49]

marks_perc = []

for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("Students' marks Graph")
    plt.xlabel("Students' Names")
    plt.ylabel("Students' Marks")
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("Students' Percentage Graph")
    plt.xlabel("Students' Names")
    plt.ylabel("Students' Percentage")
    plt.show()

percentage_bar_chart()