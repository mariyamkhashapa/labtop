import streamlit as st
import pickle
import numpy as np
#import the model 
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
st.title("laptop predictor")
#brand 
company = st.selectbox("Brand",df["Company"].unique())
#type of labtop 
type= st.selectbox("Type",df["TypeName"].unique())
#ram 
Ram=st.selectbox("RAM(in GB)",[2,4,8,12,16,24,32,64])
#weight
weight =st.number_input("Weight of the labtop ")
#touchScreen 
touchscreen=st.selectbox("Touchscreen",["No","Yes"])
#ips 
ips=st.selectbox("IPS",["No","Yes"])
#ppi 
screensize = st.number_input("Screen Size")
#resolution 
resolution = st.selectbox("Screen Resolution ",["1920x1080","1366x768","1600x900","3840x2160","3200x1800","2880x1800","2560x1600","2560x1440","2304x1440"])

#cpu brand
cpu= st.selectbox("Brand",df["Cpu brand"].unique())
#hard drive 
hdd = st.selectbox("HDD (in GB)",[0,128,256,512,1024,2048])
#SSD
ssd = st.selectbox("SSD (in GB)",[0,8,128,256,512,1024])
#gpu
Gpu= st.selectbox("GPU",df["Gpu brand"].unique())
#OS
os= st.selectbox("OS",df["os"].unique())

if st.button("Predict price"):
    ppi=None
    if touchscreen =="Yes":
        touchscreen=1
    else:
        touchscreen=0
    if ips =="Yes":
        ips=1
    else:
        ips=0
    X_res=int(resolution.split("x")[0] )
    Y_res=int(resolution.split("x")[1] )

    ppi=int(((X_res**2)+(Y_res**2))**0.5/screensize)

    query= np.array([company,type,Ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,Gpu,os])
    query=query.reshape(1,12)
    st.title("The predicted price is "+str(round(int(np.exp(pipe.predict(query)[0])))))



