import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#set page configurations
st.set_page_config(page_title="Health Guard",layout="wide")

#getting the working Directory of the .py file
working_dir=os.path.dirname(os.path.abspath(__file__))

#loading of thesaved models
diabetes_model=pickle.load(open('diabetes.pkl','rb'))
heart_model=pickle.load(open('heart.pkl','rb'))
parkinsons_model=pickle.load(open('parkinsons.pkl','rb'))



#sidebar for navigation
with st.sidebar:
	selected=option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)



if selected== 'Diabetes Prediction':
	st.title('Welcome to the Diabetes Prediction Model')
	col1,col2,col3=st.columns(3)
	
	glucose=col1.slider('Glucose Level',0,500,120)
	bp	    =col2.slider('Blood Presure level',0,200,120)
	skthic   =col3.slider('Skin thickness Value',0,100,20)
	insulin  =col1.slider('Insulin Level',0,900,30)
	bmi	     =col2.slider('BMI Value',0.0,70.0,25.0)
	dpf	     =col3.slider(' Diabetes Pedigree Function Value' ,0.0,2.5,0.5)
	age	     =col1.slider(' Age of the person',0,100,25)

#buttton
	if st.button('Diabetes Test Result'):
		user_input=[glucose,bp,skthic,insulin,bmi,dpf,age]
		pred=diabetes_model.predict([user_input])[0]
		diab_diagnosis='The Preson is Diabetic ' if pred==1 else 'The Person is not Diabetic'
		st.success(diab_diagnosis)



if selected=='Heart Disease Prediction':
	st.title('Heart Disease Prediction Using ML')
	col1,col2,col3=st.columns(3)

	age		=col1.slider('Age',0,100,50)
	gender      =col2.radio('Gender',['Male','Female'])
	cp		=col3.selectbox('Chest Pain Type',['Type1','Type2','Type3','Type4'])
	trestbps    =col1.slider('Reating blood Preassure',0,200,120)
	chol		=col2.slider('Serum Cholestrol in mg/dl',50,600,200)
	fbs		=col3.radio('Fasting Blood Sugar>120',['Yes','No'])
	restecg	=col1.radio('Resting Electrocardiograph results',['Normal','Abnormal'])
	mhra	=col2.slider('Maximum Heart Rate Achived',50,200,80)
	ang		=col3.radio('Exercise Induced Angina',['Yes','No'])
	oldpeak	=col1.slider('ST depression induced by exercise',0.0,10.0,1.0)
	slope	=col2.selectbox('Slope of the peakexercise ST segment',['Upsloping','Flat','Downsloping'])
	cf		=col3.slider('Major vessels,colored by flourosopy',0,4,0)
	thal		=col1.selectbox('Thalassemia',['Normal','Fixedd Defect','Reversable Defect'])


#mapping for categorical data-->select Box
	cp_mapping={'Type1':0,'Type2':1,'Type3':2,'Type4':3}
	slope_mapping={'Upsloping':0,'Flat':1,'Downsloping':2}
	thal_mapping={'Normal':0,'Fixedd Defect':1,'Reversable Defect':2} 

#buttton
	if st.button('Heart Disease Test Result'):
		user_input=[age,1 if gender=='Male' else 0,cp_mapping[cp],trestbps,chol,1 if fbs=='Yes' else 0,  1 if restecg=='Normal' else 0,mhra,1 if ang=='Yes' else 0 ,oldpeak,slope_mapping[slope],cf,thal_mapping[thal]]
		pred=heart_model.predict([user_input])[0]
		heart_diagnosis='The Preson has Heart Disease ' if pred==1 else 'The Person does not have heart Disease'
		st.success(heart_diagnosis)


#-------------------------------------------------------------------------

if selected=='Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction Using ML')
    col1,col2,col3,col4,col5=st.columns(5)


 	 # Sliders for 22 input features (after dropping 'name' and 'status')
    fo = col1.slider('Fundamental Frequency (Hz)', 0.0, 300.0, 120.0)
    fhi = col2.slider('Highest Frequency (Hz)', 0.0, 600.0, 200.0)
    flo = col3.slider('Lowest Frequency (Hz)', 0.0, 300.0, 100.0)
    jitter_percent = col4.slider('Jitter (%)', 0.0, 1.0, 0.01)
    jitter_abs = col5.slider('Absolute Jitter', 0.0, 0.1, 0.001)
    rap = col1.slider('Relative Amplitude Perturbation', 0.0, 0.1, 0.01)
    ppq = col2.slider('Pitch Period Quotient', 0.0, 0.1, 0.01)
    ddp = col3.slider('Jitter:DDP', 0.0, 0.3, 0.05)
    shimmer = col4.slider('Shimmer Amplitude', 0.0, 1.0, 0.02)
    shimmer_db = col5.slider('Shimmer in Decibels', 0.0, 10.0, 0.5)
    apq3 = col1.slider('APQ3 Shimmer', 0.0, 0.1, 0.02)
    apq5 = col2.slider('APQ5 Shimmer', 0.0, 0.1, 0.03)
    apq = col3.slider('Average Amplitude Perturbation', 0.0, 0.1, 0.03)
    dda = col4.slider('DDA Shimmer', 0.0, 0.3, 0.1)
    nhr = col5.slider('Noise to Harmonic Ratio', 0.0, 1.0, 0.05)
    hnr = col1.slider('Harmonic to Noise Ratio', 0.0, 50.0, 20.0)
    rpde = col2.slider('Recurrence Period Density Entropy', 0.0, 1.0, 0.5)
    dfa = col3.slider('Detrended Fluctuation Analysis', 0.0, 2.0, 0.75)
    spread1 = col4.slider('Spread 1', -10.0, 10.0, 0.5)
    spread2 = col5.slider('Spread 2', -5.0, 5.0, 0.2)
    d2 = col2.slider('Second Frequency Deviation', 0.0, 10.0, 2.0)  # Add d2 input here
    ppe = col1.slider('Pitch Period Entropy', 0.0, 1.0, 0.1)


   



 # Button to get Parkinson's disease test result
    if st.button('Parkinson\'s Test Result'):
        # Prepare user input into a list (22 features after dropping 'name' and 'status')
        user_input = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db,
                      apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2,d2, ppe]

        # Use the Parkinson's model to make a prediction
        pred = parkinsons_model.predict([user_input])[0]

        # Display the diagnosis
        parkinsons_diagnosis = 'The Person has Parkinsons Disease' if pred == 1 else 'The Person does not have Parkinsons Disease'
        st.success(parkinsons_diagnosis)



