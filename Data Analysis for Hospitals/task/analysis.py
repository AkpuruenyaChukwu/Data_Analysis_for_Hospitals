# write
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')
pd.set_option('display.max_columns', 8)
#set columns  in sports and prenatal tables to be equal to general
cols = general.columns
sports.columns = cols
prenatal.columns = cols
#join tables
df = pd.concat([general, prenatal, sports], ignore_index=True)
#drop unanamed column and entorely empty rows
df.drop(columns="Unnamed: 0", inplace=True)
df.dropna(how='all', inplace=True)
#replace gender with f and m
df['gender'] = df['gender'].str.replace('woman', 'f').replace('female', 'f')
df['gender'] = df['gender'].str.replace('man', 'm').replace('male', 'm')
#replace nan values in prenatal with f
df.loc[df['hospital'] == 'prenatal', 'gender'] ='f'
#replace nan values in investigatins columns with 0
col_na = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
for c in col_na:
    df[c].fillna(0, inplace=True)
#print(df.shape)
#print(df.sample(n=20, random_state = 30))
#hospital with highest number of paients
df.groupby("hospital")["diagnosis"].describe()
# print("The answer to the 1st question is general")
#share of patients in general hospital that suffer from stomach issues
df.groupby("hospital")["diagnosis"].value_counts()
y = 150/461
stomach = round(y, 3)
# print("The answer to the 2nd question is {}".format(stomach))
#share of sports patients with dislocation
x = 61/214
dislocation = round(x,3)
# print("The answer to the 3rd question is {}".format(dislocation))

#difference in median age between general and sports hospital
df.groupby('hospital')['age'].median()
# print("The answer to the 4th question is 19")

#Highest blood test
df.groupby('hospital')['blood_test'].value_counts()
# print("The answer to the 5th question is prenatal, 325 blood tests")

#What is the most common age of a patient among all hospitals
plt.hist(df["age"])
plt.xlabel("Age Distribution")
plt.ylabel("Frequency")
plt.title("Hospital Age Distribution")
plt.show()
print("The answer to the 1st question: 15 -35")

# What is the most common diagnosis among patients in all hospitals? Create a pie chart.
plt.pie(df["diagnosis"].value_counts(), labels = df["diagnosis"].value_counts().index, autopct = '%1.1f%%')
plt.title("Diagnosis Distribution")
plt.show()

print("The answer to the 2nd question: pregnancy")

#Build a violin plot of height distribution by hospitals. Try to answer the questions.
# What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is required to answer this question.

sns.violinplot(x= df["hospital"], y = df["height"], data = df)
plt.title("Height Distribution by Hospital")
plt.xlabel("Hospital")
plt.ylabel("Height")
plt.show()

print("The answer to the 3rd question: It's because the sports hospital has taller patients. The heights of children caused the two peaks")

