import pandas as pd

dataset = pd.read_csv('/Users/abhay/Desktop/Team-Conatus/Abhay_Pratap_Singh_Task_5/DataClean.csv')

dataset.columns = dataset.columns.str.lower().str.replace(' ','_')
dataset['status'] = dataset['status'].str.lower()
dataset['education'] = dataset['education'].str.lower()
dataset['industry'] = dataset['industry'].str.lower()
dataset['location'] = dataset['location'].str.lower()
dataset['ai_risk'] = dataset['ai_risk'].str.lower()

dataset['status'] = dataset['status'].str.replace('employed','1').str.replace('un1','0')
dataset['location'] = dataset['location'].str.replace('delhi','urban').str.replace('hyderabad','urban').str.replace('bangalore','urban').str.replace('mumbai','urban')
dataset['age_group'] = dataset['age_group'].str.replace('_','-').str.replace(' - ','-').str.replace('+','-100').str.replace(' to ','-')

print(dataset)