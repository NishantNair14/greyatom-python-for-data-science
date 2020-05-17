# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 


bank=pd.read_csv(path)
# code starts here

categorical_var=bank.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var)





# code ends here


# --------------
# code starts here
banks=bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode(axis=0)
print(bank_mode)
banks.fillna(bank_mode.iloc[0],inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here



avg_loan_amount=pd.pivot_table(banks,values='LoanAmount',index=['Gender','Married','Self_Employed'],aggfunc=np.mean)



# code ends here



# --------------
# code starts here
loan=0


loan_approved_se=banks[(banks['Loan_Status']=='Y') & (banks['Self_Employed']=='Yes')].count()
loan_approved_nse=banks[(banks['Loan_Status']=='Y') & (banks['Self_Employed']=='No')].count()

loan_approved_se=loan_approved_se[1]
loan_approved_nse=loan_approved_nse[1]
#print(loan_approved_nse,loan_approved_se)  

percentage_se=loan_approved_se*100/614
print(percentage_se)

percentage_nse=loan_approved_nse*100/614
print(percentage_nse) 



# code ends here


# --------------
# code starts here
loan_term=banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)


big_loan_term=sum(loan_term[0:]>=25)
#big_loan_term=loan_term[(loan_term[1]>25)].count()



# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
print(loan_groupby)

print(loan_groupby)
mean_values=loan_groupby.agg(np.mean)
print(mean_values)

#df.groupby('Type 1')['Speed'].agg(np.median)


# code ends here


