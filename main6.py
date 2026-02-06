import matplotlib.pyplot as plt

name = ['alex','james','sam','june','dave','ben']
weight = [52,36,45,37,51,58]
height = [159,128,149,130,163,158]

bmi = []

for i in weight,height:
    BMI = (weight/height)
    bmi.append(BMI)

def bmi_line_chart():
    plt.plot(name,weight)
    plt.title("People's weight chart")
    plt.xlabel("People's names")
    plt.ylabel("People's weight")

def bmi_line_chart():
    plt.plot(name,height)
    plt.title("People's height chart")
    plt.xlabel("People's names")
    plt.ylabel("People's height")

def bmi_line_chart():
    plt.plot(name,bmi)
    plt.title("People's BMI chart")
    plt.xlabel("People's names")
    plt.ylabel("People's BMI")

bmi_line_chart()