c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9

#Read in a floating-point number from the user
mass_kg = float(input())

#Compute E = mc^2.
energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
print('Total energy released:', energy_joules, 'Joules')

#Calculate equivalent number of AA and tons of TNT.
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_tons = energy_joules / joules_per_TNT_ton

print('Which is as much energy as:')
print('  ', num_AA_batteries, 'AA batteries')
print('  ', num_TNT_tons, 'tons of TNT')

# From Zybooks
# 
# 
# Albert Einstein's equation E = mc2 is likely the most widely known mathematical formula. The equation describes the mass-energy equivalence, which states that the mass (amount of matter) m of a body is directly related to the amount of energy E of the body, connected via a constant value c2, the speed of light squared. The significance of the equation is that matter can be converted to energy, (and theoretically, energy back to matter). The mass-energy equivalence equation can be used to calculate the energy released in nuclear reactions, such as nuclear fission or nuclear fusion, which form the basis of modern technologies like nuclear weapons and nuclear power plants.
# 
# The following program reads in a mass in kilograms and prints the amount of energy stored in the mass. Also printed is the equivalent numbers of AA batteries and tons of TNT.