import numpy as np
import matplotlib.pyplot as plt


# Data
study_time = np.array([1, 2, 3, 4, 5])
grade = np.array([2, 4, 5, 4, 5])

# Average
study_time_avg = sum(study_time) / len(study_time)
grade_avg = sum(grade) / len(grade)

sumation = 0
square_x_sumation = 0

for i in range(len(study_time)):
    # (xi- average_x)^2
    square_x_sumation += pow((study_time[i] - study_time_avg), 2)
    # (xi - average_x) * (yi - average_y)
    sumation += (study_time[i] - study_time_avg) * (grade[i] - grade_avg)

# calculate B0 and B1
B_1 = sumation/square_x_sumation
B_0 = grade_avg - (B_1*(study_time_avg))


# calculate predict values
def calculate_predict(x):
    predict_values = []
    for i in range(len(x)):
        regression_formula = B_0 + B_1*(x[i])
        predict_values.append(float(regression_formula))
    return predict_values


predict_values = calculate_predict(study_time)

# calculate residual values
residual_list = []
for i in range(len(predict_values)):
    residual = grade[i] - predict_values[i]
    residual_list.append(float(residual))


# SST = SSR + SSE
SSE = 0
SSR = 0
for i in range(len(grade)):
    SSE += pow((grade[i] - predict_values[i]), 2)
    SSR += pow((predict_values[i] - grade_avg), 2)

SST = SSR + SSE
R2 = (SSR / SST)

MSE = SSE / len(grade)
MSR = SSR / (2-1)  # p-1 p-> len parametrs B0 and B1
F = MSR / MSE


# print data
print(f'B1 : {B_1} & B0 : {B_0}')
print(f'Study Time {study_time} Grade {grade}')
print(f'Study Time {study_time} Predict values {predict_values}')
print(f'Resdiual values {residual_list}')
print(
    f'SST : {SST} \nR^2 : {R2} , \nMSE : {MSE} \nMSR : {MSR} \nF(MSR/MSE) : {F} ')


if __name__ == '__main__':
    # Show Result
    plt.title("Relation between Study Time & Grade")
    plt.xlabel("Study Time")
    plt.ylabel("Grade | (Predict-value)")
    plt.plot(study_time, grade, 'o')

    plt.plot(study_time, predict_values)
    plt.show()
