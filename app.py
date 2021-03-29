from flask import Flask, render_template, request  
import mysql.connector
import pickle
import numpy as np
import os
os.chdir("D:\Data Science\Project\P44 Sales Forecasting Excelr\deployement")
app = Flask(__name__)        

@app.route('/')
def home():
    return render_template('index.html')
       
   
@app.route('/customer',methods=['POST']) # decorator
def customer():
    
    if request.method == 'POST':
        output =""
        cust_id = request.form['Cust_id']
        
        if cust_id.isnumeric()== True:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wns$1234",
            database="ecommerce"
            )
            
            mycursor = mydb.cursor()
            executeStr = "Select count(*) from STORE where CustomerID=%s"
            mycursor.execute(executeStr, (cust_id,))
            a_rec_count=mycursor.fetchone()[0]
            if a_rec_count != 0:
                
                executeStr = "SELECT * FROM store WHERE CustomerID=%s"
                mycursor.execute(executeStr, (cust_id,))
                a_rec = mycursor.fetchone()
                NextPurchaseDay = a_rec[1]
                Recency = a_rec[2]
                RecencyCluster = a_rec[3]
                Frequency = a_rec[4]
                FrequencyCluster=a_rec[5]
                Revenue = a_rec[6]
                RevenueCluster = a_rec[7]
                OverallScore	= a_rec[8]
                Segment_High_Value	= a_rec[9]
                Segment_Low_Value	= a_rec[10]
                Segment_Mid_Value = a_rec[11]   
              
               
                loaded_model = pickle.load(open("retail_ecommerce.pkl", "rb"))
                
                #arr= np.array([[17850,303,0,312,1,5288.63,1,2,0,1,0]])
                arr = np.array([[cust_id,NextPurchaseDay,Recency,RecencyCluster,Frequency,FrequencyCluster, Revenue,RevenueCluster,OverallScore,Segment_High_Value,Segment_Low_Value,Segment_Mid_Value]])
                predict_value =loaded_model.predict(arr)
                predict_value = predict_value.item(0)
                if predict_value == 1:
                    output =  "The customer with customer id " + str(cust_id)+  " 'WILL COME' in Next 30 Days"
                    return render_template("index.html", prediction_text = output)
                else:
                    output =  "The customer with customer id " + str(cust_id)+  " 'WILL NOT COME' in Next 30 Days"
                    return render_template("index.html", prediction_text = output)
            else:
                output =  cust_id+" does not exists ! Please Enter Different Customer ID"
                return render_template("index.html", prediction_text = output)
        else:
            output = "Please enter a valid Customer Id"
            return render_template("index.html", prediction_text = output)
        
    else:
        
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False)



