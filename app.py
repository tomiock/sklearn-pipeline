import requests
import json
import streamlit as st

st.title("Multiplication API")

st.write("select the numbers from slider below")
x = st.slider("X", 0, 100, 10)
y = st.slider("Y", 0, 100, 10)

inputs = {"x": x, "y": y}

if st.button("Send"):
	# POSTING INPUTS TO MAL API (FASTAPI)
	# Posting inputs to ML API
	response = requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(inputs))

	st.subheader(f"The result is {response}")
