#Basis of a test
#Having controlled inputs for known outputs
    #and testing for these
# #Make test for make_dough
# #to make dough it will take in 'water' and 'flour'
# inputs = 'water' and 'flour'
# outputs = 'dough'
def make_dough(ing_1,ing_2):
    pass
def bake_dough(arg1):
    pass
print("Testing make_dough with 'water' and 'flour'. Expected -->'dough'")
print(make_dough('water','flour') == 'dough')
print('got:',make_dough('water','flour'))
#Make test for bake_dough
print("Testing bake_dough, with 'dough'. Expected --> 'Naan'")
#then with the dough should be able to put it to even and get out Naan
print(bake_dough('dough') == 'Naan')
print('got:',bake_dough('dough'))
