from main import calculate_predict

study_time = []
new_data = float(input("Enter New Study Time : \n"))
study_time.append(new_data)
predict_grade = calculate_predict(study_time)
print(predict_grade)