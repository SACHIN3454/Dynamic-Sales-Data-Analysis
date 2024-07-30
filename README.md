Dynamic Sales Data Analysis Project
Project Overview
This project is designed to dynamically analyze sales data, update transactions, and visualize the sales data using Power BI. The user interface is built with Tkinter, and the sales data is stored and managed in a MySQL database. The project also includes a Power BI dashboard for comprehensive data analysis.

Features
User interface for updating sales transactions.
Integration with MySQL for data storage.
Real-time data updates and analysis.
Power BI dashboard for visualizing sales data.
Getting Started
Prerequisites
Make sure you have the following modules installed:

mysql-connector-python
tkinter
pandas
You can install these modules using pip:

sh
Copy code
pip install mysql-connector-python pandas
Data Files
product_id.csv: Contains the product IDs, names, and prices.
fox_store_sales.csv: Contains the transaction data.
These files are provided as sample datasets. You can replace them with your own data files.

MySQL Database
Ensure you have a MySQL database set up. You will need to create a table for storing the sales data. Below is an example of the SQL query to create the required table:

sql
Copy code
CREATE TABLE foxsales (
    transaction_id INT PRIMARY KEY,
    date DATE,
    customer_name VARCHAR(255),
    product_id VARCHAR(255),
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2)
);
Configuring the Database Connection
In the Python script, update the following lines with your MySQL database connection details:

python
Copy code
mydb = mysql.connector.connect(
    host="YOUR HOST",
    user="USERNAME",
    passwd="PASSWORD",
    database="YOUR DATABASE"
)
Running the Project
Place the product_id.csv and fox_store_sales.csv files in the same directory as the script.
Run the Python script:
sh
Copy code
python your_script_name.py
This will launch the Tkinter interface for updating sales transactions.

Power BI Dashboard
The Power BI dashboard file DynamicSalesDataAnalysis.pbix is provided for visualizing the sales data. To use it:

Open the DynamicSalesDataAnalysis.pbix file in Power BI Desktop.
Update the data source settings to point to your MySQL database.
Usage
Enter the customer name and quantity in the respective fields.
Select the product from the dropdown menu.
Click the "OK" button to update the transaction.
The transaction will be added to the fox_store_sales.csv file and inserted into the MySQL database. The Power BI dashboard can then be refreshed to see the updated data.

Sample Data
The provided datasets (product_id.csv and fox_store_sales.csv) are sample data files. Replace them with your actual data as needed.

Contributing
Feel free to contribute to this project by submitting issues or pull requests

Author
Sachin S
