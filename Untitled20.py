#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd


# In[47]:


data = pd.read_csv('C:/Users/Lenovo/final university ranking.csv')
data


# # Display the top 5 rows

# In[48]:


top_5_rows = data.head()
top_5_rows


# # Display the last 5 rows

# In[49]:


last_5_rows = data.tail()
last_5_rows


# # Check the shape of the dataset

# In[50]:


data_shape = data.shape
print("Shape of the dataset:", data_shape)


# # Check the datatypes of each feature

# In[51]:


data_dtypes = data.dtypes
print("Data types of each feature:\n", data_dtypes)


# # Check the statistical summary

# In[52]:


data_description = data.describe()
data_description


# # Check for null values

# In[53]:


null_values = data.isnull().sum()
print("Null values in each column:")
null_values


# # Check for duplicate values

# In[54]:


duplicate_values = data.duplicated().sum()
print("Number of duplicate rows:")
duplicate_values


# # #Check for anomalies or wrong entries

# In[55]:


for column in data.columns:
    if data[column].dtype == 'object':
        unique_values = data[column].unique()
        print(f"Unique values in {column}")
        unique_values
    else:
        value_range = (data[column].min(), data[column].max())
        print(f"Range of values in {column}")
        value_range


# # Check for outliers and their authenticity

# In[56]:


numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

Q1 = data[numeric_columns].quantile(0.25)
Q3 = data[numeric_columns].quantile(0.75)
IQR = Q3 - Q1

outliers = ((data[numeric_columns] < (Q1 - 1.5 * IQR)) | (data[numeric_columns] > (Q3 + 1.5 * IQR))).sum()
print("Number of outliers in each column:\n", outliers)
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

Q1 = data[numeric_columns].quantile(0.25)
Q3 = data[numeric_columns].quantile(0.75)
IQR = Q3 - Q1

outliers = ((data[numeric_columns] < (Q1 - 1.5 * IQR)) | (data[numeric_columns] > (Q3 + 1.5 * IQR))).sum()
print("\nNumber of outliers in each column:\n", outliers)


# # 10.1: Drop duplicate rows

# In[57]:


data_cleaned = data.drop_duplicates()
print("Shape after dropping duplicates:", data_cleaned.shape)


# # 1.	Application and Enrollment Analysis
# Step 1: What is the average number of applications received by colleges?
# 

# In[58]:


average_applications = data_cleaned['Apps'].mean()
print("Average number of applications received by colleges:", average_applications)


# In[59]:


# Step 2: What percentage of applications are accepted on average across all colleges?
average_acceptance_rate = (data_cleaned['Accept'].sum() / data_cleaned['Apps'].sum()) * 100
print("Average percentage of applications accepted:", average_acceptance_rate)


# In[60]:


# Step 3: What is the average enrollment rate (number of students enrolled divided by number of applications accepted)?
average_enrollment_rate = (data_cleaned['Enroll'].sum() / data_cleaned['Accept'].sum()) * 100
print("Average enrollment rate:", average_enrollment_rate)


# In[61]:


# Step 4: Which college has the highest number of applications received?
college_highest_apps = data_cleaned.loc[data_cleaned['Apps'].idxmax(), 'Names']
highest_apps = data_cleaned['Apps'].max()
print("College with the highest number of applications received:", college_highest_apps)
print("Number of applications received by this college:", highest_apps)


# # 2.	Academic Excellence

# In[62]:


# Step 1: What is the average percentage of new students from the top 10% of their higher secondary class across all colleges?
average_top10perc = data_cleaned['Top10perc'].mean()
print("Average percentage of new students from the top 10% of their higher secondary class:", average_top10perc)


# In[63]:


# Step 2: What is the average percentage of new students from the top 25% of their higher secondary class?
average_top25perc = data_cleaned['Top25perc'].mean()
print("Average percentage of new students from the top 25% of their higher secondary class:", average_top25perc)


# In[64]:


# Step 3: Is there a correlation between the percentage of students from the top 10% and the top 25% of their higher secondary class?
correlation_top10_top25 = data_cleaned[['Top10perc', 'Top25perc']].corr().iloc[0, 1]
print("Correlation between the percentage of students from the top 10% and the top 25% of their higher secondary class:", correlation_top10_top25)


# # Student Demographics

# In[65]:


# Step 1: What is the average number of full-time undergraduate students per college?
average_fulltime_undergrad = data_cleaned['F.Undergrad'].mean()
print("Average number of full-time undergraduate students per college:", average_fulltime_undergrad)


# In[66]:


# Step 2: What is the average number of part-time undergraduate students per college?
average_parttime_undergrad = data_cleaned['P.Undergrad'].mean()
print("Average number of part-time undergraduate students per college:", average_parttime_undergrad)


# In[67]:


