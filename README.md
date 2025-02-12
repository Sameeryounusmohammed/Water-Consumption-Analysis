# 📊 Water Consumption and Cost Analysis

## 🏗️ Project Overview
This project analyzes **water consumption and cost data (2013 - 2023)** to gain insights into usage patterns and optimize resource management. It involves **data preprocessing, exploratory analysis, and predictive modeling** using machine learning techniques.

### 🔑 Key Aspects:
- 🧼 **Data Cleaning & Preprocessing**: Handling missing values, converting data types, and encoding categorical variables.
- 📈 **Exploratory Data Analysis (EDA)**: Identifying water consumption patterns using visualizations.
- 🤖 **Predictive Modeling**:
  - 🌲 **Random Forest Regression**: Predicts current water charges based on historical consumption data.
  - 📉 **Gradient Boosting Regression**: Estimates revenue using consumption, rate class, and additional charges.
- 🎨 **Visualization**: Generates charts and heatmaps for better insights.

## 📂 Files in the Repository
- 📝 **`Main_file.ipynb`**: The primary notebook where functions are called and results are displayed.
- 🛠️ **`Function_file.py`**: Contains reusable functions for data processing, prediction, and analysis.
- 📊 **`Water_Consumption_And_Cost__2013_-_Feb_2023.csv`**: The dataset used for analysis.
- 📜 **`Capstone_project.pdf`**: A detailed report summarizing findings and results.

## 🚀 How to Run the Code
### **1️⃣ Setup Environment**
1. Install dependencies if not already installed:
   ```sh
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
2. Clone this repository:
   ```sh
   git clone https://github.com/YourUsername/Water-Consumption-Analysis.git
   cd Water-Consumption-Analysis
   ```

### **2️⃣ Run the Project**
#### 🏆 **Option 1: Using Jupyter Notebook**
1. Open Jupyter Notebook:
   ```sh
   jupyter notebook
   ```
2. Open `Main_file.ipynb` and **run all cells** to see the analysis and predictions.

#### 🖥️ **Option 2: Using Python Script (Optional)**
1. Open a terminal in the project directory.
2. Run the main file:
   ```sh
   python Main_file.ipynb
   ```

### **3️⃣ Understanding the Function Calls**
- The `Function_file.py` contains functions that are imported and used inside `Main_file.ipynb`.
- Example function usage in `Main_file.ipynb`:
  ```python
  from Function_file import Predict_current_charges, Predict_revenue
  
  # Load Data
  df = pd.read_csv("Water_Consumption_And_Cost__2013_-_Feb_2023.csv")
  
  # Predict Water Charges
  predicted_charges, accuracy = Predict_current_charges(df)
  print(predicted_charges, accuracy)
  ```

## 📊 **Results & Insights**
- 🔍 Identified **high water consumption developments** that may require optimization.
- 📊 **Predicted revenue and current charges** using machine learning models.
- 📌 **Visualized trends and patterns** to help stakeholders make data-driven decisions.

---

**👨‍💻 Contributors:**
- **Sameer Younus Mohammed**

For any queries, feel free to connect on [🔗 LinkedIn](https://www.linkedin.com/in/sameer-younus-mohammed/). 🚀
