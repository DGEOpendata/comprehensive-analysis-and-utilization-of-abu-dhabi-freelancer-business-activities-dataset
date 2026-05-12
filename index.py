python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "DL06-Freelance-Activities-ADRA-OD-010-AFR.xlsx"
dataset = pd.read_excel(file_path)

# Displaying the first few rows of the dataset
print("Dataset Preview:")
print(dataset.head())

# Visualizing the distribution of business activities by category
activity_counts = dataset['Activity Category'].value_counts()
activity_counts.plot(kind='bar', figsize=(10, 6), color='skyblue', title='Distribution of Freelancer Business Activities')
plt.xlabel('Activity Category')
plt.ylabel('Number of Activities')
plt.show()

# Example: Filter activities related to sports services
sports_services = dataset[dataset['Activity Name'].str.contains("Sports", case=False)]
print("Sports-related services:")
print(sports_services)

# Save the filtered sports services to a new file
sports_services.to_excel("Sports_Services.xlsx", index=False)