# Step 3: Which college has the highest number of out-of-state students?
college_highest_outstate = data_cleaned.loc[data_cleaned['Outstate'].idxmax(), 'Names']
highest_outstate = data_cleaned['Outstate'].max()
print("College with the highest number of out-of-state students:", college_highest_outstate)
print("Number of out-of-state students in this college:", highest_outstate)


# # Cost and Spending

# In[68]:


# Step 1: What is the average cost of room and board across all colleges?
average_room_board_cost = data_cleaned['Room.Board'].mean()
print("Average cost of room and board across all colleges:", average_room_board_cost)


# In[69]:


# Step 2: What is the average estimated book cost for a student?
average_book_cost = data_cleaned['Books'].mean()
print("Average estimated book cost for a student:", average_book_cost)


# In[70]:


# Step 3: What is the average estimated personal spending for a student?
average_personal_spending = data_cleaned['Personal'].mean()
print("Average estimated personal spending for a student:", average_personal_spending)

# Step 4: How does the instructional expenditure per student vary across colleges?
# For variation, we can compute the minimum, maximum, and range (difference between max and min) of 'Expend'
min_expenditure = data_cleaned['Expend'].min()
max_expenditure = data_cleaned['Expend'].max()
range_expenditure = max_expenditure - min_expenditure
print("Minimum instructional expenditure per student:", min_expenditure)
print("Maximum instructional expenditure per student:", max_expenditure)
print("Range of instructional expenditure per student:", range_expenditure)


# # Faculty Qualifications

# In[71]:


# Step 1: What is the average percentage of faculties with Ph.D.s across all colleges?
average_phd_percentage = data_cleaned['PhD'].mean()
print("Average percentage of faculties with Ph.D.s across all colleges:", average_phd_percentage)


# In[72]:


# Step 2: What is the average percentage of faculties with terminal degrees?
average_terminal_percentage = data_cleaned['Terminal'].mean()
print("Average percentage of faculties with terminal degrees across all colleges:", average_terminal_percentage)


# In[73]:


# Step 3: Is there a correlation between the percentage of faculties with Ph.D.s and the graduation rate?
correlation_phd_gradrate = data_cleaned[['PhD', 'Grad.Rate']].corr().iloc[0, 1]
print("Correlation between percentage of faculties with Ph.D.s and graduation rate:", correlation_phd_gradrate)


# # Student-Faculty Interaction

# In[74]:


# Average percentage of faculties with Ph.D.s across all colleges
avg_phd = data['PhD'].mean()
print(f"Avg.percentage of faculties with Ph.D.s: {avg_phd:.2f}%")


# In[75]:


# Average percentage of faculties with terminal degrees across all colleges
avg_terminal = data['Terminal'].mean()
print(f"Avg. percentage of faculties with terminal degrees: {avg_terminal:.2f}%")


# In[76]:


# Correlation between the percentage of faculties with Ph.D.s and the graduation rate
corr_phd_grad = data['PhD'].corr(data['Grad.Rate'])
print(f"Correlation between faculties with Ph.D.s and graduation rate: {corr_phd_grad:.2f}")


# # Faculty qualificatioin

# In[92]:


# Average student/faculty ratio across all colleges
avg_ratio = data['S.F.Ratio'].median()
print(f"Avg. student/faculty ratio: {avg_ratio:.2f}")


# In[94]:


# Correlation between the student/faculty ratio and the graduation rate
corr_sfratio_grad = data['S.F.Ratio'].corr(data['Grad.Rate'])
print(f"Correlation between student/faculty ratio and graduation rate: {corr_sfratio_grad:.2f}")


# In[78]:


# Correlation between the student/faculty ratio and the graduation rate
corr_sfratio_grad = data['S.F.Ratio'].corr(data['Grad.Rate'])
print(f"Correlation between student/faculty ratio and graduation rate: {corr_sfratio_grad:.2f}")


# # Graduation rates

# In[82]:


# Average graduation rate across all colleges
average_graduation_rate = data['Grad.Rate'].mean()
print(f"Average graduation rate: {average_graduation_rate:.2f}%")


# In[84]:


# College with the highest graduation rate
top_col = data.loc[data['Grad.Rate'].idxmax(), 'Names']
print(f"College with highest graduation rate: {top_col}")


# In[85]:


# Correlation between the instructional expenditure per student and the graduation rate
expend_grad_corr = data['Expend'].corr(data['Grad.Rate'])
print(f"Correlation between instructional expenditure per student and graduation rate: {expend_grad_corr:.2f}")


# # Alumni Engagement

# In[87]:


# Average percentage of alumni who donate across all colleges
avg_alumni = data['perc.alumni'].mean()
print(f"Average alumni donation rate: {avg_alumni:.2f}%")


# In[89]:


# Correlation between the percentage of alumni who donate and the graduation rate
corr_alumni_grad = data['perc.alumni'].corr(data['Grad.Rate'])
print(f"Correlation between alumni donation rate and graduation rate: {corr_alumni_grad:.2f}")


# In[ ]:




