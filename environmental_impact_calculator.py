import streamlit as st

# Title and Description
st.title("Environmental Impact Calculator")
st.write("Estimate your environmental impact based on daily activities and get actionable suggestions to reduce it. 🌍")

# User Inputs
st.header("Input Your Daily Habits")

# Driving Habits
miles_driven = st.slider("Miles driven daily (car)", min_value=0, max_value=200, value=10)
fuel_efficiency = st.number_input("Car's fuel efficiency (miles per gallon)", min_value=1.0, max_value=100.0, value=25.0)

# Energy Usage
electricity_usage = st.number_input("Electricity usage per day (kWh)", min_value=0.0, max_value=200.0, value=30.0)

# Water Consumption
water_usage = st.slider("Water usage per day (gallons)", min_value=0, max_value=500, value=100)

# Calculations
st.header("Your Environmental Impact")

# Driving emissions calculation
co2_per_gallon = 19.6  # Average CO2 produced per gallon of gasoline 
daily_gas_used = miles_driven / fuel_efficiency
daily_co2_emissions = daily_gas_used * co2_per_gallon

# Energy emissions calculation (average CO2 per kWh in the US)
co2_per_kwh = 0.92  # Average pounds of CO2 per kWh
daily_energy_emissions = electricity_usage * co2_per_kwh

# Display Results
st.subheader("Daily CO₂ Emissions (in pounds)")
st.write(f"Driving: {daily_co2_emissions:.2f} lbs")
st.write(f"Electricity: {daily_energy_emissions:.2f} lbs")
st.write(f"Total: {daily_co2_emissions + daily_energy_emissions:.2f} lbs")

# Water usage feedback
st.subheader("Water Usage")
if water_usage > 100:
    st.write("Your water usage is higher than average. Consider water-saving tips like shorter showers or fixing leaks.")
else:
    st.write("Great! Your water usage is within the average range.")

# Suggestions
st.header("Suggestions to Reduce Your Impact")
st.write("- Consider carpooling or using public transport to reduce driving emissions.")
st.write("- Switch to energy-efficient appliances or use renewable energy sources.")
st.write("- Reduce water usage by installing low-flow fixtures and being mindful of water waste.")

# Footer
st.write("🌱 Small steps lead to big changes. Thank you for caring about the planet!")

#python3 -m streamlit run environmental_impact_calculator.py