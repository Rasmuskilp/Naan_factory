from naan_factory_functions import *
print('Welcome to the Naan factory')
produce1 = input('what is the first produce?')
produce2 = input('second produce?')
output1 = make_dough(produce1,produce2)
final_output = bake_dough(output1)
print('well done! You make some:',final_output)