# Basic Program to calculat GPA from letter grades
# Used to try out github
# Jason Hughes

import pandas as pd

gpa = []

df = pd.read_csv('grades.csv')

letter = df['Grade']

for i in range(len(letter)):
	if letter[i] == 'A':
		gpa.append(4.0)
	elif letter[i] == 'A-':
		gpa.append(3.67)
	elif letter[i] == 'B+':
		gpa.append(3.33)

avg = sum(gpa) / len(gpa)

print (avg)
