# Modifying a List without a function 

# Designs that need to be printed 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate each design until none it left 
# Move each desing into completed_models after printing 

while unprinted_designs:
    current_designs = unprinted_designs.pop() #pop() will remove the last item in the list 
