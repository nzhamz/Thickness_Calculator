#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import math
import requests


import streamlit as st


def open_link(url):
    """Opens a link in a new tab using JavaScript."""
    st.write(f'<a href="{url}" target="_blank">Click here for {url.split("/")[-1]}</a>', unsafe_allow_html=True)


def tank_retired_thickness_calculator():
    # Add your content for calculating tank retired thickness here
    st.subheader("Tank Retired Thickness Calculator")
    # Add functionalities like input fields, calculations, and result display
    pass


def pipe_retired_thickness_calculator():
    # Add your content for calculating pipe retired thickness here
    st.subheader("Pipe Retired Thickness Calculator")
    # Add functionalities like input fields, calculations, and result display
    pass


def cathodic_protection_calculator():
    # Add your content for calculating cathodic protection total anodes here
    st.subheader("Calculating Cathodic Protection Total Anodes")
    # Add functionalities like input fields, calculations, and result display
    pass


st.title("Static Equipment Calculator Suite (SECU) ")
st.header("Web-based Corrosion Management Calculator")


# Use function calls for button clicks
if st.button("Tank Retired Thickness Calculator"):
    tank_retired_thickness_calculator()

elif st.button("Pipe Retired Thickness Calculator"):
    pipe_retired_thickness_calculator()

elif st.button("Calculating Cathodic Protection Total Anodes"):
    cathodic_protection_calculator()

else:
    st.write("Please select a calculation tool.")

