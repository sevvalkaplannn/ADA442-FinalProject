# import necessary libraries
import streamlit as st
import pickle
import pandas as pd

# loading the trained model
model=pickle.load(open('ADA442-FinalProject/bank_marketing_predictor2.sav','rb'))

def prediction(features):
    prediction = model.predict(features)
    return prediction[0]

# this is the main function in which we define our webpage  
def main():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bank Marketing Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # following lines create boxes in which user can enter data required to make prediction 
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    job=st.selectbox('Job',('admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed'))
    marital=st.selectbox('Marital',('divorced','married','single'))
    education=st.selectbox('Education',('basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree'))
    default=st.selectbox('Default',('no','yes'))
    housing=st.selectbox('Housing',('no','yes'))
    loan=st.selectbox('Loan',('no','yes'))
    contact=st.selectbox('Contact',('cellular','telephone'))
    month=st.selectbox('Month',( 'apr', 'aug', 'dec', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep'))
    day_of_week=st.selectbox('Day of Week',('fri', 'mon', 'thu', 'tue', 'wed'))
    duration = st.number_input("Duration",step=1)
    campaign = st.number_input("Campaign",step=1) 
    pdays = st.number_input("PDays",step=1)
    previous = st.number_input("Previous",step=1)
    poutcome=st.selectbox('Poutcome',('failure','nonexistent','success'))
    emp_var_rate = st.number_input("Employment Variation Rate")
    cons_price_idx = st.number_input("Consumer Price Index")
    cons_conf_idx = st.number_input("Consumer Confidence Index")
    euribor3m = st.number_input("Euribor 3 month rate")
    nr_employed = st.number_input("Number of Employees")
    

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        features = pd.DataFrame({
        'age': [age],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'emp.var.rate': [emp_var_rate],
        'cons.price.idx': [cons_price_idx],
        'cons.conf.idx': [cons_conf_idx],
        'euribor3m': [euribor3m],
        'nr.employed': [nr_employed],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'month': [month],
        'day_of_week': [day_of_week],
        'duration': [duration],
        'poutcome': [poutcome]})

        prediction_result = prediction(features)
        if prediction_result == 1:
            st.success('Yes')
        else:
            st.success('No')

if __name__=='__main__': 
    main()
