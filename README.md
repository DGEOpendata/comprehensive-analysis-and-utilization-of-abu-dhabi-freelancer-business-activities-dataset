markdown
# Freelancer Business Activities Analysis

This repository contains a Python script that demonstrates how to utilize the "Freelancer Business Activities Dataset" for analysis and insights. The dataset includes information about various freelancer business activities in Abu Dhabi, such as sports services, consultancy, project management, and more.

### Requirements
- Python 3.7+
- pandas
- matplotlib

### Getting Started

1. **Download the Dataset:**
   Ensure you have the dataset file named `DL06-Freelance-Activities-ADRA-OD-010-AFR.xlsx`. You can download it from the official Abu Dhabi open data platform.

2. **Install Required Libraries:**
   Make sure you have the required Python libraries installed. You can install them using pip:
   
   pip install pandas matplotlib
   

3. **Run the Script:**
   Place the dataset file in the same directory as the script. Then, execute the script using the command:
   
   python analyze_freelancer_activities.py
   

4. **Output:**
   - The script will display a preview of the dataset.
   - A bar chart showing the distribution of business activities by category will be displayed.
   - A filtered list of sports-related services will be printed in the console.
   - A new Excel file `Sports_Services.xlsx` containing the filtered sports services will be saved in the current directory.

### Customization
- To filter activities by a different keyword, modify the line:
  python
  sports_services = dataset[dataset['Activity Name'].str.contains("Sports", case=False)]
  
  Replace "Sports" with the desired keyword.

- To change the visualization, you can modify the `plot` function parameters or use a different plot type.

### Contribution
We welcome contributions to enhance this script. Feel free to submit pull requests or open issues for suggestions.

### License
This project is licensed under the MIT License. Refer to the LICENSE file for details.
