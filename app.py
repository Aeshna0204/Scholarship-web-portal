from flask import Flask, flash, render_template, request, redirect
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null
import validators


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///studentinfo.db"
app.config['SQLALCHEMY_BINDS'] = {'Scholarship': "sqlite:///scholarshipinfo.db",
    'private' : "sqlite:///privatescholarship.db"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class scholarshipinfo(db.Model):
    __bind_key__ = 'Scholarship'
    
    scholarship_id = db.Column(db.Integer, primary_key=True)
    scholarship_name = db.Column(db.String(40), nullable=False)
    scholarship_type = db.Column(db.String(20), nullable=False)
    scholarship_description = db.Column(db.String(1000), nullable=False)
    scholarship_benefits = db.Column(db.String(100), nullable=False) #Up to USD 15,400
    scholarship_start_date = db.Column(db.String(12), nullable=False)  # DD/MM/YYYY
    scholarship_end_date = db.Column(db.String(12), nullable=False)  # DD/MM/YYYY
    scholarship_for_gender = db.Column(db.String(40), nullable=False)  # GIRLS / BOYS / BOTH
    scholarship_for_caste = db.Column(db.String(40), nullable=False)
    scholarship_age_restriction = db.Column(db.String(40), nullable=False) # ABOVE BELOW 55 NO AGE RESTRICTION
    scholarship_apply_link = db.Column(db.String(255), nullable=False)
    scholarship_offered_by = db.Column(db.String(50), nullable=False) #The Ministry of Social Justice and Empowerment
    scholarship_region = db.Column(db.String(50), nullable=False) #India and Other Countries
    scholarship_eligibility = db.Column(db.String(100), nullable=False)
    
    
class studentinfo(db.Model):
    student_id=db.Column(db.Integer,primary_key=True)
    student_first_name = db.Column(db.String(20), nullable=False)
    student_middle_name = db.Column(db.String(20), nullable=False)
    student_last_name = db.Column(db.String(20), nullable=False)
    student_gender = db.Column(db.String(20), nullable=False)
    student_age = db.Column(db.Integer, nullable=False)
    student_email_id = db.Column(db.String(40), nullable=False)
    student_passcode = db.Column(db.String(20), nullable=False)
    student_confirm_passcode=db.Column(db.String(20),nullable=False)
    student_country = db.Column(db.String(30), nullable=False)
    student_city = db.Column(db.String(30), nullable=False)
    student_state = db.Column(db.String(50), nullable=False)
    student_pincode = db.Column(db.Integer, nullable=False)
    student_qualification = db.Column(db.String(30), nullable=False)
    student_category = db.Column(db.String(30), nullable=False)

class privatescholarshipinfo(db.Model):
    __bind_key__= 'private'
    id = db.Column(db.Integer , primary_key=True)
    sch_name = db.Column(db.String(20),nullable=False)
    sch_type= db.Column(db.String(20),nullable=False)
    private_scholarship_for_gender =db.Column(db.String(20),nullable=False)
    private_scholarship_offered_by = db.Column(db.String(20),nullable=False)
    private_scholarship_region =db.Column(db.String(20),nullable=False)
    private_scholarship_benefits=db.Column(db.String(20),nullable=False)
    private_scholarship_for_caste=db.Column(db.String(20),nullable=False)
    private_scholarship_age_restriction = db.Column(db.String(20),nullable=False)
    private_scholarship_eligibility = db.Column(db.String(250),nullable=False)
    person_name=db.Column(db.String(20),nullable=False)
    whatsapp_contact = db.Column(db.Integer , nullable=False)
    mobile_contact = db.Column(db.Integer , nullable=False)
    email_id = db.Column(db.String(20),nullable=False)
    sch_description = db.Column(db.String(150),nullable=False)
    apply_link = db.Column(db.String(255),nullable=False)
    start_date=db.Column(db.String(50),nullable=False)
    end_date=db.Column(db.String(50),nullable=False)


# Flask Mail


# mail= Mail(app)
# @app.route('/admin')
# def mailing():
#     return render_template("mail.html")

# @app.route('/studentregistration',methods=['GET','POST'])
# def send_msg():
#     if request.method == "POST":
#         email = request.form['email']
#         subject= request.form['subject']
#         msg=request.form['message']

#         message=Message(subject,sender="aeshnajain20760@acropolis.in",recipients=[])



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method=='POST':
        admin_email_id = request.form['admin_email_id']
        admin_passcode = request.form['admin_passcode']
        if admin_email_id == "aeshnajain20760@acropolis.in" and admin_passcode == "myalltimefavourite":
            flash("succesfully logged in!")
            return redirect('/admin')
        else:
            flash("try again!!")
    return render_template('adminlogin.html')

@app.route('/studentupdate/<int:student_id>', methods=['GET','POST'])
def studentupdate(student_id):
    if request.method=='POST':
        student_first_name = request.form['student_first_name']
        student_middle_name = request.form['student_middle_name']
        student_last_name = request.form['student_last_name']
        student_gender = request.form['student_gender']
        student_age = request.form['student_age']
        student_email_id = request.form['student_email_id']
        student_passcode = request.form['student_passcode']
        student_confirm_passcode=request.form['student_confirm_passcode']
        student_country=request.form['student_country']
        student_city = request.form['student_city']
        student_state = request.form['student_state']
        student_pincode = request.form['student_pincode']
        student_category=request.form['student_category']
        student_qualification = request.form['student_qualification']
        student_update_object=studentinfo.query.filter_by(student_id=student_id).first()
        student_update_object.student_first_name=student_first_name
        student_update_object.student_middle_name = student_middle_name
        student_update_object.student_last_name = student_last_name
        student_update_object.student_gender = student_gender
        student_update_object.student_age = student_age
        student_update_object.student_email_id = student_email_id
        student_update_object.student_passcode = student_passcode
        student_update_object.student_confirm_passcode=student_confirm_passcode
        student_update_object.student_country=student_country
        student_update_object.student_city = student_city
        student_update_object.student_state = student_state
        student_update_object.student_pincode = student_pincode
        student_update_object.student_category=student_category
        student_update_object.student_qualification = student_qualification
        db.session.add(student_update_object)
        db.session.commit()
    student_update_object=studentinfo.query.filter_by(student_id=student_id).first()
    return render_template('studentupdate.html',student_update_object=student_update_object)

@app.route('/scholarshipupdate/<int:scholarship_id>', methods=['GET', 'POST'])
def scholarshipupdate(scholarship_id):
    if request.method=='POST':
        scholarship_name = request.form['scholarship_name']
        scholarship_type = request.form['scholarship_type']
        scholarship_description = request.form['scholarship_description']
        scholarship_start_date = request.form['scholarship_start_date']
        scholarship_end_date = request.form['scholarship_end_date']
        # scholarship_for_gender = request.form['scholarship_for_gender']
        scholarship_apply_link = request.form['scholarship_apply_link']
        scholarship_offered_by = request.form['scholarship_offered_by'] 
        scholarship_region = request.form['scholarship_region'] 
        # scholarship_benefits = request.form['scholarship_benefits'] 
        scholarship_for_caste=request.form['scholarship_for_caste']
        scholarship_eligibility= request.form['scholarship_eligibility']
        # scholarship_age_restriction = request.form['scholarship_age_restriction']
        scholarship_update_object= scholarshipinfo.query.filter_by(scholarship_id=scholarship_id).first()
        # scholarship_update_object.scholarship_age_restriction=scholarship_age_restriction
        scholarship_update_object.scholarship_eligibility=scholarship_eligibility
        scholarship_update_object.scholarship_name = scholarship_name
        scholarship_update_object.scholarship_type = scholarship_type
        scholarship_update_object.scholarship_description =scholarship_description
        scholarship_update_object.scholarship_start_date = scholarship_start_date
        scholarship_update_object.scholarship_end_date = scholarship_end_date
        # scholarship_update_object.scholarship_for_gender = scholarship_for_gender
        scholarship_update_object.scholarship_for_caste = scholarship_for_caste
        scholarship_update_object.scholarship_apply_link = scholarship_apply_link
        scholarship_update_object.scholarship_offered_by = scholarship_offered_by
        scholarship_update_object.scholarship_region = scholarship_region
        # scholarship_update_object.scholarship_benefits = scholarship_benefits
          
        
        db.session.add(scholarship_update_object)
        db.session.commit()
        flash("Updated Succesfully!!")
        return redirect('/admin') 
    scholarship_update_object = scholarshipinfo.query.filter_by(scholarship_id=scholarship_id).first()
    
    return render_template('scholarshipupdate.html', scholarship_update_object=scholarship_update_object)

@app.route("/scholarshipdelete/<int:scholarship_id>")
def delete(scholarship_id):
    todo = scholarshipinfo.query.filter_by(scholarship_id=scholarship_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/admin")

@app.route("/deleteprivate/<int:scholarship_id>")
def deleteprivate(scholarship_id):
    todo = privatescholarshipinfo.query.filter_by(id=scholarship_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/request")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        scholarship_name = request.form['scholarship_name']
        scholarship_type = request.form['scholarship_type']
        scholarship_description = request.form['scholarship_description']
        scholarship_start_date = request.form['scholarship_start_date']
        scholarship_end_date = request.form['scholarship_end_date']
        scholarship_for_gender = request.form['scholarship_for_gender']
        scholarship_apply_link = request.form['scholarship_apply_link']
        scholarship_offered_by = request.form['scholarship_offered_by'] #The Ministry of Social Justice and Empowerment
        scholarship_region = request.form['scholarship_region'] #India and Other Countries
        scholarship_benefits = request.form['scholarship_benefits'] #Up to USD 15,400
        scholarship_for_caste=request.form['scholarship_for_caste']
        scholarship_age_restriction = request.form['scholarship_age_restriction'] 
        scholarship_eligibility = request.form['scholarship_eligibility']
        scholarship_object = scholarshipinfo(scholarship_age_restriction=scholarship_age_restriction,scholarship_eligibility=scholarship_eligibility,scholarship_for_caste=scholarship_for_caste,scholarship_offered_by=scholarship_offered_by,scholarship_region=scholarship_region,scholarship_benefits=scholarship_benefits, scholarship_apply_link=scholarship_apply_link, scholarship_description=scholarship_description,
                                             scholarship_for_gender=scholarship_for_gender, scholarship_end_date=scholarship_end_date, scholarship_name=scholarship_name, scholarship_start_date=scholarship_start_date, scholarship_type=scholarship_type)
        db.session.add(scholarship_object)
        db.session.commit()
    obj = scholarshipinfo.query.all()
    return render_template('admin.html', obj=obj)


@app.route("/studentregistration", methods=['GET', 'POST'])
def studentregistration():
    if request.method == "POST":
        student_first_name = request.form['student_first_name']
        student_middle_name = request.form['student_middle_name']
        student_last_name = request.form['student_last_name']
        student_gender = request.form['student_gender']
        student_age = request.form['student_age']
        student_email_id = request.form['student_email_id']
        student_passcode = request.form['student_passcode']
        student_confirm_passcode=request.form['student_confirm_passcode']
        student_country=request.form['student_country']
        student_city = request.form['student_city']
        student_state = request.form['student_state']
        student_pincode = request.form['student_pincode']
        student_category=request.form['student_category']
        student_qualification = request.form['student_qualification']
        #student_course = request.form['student_course']
        student_object = studentinfo(student_first_name=student_first_name,student_middle_name=student_middle_name,student_last_name=student_last_name, student_age=student_age,student_category=student_category, student_gender=student_gender, student_email_id=student_email_id,
                                     student_passcode=student_passcode,student_confirm_passcode=student_confirm_passcode,student_country=student_country, student_city=student_city, student_state=student_state, student_pincode=student_pincode, student_qualification=student_qualification)
        db.session.add(student_object)
        db.session.commit()
        if student_passcode==student_confirm_passcode:
            flash("Registered succesfully!!")
            return redirect('/studentlogin')
        else:
            flash("Check password again!!")
    return render_template('studentregistration.html')

# @app.route("/studentregistration",method=['GET','POST'])
# def sendmail():
#     if student_passcode==student_confirm_passcode:
#         email=request.form['student_email_id']
#         subject="Hello {{student_first_name}}"

@app.route("/scholarshipaccept/<int:id>",methods=['GET','POST'])
def accept(id):
    obj=privatescholarshipinfo.query.filter_by(id=id).first()
    scholarship_name=obj.sch_name
    scholarship_type=obj.sch_type
    scholarship_description=obj.sch_description
    scholarship_start_date=obj.start_date
    scholarship_end_date=obj.end_date
    scholarship_for_gender=obj.private_scholarship_for_gender
    scholarship_apply_link=obj.apply_link
    scholarship_offered_by=obj.private_scholarship_offered_by
    scholarship_region = obj.private_scholarship_region #India and Other Countries
    scholarship_benefits = obj.private_scholarship_benefits #Up to USD 15,400
    scholarship_for_caste=obj.private_scholarship_for_caste
    scholarship_age_restriction = obj.private_scholarship_age_restriction
    scholarship_eligibility = obj.private_scholarship_eligibility
    scholarship_object = scholarshipinfo(scholarship_age_restriction=scholarship_age_restriction,scholarship_eligibility=scholarship_eligibility,scholarship_for_caste=scholarship_for_caste,scholarship_offered_by=scholarship_offered_by,scholarship_region=scholarship_region,scholarship_benefits=scholarship_benefits, scholarship_apply_link=scholarship_apply_link, scholarship_description=scholarship_description,scholarship_for_gender=scholarship_for_gender, scholarship_end_date=scholarship_end_date, scholarship_name=scholarship_name, scholarship_start_date=scholarship_start_date, scholarship_type=scholarship_type)
    db.session.add(scholarship_object)
    db.session.commit()
    db.session.delete(obj)
    db.session.commit()
    return redirect("/request")

@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        student_email_id = request.form['student_email_id']
        student_passcode = request.form['student_passcode']
        student_object = studentinfo.query.filter_by(student_email_id=student_email_id).first()
        if student_object.student_passcode == student_passcode:
            return redirect('/portal')
    return render_template('studentlogin.html')

@app.route("/portal", methods=['GET', 'POST'])
def portal():
    args=request.args
    arg=args.get('type')
    if arg:
        obj=scholarshipinfo.query.filter_by(scholarship_for_gender=arg).all()
    arg =args.get('ty')
    if arg:
        obj=scholarshipinfo.query.filter_by(scholarship_type=arg).all()
    else:
        obj=scholarshipinfo.query.all()
    return render_template('portal.html',obj=obj)

@app.route("/sort/<str>", methods=['GET','POST'])
def sort(str):
    obj= scholarshipinfo.query.filter_by(scholarship_for_gender=str).all()
    return render_template('sort.html',obj=obj)

@app.route("/applyscholarship", methods=['GET','POST'])
def private():
    if request.method=='POST':
        sch_name=request.form['sch_name']
        person_name=request.form['person_name']
        sch_type=request.form['sch_type']
        private_scholarship_for_gender = request.form['private_scholarship_for_gender']
        private_scholarship_offered_by = request.form['private_scholarship_offered_by']
        private_scholarship_region = request.form['private_scholarship_region']
        private_scholarship_benefits = request.form['private_scholarship_benefits']
        private_scholarship_for_caste=request.form['private_scholarship_for_caste']
        private_scholarship_age_restriction = request.form['private_scholarship_age_restriction']
        private_scholarship_eligibility = request.form['private_scholarship_eligibility']
        whatsapp_contact=request.form['whatsapp_contact']
        mobile_contact=request.form['mobile_contact']
        email_id=request.form['email_id']
        sch_description=request.form['sch_description']
        apply_link=request.form['apply_link']
        start_date=request.form['start_date']
        end_date=request.form['end_date']
        
        private_scholarship_object=privatescholarshipinfo( private_scholarship_for_gender= private_scholarship_for_gender,private_scholarship_offered_by=private_scholarship_offered_by,private_scholarship_region=private_scholarship_region, private_scholarship_benefits=private_scholarship_benefits,private_scholarship_for_caste=private_scholarship_for_caste,private_scholarship_age_restriction=private_scholarship_age_restriction,private_scholarship_eligibility=private_scholarship_eligibility,sch_name=sch_name,person_name=person_name,sch_type=sch_type,whatsapp_contact=whatsapp_contact,mobile_contact=mobile_contact,email_id=email_id,sch_description=sch_description,apply_link=apply_link,start_date=start_date,end_date=end_date) 
        
        if validators.url(apply_link)==True:
            db.session.add(private_scholarship_object)
            db.session.commit()
            flash("Request sent succesfully!!")
            return redirect('/')
        else:
            flash("Something went wrong, try again!!")     
    return render_template('applyscholarship.html')

@app.route("/request", methods=['GET','POST'])
def requests():
    request_scholarships=privatescholarshipinfo.query.all()
    return render_template('request.html',request_scholarships=request_scholarships)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
