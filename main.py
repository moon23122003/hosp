import streamlit as st
import time
import streamlit as st

st.set_page_config(page_title="Smart Diagnosis System", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size:40px;
        color:#2c3e50;
        text-align:center;
        font-weight:bold;
    }
    .subtitle {
        font-size:20px;
        text-align:center;
        color:gray;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Smart Diagnosis System 🩺</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Get instant health predictions based on symptoms</p>', unsafe_allow_html=True)

#-----------------navigation------------
# Sidebar menu
menu = st.sidebar.selectbox("Choose options", ["home","about","sign in","sign up","predict"])

#--------home----------
if options==home:
    import streamlit as st
    import time#core python
    with st.spinner("Loding...."):
        time.sleep(5)
        with st.sidebar:
            st.write("Show the above options")
            st.snow()
            
            st.title("Smart Diagnosis System")

#-----------about----------
if options==about:
    import streamlit as st
    st.title("AboutUs")

#----------sign in-------------
if options==sign in:
    import streamlit as st
    import mysql.connector
    mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="hp")
    my=mydb.cursor()
    
    st.title("SignIn")
    name=st.text_input("USER NAME")
    password=st.text_input("PASSWORD")
    b1=st.button("SIGNIN")
    valid=0
    if b1:
        str1="select * from user_info where username="+"'"+name+"'"+" and pass="+"'"+password+"'"+""
        my.execute(str1)
        res=my.fetchall()
        
        for x in res:
            st.success(x[0])
            st.session_state['username'] = x[0]
            st.session_state['password']=x[1]
            st.switch_page("pages/profile.py")
            
            
            valid=valid+1
            if valid==0:
                st.success("Invalid Login")

#---------------sign up--------------
if options==sign up:
    import streamlit as st
    import random
    import mysql.connector  

    st.title("SignUp")
    h1,h2,h3,h4=st.columns(4)
    name=h1.text_input("USER NAME")
    password=h1.text_input("PASSWORD")
    email=h1.text_input("Email Id")
    age=h1.slider("Age",1,100)
    mobile=h2.text_input("Mobbile Number")
    g=h2.radio("Gender",['M','F'],index=0)
    h2.write("Languages Known")
    c1=h2.checkbox("Hindi")
    c2=h2.checkbox("English")
    c3=h2.checkbox("Nagupri")
    c4=h2.checkbox("Bagla")
#st.link_button("Go to gallery", "https://streamlit.io/gallery")
    address=h3.text_area("Address")
    dob=h3.date_input("DOB")
    photo=h3.file_uploader("Upload Photo")
    color=h4.color_picker("Pick your color")
    live_photo=h4.camera_input("Live Photo")
    count=random.randrange(1, 10)
    str1="img"
    str1=str1+str(count)
    str1=str1+".png"
    count=count+1
    
    if live_photo:
        with open(str1,"wb") as f:
            f.write(live_photo.getvalue())
            def get_data():
                st.success("Following Details Are Save Successfully....")
                st.write(name)
                st.write(password)
                st.write(email)
                st.write(age)
                st.write(mobile)
                st.write(g)
                lang=""
                if c1:
                    lang=lang+"Hin"+" "
                    if c2:
                        lang=lang+"Eng"+" "
                        if c3:
                            lang=lang+"Nag"+" "
                            if c4:
                                lang=lang+"Ban"+" "
                                st.write(lang)
                                st.write(address)
                                st.write(dob)
                                st.write(photo)
                                st.write(color)
                                st.write(str1)
                                mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="hp")
                                my=mydb.cursor()
                                my.execute("insert into user_info values("+"'"+name+"'"+","+"'"+password+"'"+","+"'"+email+"'"+","+"'"+str(age)+"'"+","+"'"+mobile+"'"+","+"'"+g+"'"+","+"'"+lang+"'"+","+"'"+address+"'"+","+"'"+str(dob)+"'"+","+"'"+str1+"'"+")")
                                mydb.commit()
                                
                                b1=st.button("SIGNUP")
                                if b1:
                                    get_data()

#--------------predict----------------
if options==predict:
    import streamlit as st
    st.title("Predict Your Health ")
