import mysql.connector
from tkinter import *
import csv
from datetime import datetime
import pandas as pd


prod_file='product_id.csv'

transact_file='fox_store_sales.csv'

now_date=datetime.now().strftime("%Y-%m-%d")



root = Tk()

root.title("Dynamic Sales Data Analysis")
root.geometry('550x300')

lbl = Label(root, text = "Customer Name")
lbl.grid()

lbl2 = Label(root, text = "Quantity")
lbl2.grid()

txt12 = Entry(root, width=10)
txt12.grid(column=1, row=0)


txt21 = Entry(root, width=10)
txt21.grid(column=1, row=1)


prod_data=[]

with open(prod_file,newline='') as csvfile:
    reader= csv.DictReader(csvfile)

    for row in reader:
        prod_data.append(row)

print(prod_data)
transact_data=[]

with open(transact_file,newline='') as csvfile:
    reader= csv.DictReader(csvfile)

    for row in reader:
        transact_data.append(row)


opt_prod_ids=[]

for transaction in prod_data:
    id = transaction['product_id']
    opt_prod_ids.append(id)

print(opt_prod_ids)
variable = StringVar(root)
variable.set(opt_prod_ids[0])

opt = OptionMenu(root, variable,*opt_prod_ids)
opt.grid()



def ok():
    pid= variable.get()
    lbl8 = Label(root, text="Product Id:")
    lbl8.grid(column=1, row=2)
    lbl7 = Label(root, text=pid)
    lbl7.grid(column =2, row =2)

    for product in prod_data:
        if product['product_id'] == pid:
            product_name = product['product_name']
            product_price = product['price']

            lbl9 = Label(root, text="Product Name:")
            lbl9.grid(column=1, row=3)
            lbl10 = Label(root, text=product_name)
            lbl10.grid(column=2, row=3)

            lbl11 = Label(root, text="Product Price:")
            lbl11.grid(column=1, row=4)
            lbl12 = Label(root, text=product_price)
            lbl12.grid(column=2, row=4)

            last_trans = transact_data[-1]
            last_id = int(last_trans['transaction_id'])
            new_id = last_id + 1

            ppqustomer_name = txt12.get()

            p_quantity = txt21.get()
            pp_quantity = int(p_quantity)

            final_data = []
            final_data.extend([new_id, now_date, ppqustomer_name, pid, product_name, pp_quantity, product_price])


            with open('fox_store_sales.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(final_data)

    mydb = mysql.connector.connect(
        host="YOUR HOST",
        user="USERNAME",
        passwd="PASSWORD",
        database="YOURDATABASE"
    )
    csv_file_path = 'fox_store_sales.csv'
    mycursor = mydb.cursor()

    insert_query = """
    INSERT IGNORE INTO foxsales(transaction_id, date, customer_name, product_id, product_name, quantity, price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    df = pd.read_csv(csv_file_path)
    data_to_insert = df.values.tolist()
    mycursor.executemany(insert_query, data_to_insert)
    mydb.commit()

button = Button(root, text="OK",command=ok)
button.grid()

root.mainloop()
