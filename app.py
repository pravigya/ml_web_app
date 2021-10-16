# importing the packages
import streamlit as st


# importingthe files
from eda import eda
from ml import ml

def main():

	menu = ["Home","Prediction Section"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.write("# Early Stage heart attack risk predictor app")
	elif choice == "Prediction Section":
		ml()
			
main()