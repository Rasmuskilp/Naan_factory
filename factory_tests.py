#Basis of a test
#Having controlled inputs for known outputs
    #and testing for these
# #Make test for make_dough
# #to make dough it will take in 'water' and 'flour'
# inputs = 'water' and 'flour'
# outputs = 'dough'
def make_dough(ing_1,ing_2):
    if ing_1 != 'water' and ing_2 != 'water':
        return 'not dough'
    elif ing_1 != 'flour' and ing_2 != 'flour':
        return 'not dough'
    elif 'water' in [ing_1,ing_2] and 'flour' in [ing_1,ing_2]:
        return 'dough'
#return 'dough'
def bake_dough(arg1):
    if arg1 == 'dough':
        return 'Naan'
    else:
        return 'not Naan'
print("Testing make_dough with 'water' and 'flour'. Expected -->'dough'")
print(make_dough('water','flour') == 'dough')
print('got:',make_dough('water','flour'))
print(make_dough('concrete','water') == 'not dough')
print("Testing make_dough with 'concrete' and 'flour'. Expected -->'not dough'")
print('got:',make_dough('concrete','flour'))
print(make_dough('flower','carrot') == 'not dough')
#When I pass in cement wand water, or anything else... I should get : 'not dough'
#Make test for bake_dough
print("Testing bake_dough, with 'dough'. Expected --> 'Naan'")
#then with the dough should be able to put it to even and get out Naan
print(bake_dough('dough') == 'Naan')
print('got:',bake_dough('dough'))
#when bake_dough is passed something other than dough, it should output 'not Naan'
print(bake_dough('chicken') == 'not Naan')
print("Testing bake_dough, with 'dough'. Expected --> 'not Naan'")
print('got:',bake_dough('chicken'))
print(bake_dough('wood') == 'not Naan')

