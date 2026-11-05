from src.database.config import supabase
import bcrypt #this is for register and login methods i am gonna use



def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pw,hashpw):
    return bcrypt.checkpw(pw.encode(),hashpw.encode()) 

def check_teacher_exists(username):
    #check for unique username, returns false if its already taken.
    response=supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data) > 0  # if exists returns true -- 

def create_teacher(username,password,name):
    # before entering password into data base we will do hashing of this password.
    #using dictionary :
    data={"username": username, "password": hash_pass(password), "name":name}
    response=supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response=supabase.table("teachers").select("*").eq("username",username).execute()
    #this response>data returns an array always
    if response.data:
        teacher=response.data[0]
        if check_pass(password,teacher["password"]):
            return teacher 
    return None

def get_all_students():
    response=supabase.table('students').select("*").execute()
    return response.data

def create_student(new_name, face_embedding=None):
    data={"name":new_name,"face_embedding":face_embedding}
    response=supabase.table('students').insert(data).execute()
    return response.data


def create_subject(subject_code,name,section,teacher_id):
    data={"subject_code":subject_code,"name":name,"section":section,"teacher_id":teacher_id}
    response=supabase.table("subjects").insert(data).execute()
    return response.data


def get_teacher_subjects(teacher_id):
    # we will also keep the inner join , outer join things in this:
    response=supabase.table('teachers').select('*,subject_students(count),attendance_logs(timestamp)').eq("teacher_id",teacher_id).execute()
    subjects=response.data()

    for sub in subjects:
        sub['total_students']=sub.get("subjects_student",[{}])[0].get('count',0) if sub.get("subject_student") else 0 #if anythings not there return empty array
     #while using get we use getback , if got fine , otherwise return empty
        attendance=sub.get("attendance_logs",[])
        unique_sessions= len(set(log['timestamp'] for log in attendance))
        sub['total_classess']=unique_sessions

        sub.pop('student_subject',None)
        sub.pop('attendance_logs',None)
        

