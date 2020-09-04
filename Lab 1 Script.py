'''
Name: Gloria Pappalardo
Date created: 9/3/2020
Version of Python you are using: 3.6
In this assignment I found the water runoff in gallons of a plot of land in Kenya. The input is the area in square feet
and the amount of rainfall in inches and the output is the amount of runoff in gallons.
'''
# These variables describe the study area of the plot of land in Kenya in feet.
plot_length = 50
plot_width = 20
plot_area = plot_length * plot_width
# Area in inches
plot_area_inches = plot_area * 144
# Amount of rainfall in inches
rainfall_inches = 1
# Amount of run off in cubic inches
runoff_inches = plot_area_inches * rainfall_inches
# Amount of run off in gallons
runoff_gallons = runoff_inches / 231
# Print to check code
print(runoff_gallons)

# Print of the run off information. The runoff in gallons to the hundredths place
# is 623.38 gallons.
print('plot_length is:', plot_length, 'feet')
print('plot_width is:', plot_width, 'feet')
print('rainfall_inches is:', rainfall_inches, 'inch')
# Print rounded to nearest hundredths
print('runoff_gallons is:', round(runoff_gallons, 2), 'gallons')