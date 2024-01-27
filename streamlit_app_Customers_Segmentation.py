
import joblib
import streamlit as st
import category_encoders
import pandas as pd
import sklearn

RFM_Final_DF_Load= joblib.load("RFM_Final_DF.pkl")

def Category(User_Id):
    # Get the cluster number for the user_id
    cluster = RFM_Final_DF_Load.loc[RFM_Final_DF_Load['User_Id'] == User_Id, 'Cluster'].values[0]
    # Show the appropriate message based on the cluster number
    if cluster == 0:
        return ' Rajasthan Handicrafts, Saraswati Fabrics, Madurai Music Mania Or Jai Hind General Stores, Amritsar Auto Accessories, Gurgaon Gift Gallery'
    elif cluster == 1:
        return ' Rajasthan Handicrafts, Saraswati Fabrics, Madurai Music Mania Or Jai Hind General Stores, Amritsar Auto Accessories, Gurgaon Gift Gallery'
    elif cluster == 2:
        return ' Rajasthan Handicrafts, Saraswati Fabrics, Madurai Music Mania Or Jai Hind General Stores, Amritsar Auto Accessories Or Agra Appliance Arena, Faridabad Footwear Fair'
    elif cluster == 3:
        return ' Rajasthan Handicrafts, Saraswati Fabrics, Madurai Music Mania Or Jai Hind General Stores, Amritsar Auto Accessories, Gurgaon Gift Gallery'
    elif cluster == 4:
        return ' Rajasthan Handicrafts, Saraswati Fabrics, Madurai Music Mania Or Jai Hind General Stores, Amritsar Auto Accessories, Gurgaon Gift Gallery'
    elif cluster == 5:
        return ' Agra Appliance Arena, Faridabad Footwear Fair, Delhi Electronics Or Indore Instrument Inn Or Jai Hind General Stores '

def main():    
    ## Setting up the page title
    st.set_page_config(page_title= 'Customers Segmentation')
    
     # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:GoldenRod'>Customers Segmentation</h1>", unsafe_allow_html=True)
    
    User_Id=st.number_input('Insert User ID, Please',min_value=0, max_value=33457, value=10000,step=50)
    
    if st.button('Confirm'):
        Result = Category(User_Id)
        st.text(f"We recommend to you {Result} ")
        
main()
