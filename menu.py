#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import requests

# Create a text input widget for the image URL
filenamei1= 'CMC'
model_url0 = 'https://huggingface.co/datasets/Nzham/V4.5/resolve/main/CMC.png?download=true'

def open_link(url):
  """Opens a link in a new tab using JavaScript."""
  st.write(f'<a href="{url}" target="_blank">Click here for {url.split("/")[-1]}</a>', unsafe_allow_html=True)

# Check if the URL is not empty
if model_url0:
    # Send a GET request to the URL and get the response
    response = requests.get(model_url0)
    # Display the image from the response
    st.image(response.content, caption="CMC", use_column_width=True)
    
    
# Title for the Streamlit app
st.title('Welcome to Corrosion Management Calculator (CMC) : ')

st.write('')
#F

# Button for CYP
if st.button('Pipe Retirement Thickness Calculator'):
    # Open the link in a new tab
    open_link('https://thicknesscalculator-cifmkkwkbnuzztnoxsaruv.streamlit.app/')

st.write('')


# Button for TASI
if st.button('Tank Retirement Thickness Calculator'):
    # Open the link in a new tab
    st.write('Comming SOOOOOON!!!')
    #open_link('https://tasi-nuramark.onrender.com/')

st.write('')


# Button for TASI
if st.button('Cathodic Protection Total Anodes Calculator'):
    st.write('Comming SOOOOOON!!!')


st.write('')

imo= ':rocket:'* 9

st.title(imo)


