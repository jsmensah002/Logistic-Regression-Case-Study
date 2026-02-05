#Importing the Cusumer_complaints file using pandas
import pandas as pd
df = pd.read_excel('Consumer_Complaints.xlsx')
print(df)

#Data Cleaning: The timely response column has null values so the null values would be replaced with 'No'
df['Timely response?'] = df['Timely response?'].fillna('No')
print(df)

#The aim of this project is to predict whether a customer would receive a timely response based on certain paramets
#Parameters: 'Submitted via', 'State', 'Product', and 'Issue'

#Dummy variables would be needed for the prediction model 
sub_via_dummies = pd.get_dummies(df['Submitted via'], dtype=float)
print(sub_via_dummies)

state_dummies = pd.get_dummies(df['State'],dtype=float)
print(state_dummies)

products_dummies = pd.get_dummies(df['Product'],dtype=float)
print(products_dummies)

issues_dummies = pd.get_dummies(df['Issue'],dtype=float)
print(issues_dummies)

#Defining x and y variables
x = pd.concat([sub_via_dummies,
               state_dummies,
               products_dummies,
               issues_dummies], axis='columns')
print(x)

y = df['Timely response?']
print(y)

#Prediction tests: If a customer in Florida (FL) submits a complain about an incorrect information on his/her payday loan via web, is that customer likely to get a timely response?
submitted_via = 'Web'
state = 'FL'
product = 'Payday loan, title loan, or personal loan'
issue = 'Incorrect information on your report'

row = pd.DataFrame(0.0, index=[0], columns=x.columns)
row.loc[0, submitted_via] = 1
row.loc[0, state] = 1
row.loc[0,product] = 1
row.loc[0,issue] = 1

#Importing logistics regression
import sklearn.linear_model as linear_model
logreg = linear_model.LogisticRegression()
logreg.fit(x,y)

#Prediction test
prediction = logreg.predict(row)[0]
print(prediction)

#Train test split
from sklearn.model_selection import train_test_split as tt
x_train, x_test, y_train, y_test = tt(x,y,test_size=0.2,random_state=0)
logreg.fit(x_train,y_train)

#Checking the regression scores
original_score = logreg.score(x,y)
train_score = logreg.score(x_train,y_train)
test_score = logreg.score(x_test,y_test)
print(original_score)
print(train_score)
print(test_score)

