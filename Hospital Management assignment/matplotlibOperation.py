
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



patients = ['Aman', 'Riya', 'Karan', 'Neha', 'Rahul',
            'Priya', 'Ankit', 'Sneha', 'Rohit', 'Pooja']

age = [25, 32, 45, 60, 28, 55, 40, 35, 65, 22]

treatment_cost = [5000, 8000, 12000, 20000, 6000,
                  15000, 10000, 7000, 25000, 4000]

days_admitted = [2, 4, 7, 10, 3, 8, 5, 3, 12, 2]

recovery = [90, 85, 75, 60, 95, 70, 80, 88, 55, 98]



# Q1. Bar Chart – Patient Treatment Cost
#
# Create a bar chart to display the treatment cost
# of each patient.
#
# X-axis: Patient Names
# Y-axis: Treatment Cost
# Add title, axis labels and different bar colors.


# plt.figure(figsize=(10, 5))

# colors = ['red', 'blue', 'green', 'orange', 'purple',
#           'pink', 'yellow', 'cyan', 'brown', 'grey']

# plt.bar(patients, treatment_cost, color=colors)

# plt.title("Patient Treatment Cost")
# plt.xlabel("Patient Names")
# plt.ylabel("Treatment Cost (₹)")

# plt.show()






# Q2. Pie Chart – Patient Recovery Status
#
# Create a pie chart to show the proportion of
# patients in each recovery status (Good and
# Needs Attention).
#
# Recovery >= 80% : Good
# Recovery < 80%  : Needs Attention
# Display percentage using autopct.



# good = sum(r >= 80 for r in recovery)
# needs_attention = sum(r < 80 for r in recovery)
# print(good)
# print(needs_attention)
# status_count = [good, needs_attention]

# labels = ['Good', 'Needs Attention']

# colors = ['green', 'red']



# plt.pie(status_count,
#         labels=labels,
#         autopct='%1.1f%%',
#         colors=colors,
#         startangle=90)

# plt.title("Patient Recovery Status")

# plt.show()








# Q3. Histogram – Patient Age Distribution
#
# Create a histogram to represent the age distribution
# of patients.
#
# Requirements:
# bins = 5
# Add X-axis and Y-axis labels.
# Add title and edgecolor.








# plt.hist(age,
#          bins=5,
#          color='skyblue',
#          edgecolor='black')

# plt.title("Patient Age Distribution")
# plt.xlabel("Patient Age")
# plt.ylabel("Number of Patients")

# plt.show()






# Q4. Scatter Plot – Admission Days vs Treatment Cost
#
# Create a scatter plot to analyse the relationship
# between admission days and treatment costs.
#
# X-axis: Days Admitted
# Y-axis: Treatment Cost
# Add appropriate labels and title.







# plt.scatter(days_admitted,
#             treatment_cost,
#             color='blue',
#             marker='o',
#             s=100)

# plt.title("Admission Days vs Treatment Cost")
# plt.xlabel("Days Admitted")
# plt.ylabel("Treatment Cost (₹)")

# plt.grid(True)

# plt.show()






# Q5. Line Graph – Patient Recovery Percentage
#
# Create a line graph to display the recovery
# percentage of each patient.
#
# X-axis: Patient Names
# Y-axis: Recovery Percentage
# Add markers, title, labels and legend.







# plt.plot(patients,
#          recovery,
#          color='green',
#          marker='o',
#          linestyle='-',
#          label='Recovery Percentage')

# plt.title("Patient Recovery Percentage")
# plt.xlabel("Patient Names")
# plt.ylabel("Recovery Percentage")

# plt.legend()

# plt.show()






# Q6. Box Plot – Treatment Cost Analysis
#
# Create a box plot to analyse the distribution
# of patient treatment costs.
#
# Requirements:
# Display median and quartiles.
# Identify outliers.
# Add title and Y-axis label.







plt.boxplot(treatment_cost,
            patch_artist=True,
            boxprops=dict(facecolor='lightblue'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o',
                            markerfacecolor='red',
                            markersize=8))

plt.title("Treatment Cost Analysis")
plt.ylabel("Treatment Cost (₹)")

plt.show()
