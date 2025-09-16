import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


study_time = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
grade = np.array([2, 4, 5, 4, 5])

reg = LinearRegression()
reg.fit(study_time, grade)  # linear regression formual
predict_values = reg.predict(study_time)

print(f'B1 : {reg.coef_} B0 : {reg.intercept_}')
print(f'R^2 : {reg.score(study_time ,grade)}')
print(f' Predict Values : {predict_values} ')


if __name__ == "__main__":
    plt.title("Relation between Study Time & Grade")
    plt.xlabel("Study Time")
    plt.ylabel("Grade (predict-value)")
    plt.scatter(study_time, grade, color='blue', label='Natural Data')
    plt.plot(study_time, predict_values, color='red', label='Predict Data')
    plt.legend()
    plt.show()
