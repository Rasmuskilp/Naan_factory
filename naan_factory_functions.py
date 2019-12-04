#here we run the factory (functions)
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
def run_factory(arg1,arg2):
    output = make_dough(arg1,arg2)
    output2 = bake_dough(output)
    return output2