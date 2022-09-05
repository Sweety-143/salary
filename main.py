import streamlit as st 
import pickle
pickle_in=open('SalaryPrediction.pkl','rb')
model=pickle.load(pickle_in)

years=st.number_input('Years of Experience')
if st.button('PREDICT'):
  Salary=model.Predict([[Years]])
  st.success(f'SALARYPREDICTED IS {Salary}')
