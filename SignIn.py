import streamlit as st
import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="hp")
my=mydb.cursor()

st.title("SingIn")
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
       
                             
                                  



