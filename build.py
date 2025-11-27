import streamlit as st 
import matplotlib.pyplot as plt 
import pandas as pd
st.set_page_config(page_title="Converters")

selectbox=st.sidebar.selectbox(
    "Select the type of converter",
    ("Home page","Temperature","Currency","Weight","Distance","Contact Info")
)
if selectbox=="Temperature":
    title=st.header("Temperature")
    st.subheader("Welcome to the Temperature page")
    fr = st.selectbox("From:",["Fahrenheit","Celcius","Kelvin","Rankine"])
    to = st.selectbox("To :",["Fahrenheit","Celcius","Kelvin","Rankine"])
    value = st.number_input("value:")
    if fr == "Fahrenheit" :
        if to == "Celcius":
            st.write((value-32)*(5/9))
        elif to == "Kelvin":
            st.write(( value - 32)* (5/9) + 273.15)
        elif to == "Rankine" :
            st.write(value + 459.67)
    if fr == "Celsius" :
        if to == "Fahrenheit":
            st.write(value*(9/5)+32)
        elif to == "Kelvin":
            st.write(( value + 273.15))
        elif to == "Rankine" :
            st.write((value + 273.15)*(9/5))
    if fr == "Kelvin" :
        if to == "Fahrenheit":
            st.write(value-273.15*(9/5)+32)
        elif to == "Celcius":
            st.write(( value - 273.15))
        elif to == "Rankine" :
            st.write(value*(9/5))
    if fr == "Rankine" :
        if to == "Fahrenheit":
            st.write((value-459.67))
        elif to == "Kelvin":
            st.write( value * (5/9))
        elif to == "Celcius" :
            st.write((value + 491.67)*(5/9))
    if fr==to:
        st.write(value)
elif selectbox=="Home page":
    title=st.title("Home Page")
    with st.expander("See explanation"):
        st.header("Index")
        st.subheader("Temperature Overview")
        data={"Temperature":["Fahreheit","Kelvin","Rankine"],"Values":[33.8,274.15,493.67]}
        data=pd.DataFrame(data)
        fig , ax= plt.subplots()
        ax.bar(data["Temperature"],data["Values"],color=["black","red","green"])
        ax.grid(True)
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Values of 1°C")
        ax.set_title("Temperature Graph")
        plt.xticks(rotation=45)
        st.pyplot(fig)
        st.write("1°C=33.8°F")
        st.write("1°C=247.15K")
        st.write("1°C=493.67°R")
        st.subheader("Currency Overview")
        data2={"Currency":["Kuwaiti Dinar","Bahrain Dinar","Omani Rial","Jordanian Dinar","British Pound"],"Values":[270,220,215,118,105]}
        data2=pd.DataFrame(data2)
        fig2 , ax2= plt.subplots()
        ax2.plot(data2["Currency"],data2["Values"],marker="o",linestyle="--",color="black",markerfacecolor="red")
        ax2.grid(True)
        ax2.set_ylabel("Value of Rupees in different currencies")
        ax2.set_xlabel("Top 5 currencies")
        ax2.set_title("Rupees Vs Top5 currencies")
        plt.xticks(rotation=45)
        st.pyplot(fig2)
        st.write("1KWD=270 INR")
        st.write("1BHD=220 INR")
        st.write("1OMR=215 INR")
        st.write("1JOD=118 INR")
        st.write("1GBP=105 INR")
        st.subheader("Weight Overview")
        data3={"Weights":["Grams","Ounce","Pounds"],"Values":[1000,35.274,2.204]}
        data3=pd.DataFrame(data3)
        fig3 , ax3= plt.subplots()
        ax3.scatter(data3["Weights"],data3["Values"])
        ax3.grid(True)
        ax3.set_ylabel("Different weight categories")
        ax3.set_xlabel("Value in Kgs")
        ax3.set_title("Weight unit comparison")
        plt.xticks(rotation=45)
        st.pyplot(fig3)
        st.write("1kg=1000 gm")
        st.write("1kg=35.274 oz")
        st.write("1kg=2.204 lb")
        st.subheader("Distance Overview")
        data4={"Distance":["Kilometer","Meter","Yards"],"Values":[1.6,1609,1760]}
        data4=pd.DataFrame(data4)
        fig4 , ax4= plt.subplots()
        ax4.barh(data4["Distance"],data4["Values"],color="black")
        ax4.grid(True)
        ax4.set_xlabel("Value in 1Mile")
        ax4.set_ylabel("Different Distance unit")
        ax4.set_title("Ditance unit comparison")
        plt.xticks(rotation=45)
        st.pyplot(fig4)
        st.write("1Mile=1.6 Km")
        st.write("1Mile=1609 meters")
        st.write("1Mile=1760 yards")
        st.subheader("Height Overview")
        data5={"Height":["Meter","feet","inches"],"Values":[100,30.48,2.54]}
        data5=pd.DataFrame(data5)
        fig5 , ax5= plt.subplots()
        ax5.pie(data5["Values"],labels=data5["Height"],autopct="%1.1f%%")
        ax5.set_title("Height unit comparison")
        plt.xticks(rotation=45)
        st.pyplot(fig5)
        st.write("1 centimetre=100 meter")
        st.write("1 centimetre=30.48 feet")
        st.write("1 centimetre=2.54 inches")

