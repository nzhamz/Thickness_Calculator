
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import requests
imo= '➕➖✖️➗'* 3

# Create a text input widget for the image URL
#filenamei1= 'CMC'
#model_url0 = 'https://huggingface.co/datasets/Nzham/V4.5/resolve/main/CMC.png?download=true'

def open_link(url):
  """Opens a link in a new tab using JavaScript."""
  st.write(f'<a href="{url}" target="_blank">Click here for {url.split("/")[-1]}</a>', unsafe_allow_html=True)

# Check if the URL is not empty
#if model_url0:
    # Send a GET request to the URL and get the response
#    response = requests.get(model_url0)
    # Display the image from the response
#    st.image(response.content, caption="CMC", use_column_width=True)
 #########################################################
def set_dark_theme():
  """Sets the background and text colors for a dark theme."""
  style = """
  body {
    background-color: #111;
    color: #ddd;
  }
  """
  st.set_page_config(page_title="CIeT - Corrosion Inspector e-Tool", page_icon=":gear:")
  st.write('<style>' + style + '</style>', unsafe_allow_html=True)

set_dark_theme()

st.title(imo)

    
# Title for the Streamlit app
st.title('Corrosion Inspector e-Tool (CIeT) : ')

st.write('')
#########################################################

if st.button('Pipe Retirement Thickness Calculator'):
    # Open the link in a new tab
    open_link('https://thicknesscalculator-cifmkkwkbnuzztnoxsaruv.streamlit.app/')

st.write('')
#########################################################


if st.button('Tank Retirement Thickness Calculator'):
    # Open the link in a new tab
    st.write('Comming SOOOOOON!!!')
    #open_link('https://tasi-nuramark.onrender.com/')

st.write('')
#########################################################

if st.button('Corrosion Rate & Remaining Life Calculator'):
    # Open the link in a new tab
    st.write('Comming SOOOOOON!!!')
    #open_link('https://tasi-nuramark.onrender.com/')

st.write('')
#########################################################

if st.button('Cathodic Protection Total Anodes Calculator'):
    st.write('Comming SOOOOOON!!!')
  
st.write('')

#########################################################
if st.button('Coating Volume Calculator'):
    st.write('Comming SOOOOOON!!!')

st.write('')


st.title(imo)








