from naan_factory_functions import *
#Tests go here for separation of concerns
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
