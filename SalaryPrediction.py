name = input('Enter your name : ')
import joblib
num = float(input('Enter year of experience : '))
model = joblib.load('SalaryPrediction.pk1')
print()
print('Name               : ' ,name)
print('Year_of_Experience : ', num)
output = model.predict([[num]])
print("Here is Prediction result: " ,int(output))
