from flask import  request,  send_file, render_template, redirect, jsonify
from openpyxl import load_workbook
  
wb = load_workbook('RegisteredUsers.xlsx') 
sheet1 = wb.active 

print("done setting")

def submit_file():
    top=sheet1.max_row+1
    f = request.files['pp']
    if(f.filename!=''):
        f.save('files/'+f.filename)

        sheet1["A"+str(top)] = request.form['name']
        sheet1["B"+str(top)] = request.form['email']  
        sheet1["C"+str(top)] = request.form['password'] 
        sheet1["D"+str(top)] = f.filename 
        print(f.filename)
        wb.save('RegisteredUsers.xlsx') 
        return redirect('/login')
    else:
        print("No file choosen")
        return redirect('/register')
    

def home():
    return render_template('home.html')

def register():
    return render_template('register.html')

def login():
    return render_template('login.html')

def api_call():
    return render_template('download_file.html', filename="college_id.jpg")

def download():
    return send_file("files/college_id.jpg")

def loginAuth():
    email = request.form["email"]
    password = request.form["password"] 
    print(sheet1.active_cell)
    for row in range(2, sheet1.max_row+1):
        if(sheet1['B'+str(row)].value==email):
            if(sheet1['C' + str(row)].value == password):
                return 'login successfull!"> Hello %s ' %(sheet1['A' + str(row)].value)
            
    return 'login failed'

