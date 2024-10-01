from flask import flask,request,render_template app=flask(_name_)
@app.route("/register",methods=['GET','POST'])
def register();
if requst methods=='POST';
name=request.form['name']
email=request.form['email']
password=request.form['password']
return rander_template('success.html')
return rander_template('register.html')
if_name_=='_main_';
app.run(host='0.0.0.0')

                  
                  
