# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd

st.title("💅Salon Appointment Booking")

st.write("Fill in the details to book your appointment")


# Inputs

name = st.text_input("Name")

service = st.selectbox(
    "Service",
    ["Nails", "Hair", "Lashes"]
)

# simple if statements (very student style)
if service == "Nails":
    option = st.selectbox("Type", ["Manicure", "Pedicure", "Both"])

elif service == "Hair":
    option = st.selectbox("Type", ["Cut", "Style", "Braids"])

else:
    option = st.selectbox("Type", ["Classic", "Volume"])

date = st.date_input("Date")
time = st.time_input("Time")

# Button

if st.button("Book"):

    if name == "":
        st.write("Please enter your name")

    else:
        # create one row
        customer_deets = {
            "Name": name,
            "Service": service,
            "Type": option,
            "Date": date,
            "Time": time
        }

        df = pd.DataFrame([customer_deets])

        # save to csv
        try:
            old_df = pd.read_csv("appointments.csv")
            df = pd.concat([old_df, df])
        except:
            pass

        df.to_csv("appointments.csv", index=False)

        st.write("✅You've successfully booked your appointment!")
       # st.snow()
       
       


# Show appointments


st.subheader("📋 Appointments List")

try:
    data = pd.read_csv("appointments.csv")
    st.table(data)
except:
    st.write("No bookings yet")
