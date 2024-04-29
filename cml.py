#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import math


# Decorative emoji string (consider using CSS for styling)
decorative_emojis = "➕➖✖️➗" * 3
st.title(decorative_emojis)

st.title("Corrosion Inspector e-Tool (CIeT) :")

st.header("Corrosion Rate & Remaining Life Calculator")

# Input fields for Tank Calculator (consistent float data type)
original_thickness_mm = st.number_input("Thickness 1, in mm: ", value=10.0, step=0.5)
current_thickness_mm = st.number_input("Thickness 2, in mm: ", value=9.5, step=0.5)
exposure_time_years = st.number_input("Time Between Thickness in Years", value=3.0, step=1.0)
minimum_thickness_mm = st.number_input("Retired Thickness in mm: ", value=3.0, step=1.0)

st.subheader("Corrosion Rate")

# Calculate corrosion rate (ensure consistent data types)
corrosion_rate_mm_per_year = (original_thickness_mm - current_thickness_mm) / float(exposure_time_years)
st.write("Corrosion Rate:", round(corrosion_rate_mm_per_year,2), "mm/y")

# Advanced Settings
st.subheader("Remaining Life")
if current_thickness_mm > minimum_thickness_mm:
    remaining_life_years = (current_thickness_mm - minimum_thickness_mm) / corrosion_rate_mm_per_year
    st.write("Remaining Life:", round(remaining_life_years,1), "years")
else:
    st.write("Warning: Current thickness is below retired thickness. Replace or shutdown immediately!")


st.title(decorative_emojis)  # Display decorative emojis again at the end
