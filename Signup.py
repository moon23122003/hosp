import streamlit as st
import random
import mysql.connector

st.title("SingUp")
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


