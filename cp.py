#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:55:17 2024

@author: ziad oqifi
"""

import streamlit as st
import math

def piping_calculator(diameter_inch, pressure_psi, S, E, W, Y, C, C_retired, F):
  mm_per_inch = 25.4
  MPa_per_psi = 0.0689476

  diameter_mm = diameter_inch * mm_per_inch
  pressure_MPa = pressure_psi * MPa_per_psi

  t = (pressure_MPa * diameter_mm) / (2 * S * E * W + 2 * pressure_MPa * Y) + C
  t = max(t, 2.5)  # Ensure minimum thickness is 2.5 mm
  t = math.ceil(t * 10) / 10

  t_retired = (pressure_MPa * diameter_mm) / (2 * S * E * W + 2 * pressure_psi * Y) * F + C_retired
  t_retired = max(t_retired, 2.8)  # Ensure minimum thickness is 2.5 mm
  t_retired = math.ceil(t_retired * 10) / 10

  return t, t_retired

def piping_input():
  # Define default values
  default_diameter_inch = 6.0
  default_pressure_psi = 100.0
  default_S = 138.0
  default_E = 1.0
  default_W = 1.0
  default_Y = 0.4
  default_C = 3.0
  default_C_retired = 0.0
  default_F = 0.8

  # Use temporary variables to store input values
  diameter_inch = st.number_input("Pipe Diameter (in inches)", value=default_diameter_inch, step=1.5)
  pressure_psi = st.number_input("Pressure (in psi)", value=default_pressure_psi, step=1.0)
  st.write('')
  st.write('Advanced Features')
  S = st.number_input("Allowable Stress (MPa)", value=default_S, step=10.0)
  E = st.number_input("Longitudinal Weld Joint Efficiency", value=default_E, step=0.1)
  W = st.number_input("Weld Strength Reduction Factor", value=default_W, step=0.1)
  Y = st.number_input("Coefficient for Temperature and Material", value=default_Y, step=0.1)
  C = st.number_input("Corrosion Allowance (mm)", value=default_C, step=1.0)
  C_retired = st.number_input("Corrosion Allowance for Retired Thickness (mm)", value=default_C_retired, step=0.1)
  F = st.number_input("Safety Factor for Retired Thickness", value=default_F, step=0.1)

  return diameter_inch, pressure_psi, S, E, W, Y, C, C_retired, F

st.title("Corrosion Management Retired Thickness Calculator")

st.header("Piping Calculator")

# Get input values with default values pre-filled
diameter_inch, pressure_psi, S, E, W, Y, C, C_retired, F = piping_input()

# Perform calculation only when the button is clicked
if st.button("Calculate"):
  t, t_retired = piping_calculator(diameter_inch, pressure_psi, S, E, W, Y, C, C_retired, F)
  st.write("## Retired Thickness:", t_retired, "mm")