elif selectbox=="Currency":
    st.title("Currency Converter")

    fr = st.selectbox("From:",["USD","EUR","INR","JPY","AED"])
    to = st.selectbox("To :",["USD","EUR","INR","JPY","AED"])
    value = st.number_input("value:")
    if fr == "USD" :
        if to == "EUR":
            st.write(value*0.867)
        elif to == "INR":
            st.write(value*89.19)
        elif to == "JPY" :
            st.write(value*156.5)
        elif to == "AED" :
            st.write(value*3.67)
    if fr == "EUR" :
        if to == "USD":
            st.write(value*1.153)
        elif to == "INR":
            st.write(value*102.89)
        elif to == "JPY" :
            st.write(value*180.4)
        elif to == "AED" :
            st.write(value*4.234)
    if fr == "INR" :
        if to == "EUR":
            st.write(value*0.00972)
        elif to == "USD":
            st.write(value*0.0112)
        elif to == "JPY":
            st.write(value*1.75)
        elif to == "AED" :
            st.write(value*0.0409)
    if fr == "JPY" :
        if to == "EUR":
            st.write(value*0.00554)
        elif to == "INR":
            st.write(value*0.570)
        elif to == "USD" :
            st.write(value*0.00639)
        elif to == "AED" :
            st.write(value*0.0234)
    if fr == "AED" :
        if to == "EUR":
            st.write(value*0.236)
        elif to == "INR":
            st.write(value*24.43)
        elif to == "JPY" :
            st.write(value*42.67)
        elif to == "USD" :
            st.write(value*0.272)
    if fr == to :
        st.write(value)
elif selectbox=="Weight":
    st.title("Weight Converter")
    fr = st.selectbox("From :",["Kilogram","Ounce","Pound"])
    to= st.selectbox("To :",["Kilogram","Ounce","Pound"])
    value=st.number_input("Enter the value : ")
    if fr=="Kilogram":
        if to=="Ounce":
            st.write(value*35.273)
        elif to=="Pound":
            st.write(value*2.204)
    elif fr=="Ounce":
        if to=="Kilogram":
            st.write(value*0.0283)
        elif to=="Pound":
            st.write(value*0.0625)
    elif fr=="Pound":
        if to=="Kilogram":
            st.write(value*0.453)
        elif to=="Ounce":
            st.write(value*16)
    elif fr==to:
        st.write(value)
elif selectbox=="Distance":
    st.title("Distance Converter")
    fr= st.selectbox("From :",["Mile","Kilometer","Yards","Meter"])
    to= st.selectbox("To :",["Mile","Kilometer","Yards","Meter"])
    value=st.number_input("Enter the value : ")
    if fr =="Mile":
        if to=="Kilometer":
            st.write(value*1.6)
        elif to=="Yards":
            st.write(value*1760)
        elif to=="Meter":
            st.write(value*1609)
    elif fr=="Kilometer":
        if to=="Mile":
            st.write(value*0.62)
        elif to=="Yards":
            st.write(value*1093)
        elif to=="Meter":
            st.write(value*1000)
    elif fr=="Yards":
        if to=="Mile":
            st.write(value*0.00057)
        elif to=="Kilometer":
            st.write(value*0.00091)
        elif to=="Meter":
            st.write(value*0.914)
    elif fr=="Meter":
        if to=="Mile":
            st.write(value*0.00062)
        elif to=="Kilometer":
            st.write(value*0.001)
        elif to=="Yards":
            st.write(value*1.093)
    elif fr==to:
        st.write(value)
elif selectbox=="Contact Info":
    st.title("Team Dynamite")
    st.header("Team Info")
    st.subheader("1.Vinamra Bajaj")
    st.subheader("2.Vaishali Garg")
    st.subheader("3.Krish Sinha")
