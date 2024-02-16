from flask import Flask,redirect,url_for,render_template,request,session,flash,jsonify
from os import path
import pyodbc
import json
app=Flask(__name__)
app.config["SECRET_KEY"]="quanhoangduong"
server = 'LAPTOP-FF387IJ3\HOANGQUAN'
database = 'Account'
username = 'quan'
password = '123456'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

questions = []

#khoi tao trang web dau tien 
@app.route('/')
def index():
    return render_template('trangkhoidau.html')


#Đăng nhập và xử lý đăng nhâp
def check(a,b):
    for row in cursor.execute("select * from NGUOIDUNG"):
        if row[1] == a and row[2] == b:
            return row[0]
    return 0

@app.route('/login', methods=["POST", "GET"] )
def login():
    if request.method=="POST":
        tendangnhap=request.form["username"]
        matkhau=request.form["password"]
        if check(tendangnhap,matkhau)!=0:
            session["user"]=check(tendangnhap,matkhau)
            return redirect(url_for("trangchu"))
        else:
            flash("Tài khoản hoặc mật khẩu của bạn bị sai",category="info")
            return render_template("login.html")
    else:
        return render_template("login.html")


# trang chủ 
@app.route('/trangchu',methods=["POST", "GET"])
def trangchu():
    if "user" in session:
        if request.method=="GET":
            return render_template('trangchu.html')
        else :
            mamonthi=request.form["mamonhoc"]
            questions.clear()
            for row in cursor.execute("SELECT * FROM NGANHANGCAUHOI WHERE mamon IN (?)",(mamonthi)):
                res={}
                res['question']=row[3]
                options=[]
                options.append(row[4])
                options.append(row[5])
                options.append(row[6])
                options.append(row[7])
                res['options']=options
                res['correctAnswer']=row[8]
                questions.append(res)
            return redirect(url_for("get_questions"))
    else:
        flash("Bạn hãy đăng nhập tài khoản",category="info")
        return redirect(url_for("index"))


#thi trắc nghiệm:
@app.route('/thitracnghiem')
def get_questions():
    if "user" in session:
        return render_template('thitracnghiem.html')
    else:
        flash("Bạn hãy đăng nhập tài khoản",category="info")
        return redirect(url_for("index"))
#them cau hoi vao phan data tren web
@app.route('/data')
def get_data():
    if "user" in session:
        return jsonify(questions)
    else:
        flash("Bạn hãy đăng nhập tài khoản",category="info")
        return redirect(url_for("index"))

# Thêm câu hỏi từ web vào database
@app.route('/themmon')
def themde():
    if "user" in session:
        return render_template("themmon.html")
    else:
        flash("Bạn hãy đăng nhập tài khoản",category="info")
        return redirect(url_for("index"))

@app.route('/save-data', methods=['POST'])
def save_data():
    if "user" in session:
        data = request.json  # Lấy dữ liệu được gửi từ trang web
        # Đoạn mã xử lý dữ liệu ở đây (ví dụ: lưu vào cơ sở dữ liệu)
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        for i in data.get('questions'):
            question_text = i.get('question_text')
            option1 = i.get('options')[0]
            option2 = i.get('options')[1]
            option3 = i.get('options')[2]
            option4 = i.get('options')[3]
            correct = i.get('correct_answer')
            if correct=='option1':
                correct_answer=option1
            elif correct=='option2':
                correct_answer=option2
            elif correct=='option3':
                correct_answer=option3
            else:
                correct_answer=option4
            # Thực hiện câu lệnh SQL INSERT INTO
            cursor.execute("INSERT INTO NGANHANGCAUHOI(mamon,tenmon,question,option1,option2,option3,option4,correctAnswer) VALUES (?, ?, ?, ?, ?, ?, ?,?)",
                    (data.get('subject_code'), data.get('subject_name'), question_text, option1, option2, option3, option4, correct_answer))
            conn.commit()
        # Sau đó, trả về phản hồi cho trang web
            return redirect(url_for("trangchu"))
    else:
        flash("Bạn hãy đăng nhập tài khoản",category="info")
        return redirect(url_for("index"))

#xử lý đăng ký tại đây
def check1(a):
    for row in cursor.execute("select * from NGUOIDUNG"):
        if row[1] == a:
            return 0
    return 1

@app.route('/dangky', methods=["POST", "GET"] )
def dangky():
    if request.method=="POST":
        tendangnhap=request.form["username"]
        matkhau=request.form["password"]
        if check1(tendangnhap)!=0:
            cursor.execute("INSERT INTO NGUOIDUNG(username,pass) VALUES (?, ?)",(tendangnhap,matkhau))
            conn.commit()
            flash("Bạn đăng ký tài khoản thành công",category="info")
            return redirect(url_for("index"))
        else:
            flash("Tài khoản bạn đăng ký đã tồn tại",category="info")
            return render_template("dangky.html")
    else:
        return render_template("dangky.html")
    
#code cho phan logout
@app.route("/logout")
def log_out():
    session.pop("user", None)
    return redirect(url_for("index"))






if __name__ == "__main__":
    
    app.run(debug=True)