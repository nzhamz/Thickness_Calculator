#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import math



def navigate_to_tank_calculator():
    st.experimental_rerun()  # Force Streamlit to rerun and clear state
    exec(open("tank.py").read())  # Execute the tank_calculator.py file

def navigate_to_pipe_calculator():
    st.experimental_rerun()  # Force Streamlit to rerun and clear state
    exec(open("pipe.py").read())  # Execute the pipe_calculator.py file

st.title("Static CalX")
st.header("Web-based Tank & Pipe Retirement Calculator")

# Use function calls for button clicks
if st.button("Tank Retired Thickness Calculator"):
    navigate_to_tank_calculator()

elif st.button("Pipe Retired Thickness Calculator"):
    navigate_to_pipe_calculator()
