import pandas as pd
import numpy as np
import math
df=pd.read_csv('training_data.csv', lineterminator='\n')
#
print(len(df.index))

row=len(df.index)



#print(df)
#df['int_rate'].str.extract('([0-9]+)').astype(float)
df.int_rate=df['int_rate'].str.extract('([0-9]+)').astype(float)
df.term=df['term'].str.extract('([0-9]+)').astype(float)
df.revol_util=df['revol_util'].str.extract('([0-9]+)').astype(float)
df.int_rate=df.int_rate/100
df.revol_util=df.revol_util/100
#print(df['grade'].mask(df['grade']== 'A',0).head(5))
#grade_change_number


df['grade']=df['grade'].mask(df['grade']== 'A',0)
df['grade']=df['grade'].mask(df['grade']== 'B',1/6)
df['grade']=df['grade'].mask(df['grade']== 'C',2/6)
df['grade']=df['grade'].mask(df['grade']== 'D',3/6)
df['grade']=df['grade'].mask(df['grade']== 'E',4/6)
df['grade']=df['grade'].mask(df['grade']== 'F',5/6)
df['grade']=df['grade'].mask(df['grade']== 'G',6/6)
df.grade=df.grade.astype(float)

df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'A1',1/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'A2',2/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'A3',3/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'A4',4/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'A5',5/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'B1',6/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'B2',7/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'B3',8/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'B4',9/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'B5',10/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'C1',11/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'C2',12/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'C3',13/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'C4',14/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'C5',15/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'D1',16/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'D2',17/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'D3',18/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'D4',19/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'D5',20/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'E1',21/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'E2',22/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'E3',23/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'E4',24/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'E5',25/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'F1',26/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'F2',27/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'F3',28/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'F4',29/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'F5',30/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'G1',31/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'G2',32/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'G3',33/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'G4',34/35)
df['sub_grade']=df['sub_grade'].mask(df['sub_grade']== 'G5',35/35)
df.sub_grade=df.sub_grade.astype(float)

df['emp_length']=df['emp_length'].mask(df['emp_length']== '< 1 year',"0.5")
df['emp_length']=df['emp_length'].mask(df['emp_length']== '10+ years ',"11")
df.emp_length=df['emp_length'].str.extract('([0-9]+)')

df.emp_length=df.emp_length.astype(float)
#"print(df.head(15))
#print (df)
#print(df.dtypes)
#print(df['revol_util'].head(15))
a = max(df['tot_hi_cred_lim'])
df.tot_hi_cred_lim=df.tot_hi_cred_lim/a

a = max(df['dti'])
df.dti=df.dti/a
a = max(df['annual_inc'])

df.annual_inc=df.annual_inc/400000
"""
for j in range(0,row):
    df['annual_inc'][j]=math.tanh(2*df['annual_inc'][j])
    print(j)
"""    
    #print(df['annual_inc'][j],j,a)
a = max(df['mths_since_last_delinq'])
df.mths_since_last_delinq=df.mths_since_last_delinq/a
#a = max(df['mths_since_last_record'])
#df.mths_since_last_record=df.mths_since_last_record/a
a = max(df['revol_bal'])
df.revol_bal=df.revol_bal/a
a = max(df['tot_cur_bal'])
df.tot_cur_bal=df.tot_cur_bal/a
a = max(df['total_bal_il'])
df.total_bal_il=df.total_bal_il/a
a = max(df['max_bal_bc'])
df.max_bal_bc=df.max_bal_bc/a
df.total_bal_il=df.total_bal_il/a
a = max(df['total_rev_hi_lim'])
df.total_rev_hi_lim=df.total_rev_hi_lim/a
#a = max(df['avg_cur_bal'])
#df.avg_cur_bal=df.avg_cur_bal/a
a = max(df['bc_open_to_buy'])
df.bc_open_to_buy=df.bc_open_to_buy/a
a = max(df['total_bal_ex_mort'])
df.total_bal_ex_mort=df.total_bal_ex_mort/a
a = max(df['avg_cur_bal'])
df.avg_cur_bal=df.avg_cur_bal/a
a = max(df['total_bc_limit'])
df.total_bc_limit=df.total_bc_limit/a
a = max(df['total_il_high_credit_limit'])
df.total_il_high_credit_limit=df.total_il_high_credit_limit/a

a = max(df['loan_amnt'])
print("loan_amnt",a)
df.loan_amnt=df.loan_amnt/a
a = max(df['term'])
df.term=df.term/a
a = max(df['installment'])
df.installment=df.installment/a
a = max(df['emp_length'])
df.emp_length=df.emp_length/a
a = max(df['mo_sin_old_rev_tl_op'])
df.mo_sin_old_rev_tl_op=df.mo_sin_old_rev_tl_op/a
a = max(df['mo_sin_old_il_acct'])
df.mo_sin_old_il_acct=df.mo_sin_old_il_acct/a
a = max(df['pct_tl_nvr_dlq'])
df.pct_tl_nvr_dlq=df.pct_tl_nvr_dlq/a
a = max(df['percent_bc_gt_75'])
df.percent_bc_gt_75=df.percent_bc_gt_75/a



# Delete column
del df['emp_title']
print(df.head(2))
#df.to_csv("output.csv", index=None)
"""
print (df['emp_title'])

def remove_duplicates(x):
    list_a = []
    for index,i in enumerate(x):
        list_a.append(i)
        if list_a.count(i) > 1:
            list_a.remove(i)
    return list_a
aaa=remove_duplicates(df['emp_title'])
bbb=np.array(aaa)
print (bbb.shape)
"""
#print(max(df['annual_inc']))


