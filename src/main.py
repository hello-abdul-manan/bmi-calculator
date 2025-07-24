print('\nBMI Calculator')

# Get inputs
weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))

# Calculate BMI
bmi = weight / (height * height)

# Show the result
print('----------')
print('Your BMI is: ' + str(round(bmi, 2)))
