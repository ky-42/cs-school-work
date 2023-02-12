##
# Calculates how long it will take in years for moonlands population
# to exceed the population of sunland
##

# Gets the population of sun and moon land
sunland_pop = float(input('Please enter the population of Sunland in millions: '))
moonland_pop = float(input('Please enter the population of Moonland in millions: '))


# Calculates new populations year by year until moons population passes suns
years = 0
while sunland_pop >= moonland_pop:
    sunland_pop *= 1.01
    moonland_pop *= 1.2
    years += 1

print(
    'It will take %i years for the population of Moonland to exceed the population of Sunland.'
    % years
)