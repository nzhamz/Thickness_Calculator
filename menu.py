#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import math
import requests


def open_link(url):
  """Opens a link in a new tab using JavaScript."""
  st.write(f'<a href="{url}" target="_blank">Click here for {url.split("/")[-1]}</a>', unsafe_allow_html=True)
    
#model_url0 = 'https://huggingface.co/datasets/Nzham/CRY/resolve/main/NuraMark2.png?download=true'

#response = requests.get(model_url0)
# Display the image from the response
#st.image(response.content, caption="NeuraMark", use_column_width=True)

st.title("Static Equipment Calculator Suite (SECU) ")
st.header("Web-based Corrosion Management Calculator")

# Use function calls for button clicks
if st.button("Tank Retired Thickness Calculator"):
    #open_link('https://nzham-kuk.onrender.com/')
    st.write('Under Devlopment')

elif st.button("Pipe Retired Thickness Calculator"):
    open_link('https://thicknesscalculator-cifmkkwkbnuzztnoxsaruv.streamlit.app/')

elif st.button("Calculating Cathodic Protection Total Anodes"):
    #open_link('https://thicknesscalculator-cifmkkwkbnuzztnoxsaruv.streamlit.app/')
    st.write('Under Devlopment')
