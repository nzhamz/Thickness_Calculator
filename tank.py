#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import math

def calculate_tank_thickness(diameter, height, yield_strength, tensile_strength, joint_efficiency, minimum_plate_thickness_m, density_water, gravity):
  diameter_m = diameter / 100
  height_m = height / 100

  head_pressure = density_water * height_m * gravity / 1000

  bottom_thickness_m = (2 * head_pressure * diameter_m) / (3 * yield_strength * joint_efficiency)
  shell_body_thickness_m = (head_pressure * diameter_m) / (yield_strength * joint_efficiency)
  top_thickness_m = minimum_plate_thickness_m

  # Ensure minimum thickness is 2.5 mm
  bottom_thickness_m = max(bottom_thickness_m, 0.0028)
  shell_body_thickness_m = max(shell_body_thickness_m, 0.0028)
  top_thickness_m = max(top_thickness_m, 0.0028)

  bottom_thickness_mm = bottom_thickness_m * 1000
  shell_body_thickness_mm = shell_body_thickness_m * 1000
  top_thickness_mm = top_thickness_m * 1000

  # Removed commented section for retired thickness per course

  return bottom_thickness_mm, shell_body_thickness_mm, top_thickness_mm



imo= '➕➖✖️➗'* 3
st.title(imo)

st.title("Corrosion Inspector e-Tool (CIeT) :")

st.header("Tank Retirement Thickness Calculator'")

# Input fields for Tank Calculator
diameter_ft = st.number_input("Tank Diameter (in feet)", value=40.0, step=1.0)
height_ft = st.number_input("Tank Height (in feet)", value=50.0, step=1.0)

# Advanced Settings
st.subheader("Tank dvanced Settings")
yield_strength = st.number_input("Yield Strength (MPa)", value=300.0, step=10.0)
tensile_strength = st.number_input("Tensile Strength (MPa)", value=540.0, step=10.0)
joint_efficiency = st.number_input("Joint Efficiency", value=0.9, step=0.1)
minimum_plate_thickness_m = st.number_input("Minimum Plate Thickness (m)", value=0.0032, step=0.0001)
density_water = st.number_input("Density of Water (kg/m³)", value=1000, step=10)
gravity = st.number_input("Gravity (m/s²)", value=9)

# Calculate and display retired thicknesses
#bottom_thickness_mm, shell_body_thickness_mm, top_thickness_mm, retired_thicknesses_mm = calculate_tank_thickness(diameter_ft, height_ft, yield_strength, tensile_strength, joint_efficiency, minimum_plate_thickness_m, density_water, gravity)
#st.write("Retired Shell Thickness:", retired_thicknesses_mm, "mm")
#st.write("Retired Bottom Plate Thickness:", bottom_thickness_mm, "mm")
#st.write("Retired Roof Plate Thickness:", top_thickness_mm, "mm")
# Get input values with default values pre-filled

# Perform calculation only when the button is clicked
if st.button("Calculate"):
  bottom_thickness_mm, shell_body_thickness_mm, top_thickness_mm= calculate_tank_thickness(diameter_ft, height_ft, yield_strength, tensile_strength, joint_efficiency, minimum_plate_thickness_m, density_water, gravity)

  st.write("## Retired Bottom Plate Thickness:", round(bottom_thickness_mm,2), "mm")
  st.write("## Retired Shell Plate Thickness:", round(shell_body_thickness_mm,2), "mm")
  st.write("## Retired Roof Plate Thickness:", round(top_thickness_mm,2), "mm")
  
  
st.title(imo)
