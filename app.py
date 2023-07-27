from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    return render_template('index.html')


user_details=[]
@app.route('/user_detail', methods=["GET","POST"])


def user_detail():
    if request.method == 'POST' and request.form.get("submit1") == "submit1":
        name = request.form.get("name")
        phone= request.form.get("phone")
        email= request.form.get("email")
        t= {}
        t["name"] = name
        t["phone"] = phone
        t["email"] = email
        t["item1"] = 0
        t["item2"] = 0
        t["item3"] = 0
        t["item4"] = 0
        user_details.append(t)
        return render_template('login.html', data=user_details)
    return render_template('login.html', data=user_details)
@app.route('/update',methods =["GET","POST"])
def update():
    if request.method == "POST" and request.form.get("submit2") == "submit2":
        email=request.form.get("email")
        for i in user_details:
            if i.get("email") == email:
                item1 =request.form.get("item1")
                item2 =request.form.get("item2")
                item3 =request.form.get("item3")
                item4 =request.form.get("item4")
                
                i["item1"] = i.get("item1") + int(item1)
                i["item2"] = i.get("item2") + int(item2)
                i["item3"] = i.get("item3") + int(item3)
                i["item4"] = i.get("item4") + int(item4)
                
        return render_template('login.html',data = user_details)
    
    return render_template('login.html', data=user_details)
@app.route('/delete',methods=["GET","POST"])
def delet():
    if request.method == "POST" and request.form.get("submit2") == "submit2":
        email=request.form.get("email")
        for i in user_details:
            if i.get("email") == email:
                # user_details.remove(i)
                i["item1"] =0
                i["item2"] =0
                i["item3"] =0
                i["item4"] =0
                
                break
                
                
                         
                         
        return render_template('login.html',data = user_details)
    
    return render_template('login.html', data=user_details)
                
    
if __name__ == "__main__":
    app.run(debug=True)