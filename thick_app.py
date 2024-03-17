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

    t_retired = (pressure_MPa * diameter_mm) / (2 * S * E * W + 2 * pressure_MPa * Y) * F + C_retired
    t_retired = max(t_retired, 2.8)  # Ensure minimum thickness is 2.5 mm
    t_retired = math.ceil(t_retired * 10) / 10

    return t, t_retired

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

    # Calculate retired thickness for each shell course
    num_shell_courses = st.sidebar.number_input("Total Number of Shell Courses", value=1, step=1)
    average_height_per_course = st.sidebar.number_input("Average Height of Shell Courses (in meters)", value=2.0, step=0.1)

    retired_thicknesses_mm = []
    for _ in range(num_shell_courses):
        retired_thickness_mm = calculate_retired_thickness_per_course(diameter, average_height_per_course, yield_strength, tensile_strength, joint_efficiency, minimum_plate_thickness_m, density_water, gravity)
        retired_thicknesses_mm.append(retired_thickness_mm)

    return bottom_thickness_mm, shell_body_thickness_mm, top_thickness_mm, retired_thicknesses_mm

def calculate_retired_thickness_per_course(diameter, height, yield_strength, tensile_strength, joint_efficiency, minimum_plate_thickness_m, density_water, gravity):
    diameter_m = diameter / 1000
    height_m = height

    head_pressure = density_water * height_m * gravity / 1000

    retired_thickness_m = (head_pressure * diameter_m) / (yield_strength * joint_efficiency)
    retired_thickness_m = max(retired_thickness_m, minimum_plate_thickness_m)

    # Reduce thickness based on height
    reduction_factor = height_m / (2 * height)  # Assuming the average height is half of the total height
    retired_thickness_m *= reduction_factor

    return max(retired_thickness_m, minimum_plate_thickness_m) * 1000  # Ensure minimum thickness is 2.5 mm


def main():
    st.title("Corrosion Management Retired Thickness Calculator")

    option = st.sidebar.selectbox("Select Calculator", ["Piping Calculator", "Tank Thickness Calculator"])

    if option == "Piping Calculator":
        st.header("Piping Calculator")

        diameter_inch = st.sidebar.number_input("Pipe Diameter (in inches)", value=6.0, step=0.1)
        pressure_psi = st.sidebar.number_input("Pressure (in psi)", value=100.0, step=1.0)

        st.sidebar.subheader("Advanced Settings")
        S = st.sidebar.number_input("Allowable Stress (MPa)", value=138.0, step=1.0)
        E = st.sidebar.number_input("Longitudinal Weld Joint Efficiency", value=1.0, step=0.1)
        W = st.sidebar.number_input("Weld Strength Reduction Factor", value=1.0, step=0.1)
        Y = st.sidebar.number_input("Coefficient for Temperature and Material", value=0.4, step=0.1)
        C = st.sidebar.number_input("Corrosion Allowance (mm)", value=3.0, step=0.1)
        C_retired = st.sidebar.number_input("Corrosion Allowance for Retired Thickness (mm)", value=0.0, step=0.1)
        F = st.sidebar.number_input("Safety Factor for Retired Thickness", value=0.8, step=0.1)

        t, t_retired = piping_calculator(diameter_inch, pressure_psi, S, E, W, Y, C, C_retired, F)

        st.write("Required Thickness:", t, "mm")
        st.write("Retired Thickness:", t_retired, "mm")

    elif option == "Tank Thickness Calculator":
        st.header("Tank Thickness Calculator")

        diameter_ft = st.sidebar.number_input("Tank Diameter (in feet)", value=40.0, step=1.0)
        height_ft = st.sidebar.number_input("Tank Height (in feet)", value=50.0, step=1.0)

        yield_strength = st.sidebar.number_input("Yield Strength (MPa)", value=300.0, step=10.0)
        tensile_strength = st.sidebar.number_input("Tensile Strength (MPa)", value=540.0, step=10.0)
        joint_efficiency = st.sidebar.number_input("Joint Efficiency", value=0.9, step=0.1)
        minimum_plate_thickness_m = st.sidebar.number_input("Minimum Plate Thickness (m)", value=0.0032, step=0.0001)
        density_water = st.sidebar.number_input("Density of Water (kg/m³)", value=1000, step=10)
        gravity = st.sidebar.number_input("Gravity (m/s²)", value=9.81, step=0.1)

        #diameter_mm = diameter_ft * 304.8
        #height_mm = height_ft * 304.8
        
        diameter_mm = diameter_ft
        height_mm = height_ft
        
        
        
        

        bottom_thickness_mm, shell_body_thickness_mm, top_thickness_mm, retired_thicknesses_mm = calculate_tank_thickness(diameter_mm, height_mm, yield_strength, tensile_strength, joint_efficiency, minimum_plate_thickness_m, density_water, gravity)

        st.write("Bottom Retired Thickness:", round(bottom_thickness_mm,2), "mm")
        st.write("Shell Retired Body Thickness:", round(shell_body_thickness_mm,2), "mm")
        #st.write("Top Thickness:", top_thickness_mm, "mm")
        #st.write("Retired Thicknesses for Each Shell Course (mm):", retired_thicknesses_mm)

if __name__ == "__main__":
    main()
