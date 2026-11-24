
import numpy as np



patients = ['Aman', 'Riya', 'Karan', 'Neha', 'Rahul',
            'Priya', 'Ankit', 'Sneha', 'Rohit', 'Pooja']

age = [25, 32, 45, 60, 28, 55, 40, 35, 65, 22]

treatment_cost = [5000, 8000, 12000, 20000, 6000,
                  15000, 10000, 7000, 25000, 4000]

days_admitted = [2, 4, 7, 10, 3, 8, 5, 3, 12, 2]

recovery = [90, 85, 75, 60, 95, 70, 80, 88, 55, 98]



# Q1. Convert all numerical lists (age, treatment_cost,
# days_admitted, and recovery) into NumPy arrays.


# age = np.array(age)
# treatment_cost = np.array(treatment_cost)
# days_admitted = np.array(days_admitted)
# recovery = np.array(recovery)

# print("Age Array:", age)
# print("Treatment Cost Array:", treatment_cost)
# print("Days Admitted Array:", days_admitted)
# print("Recovery Array:", recovery)



# Q2. Calculate the average age of all patients.


# average_age = np.mean(age)
# print("Average Age:", average_age)





# Q3. Find the maximum and minimum treatment costs.


# max_cost = np.max(treatment_cost)
# min_cost = np.min(treatment_cost)

# print("Maximum Treatment Cost:", max_cost)
# print("Minimum Treatment Cost:", min_cost)






# Q4. Calculate the total treatment cost of all patients.



# total_cost = np.sum(treatment_cost)
# print("Total Treatment Cost:", total_cost)




# Q5. Calculate the average recovery percentage.



# average_recovery = np.mean(recovery)
# print("Average Recovery Percentage:", average_recovery)




# Q6. Find the patients whose recovery percentage
# is greater than 80%.



# high_recovery = recovery > 80

# print("Patients with Recovery Greater Than 80%:")
# print(np.array(patients)[high_recovery])





# Q7. Find the patients who were admitted for
# more than 5 days.



# long_admission = days_admitted > 5

# print("Patients Admitted for More Than 5 Days:")
# print(np.array(patients)[long_admission])






# Q8. Calculate the standard deviation of
# treatment costs.




# std_cost = np.std(treatment_cost)
# print("Standard Deviation of Treatment Cost:", std_cost)




# Q9. Count the number of patients whose recovery
# percentage is below 70%.
# ==================================================

# below_70 = recovery < 70

# count = np.sum(below_70)

# print("Patients with Recovery Below 70%:", count)
