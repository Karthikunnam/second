from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector


def test_view(request):
    return render(request,"a.html")
def continuepage(request):
    return render(request,"b.html")    
def montlypass(request):
    return render(request,"c.html")    



from django.shortcuts import render
import mysql.connector

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='database-1.cf44eig4s93v.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='9676291170',
            database='KARTHIK'
        )
        
        cursor = connection.cursor()
        
        # Execute SQL query to insert data
        sql = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
        values = (name, email, phone)
        cursor.execute(sql, values)
        
        # Commit changes and close connection
        connection.commit()
        connection.close()
        
        # Redirect to the starting page (a.html)
        return render(request, 'a.html')
    
    # Render the form page (c.html)
    return render(request, 'c.html')
