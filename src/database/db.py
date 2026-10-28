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
