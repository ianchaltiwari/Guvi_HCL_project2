# Guvi_HCL_project2

**Stationery Sales Performance Dashboard**


**Project Overview**

This project focuses on analyzing and visualizing stationery shop sales data to identify top-selling products and high-revenue days.
Using Tableau for dashboards and Python (Pandas, Matplotlib, Scikit-learn) for data preprocessing & machine learning, the project demonstrates how data can be transformed into actionable insights.



**The dashboard allows stakeholders to:**
-Explore product-wise and date-wise sales
-Track total revenue and units sold
-Identify trends in sales performance
-Gain insights into customer purchasing behavior



**Objectives**

-Import and clean stationery sales dataset
-Create calculated fields (e.g., Total Revenue = Units × Unit Price)
-Build interactive Tableau dashboards (Bar chart, Line chart, Filters)
-Apply machine learning workflow for predictive insights
-Communicate insights effectively

**Tools & Technologies Used**

-Python (pandas, numpy, matplotlib, scikit-learn)
-Tableau (for visualization & dashboard design)
-GitHub (for project hosting & version control)




📂 Project Structure
│
├── data/
│   └── stationery_sales.csv        # Dataset
|
├──output/
|   └── Screenshot (10).png        #screnshot of dashboard
|       Screenshot (11).png        #screnshot of dashboard
|       Screenshot (7).png         #screnshot of dashboard
|       Screenshot (8).png         #screnshot of dashboard
|       Screenshot (9).png         #screnshot of dashboard
|       sales_trend.png            #generated graph through python
│
├── scripts/
│   └── sales.py                    # ML workflow (data prep + regression)
│
├── tableau/
│   └── sales_performance_dashboard.twbx   # Tableau workbook file
│
│
├── requirements.txt                # Required Python libraries
├── README.md                       # Project documentation


**Setup & Installation**

-Clone the repository:
git clone https://github.com/ianchaltiwari/Guvi_HCL_project2.git
cd Guvi_HCL_project2

-Install dependencies:
pip install -r requirements.txt

-Run Python script:
python scripts/sales.py
Open Tableau file:

-Import tableau/stationery_dashboard.twbx
Connect with the dataset (data/stationery_sales.csv)
Explore the interactive dashboard


**Expected Output**

A Tableau dashboard with:
✅ Bar Chart → Product vs Total Revenue
✅ Line Chart → Date vs Units Sold
✅ Filters for Product & Date
✅ KPIs → Total Revenue, Units Sold

Machine Learning output:
✅ Predict revenue based on sales data
✅ Show evaluation metrics (MSE, R²)




Anchal Tiwari
tiwarianchal539@gmail.com
