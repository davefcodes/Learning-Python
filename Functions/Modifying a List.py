# Modifying a List without a function 

# Designs that need to be printed 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = [] 

print(unprinted_designs)

# Simulate each design until none it left 
# Move each desing into completed_models after printing 

while unprinted_designs:
    current_designs = unprinted_designs.pop() #pop() will remove the last item in the list 

    print(f"Printing model: {current_designs}")
    completed_models.append(current_designs) #append() will add the items into our completed_models

# Display the completed_models
print("\nThe following models have been completed: ")

for model in completed_models: # loop through the completed models and print it 
    print(model)




