# input -> "sub(1,3)" output -> -2
# operations take only 2 params. commands may be nested.
# ie. add(sub(3,4), 1), sub(add(238943, 2343), add(1, sub(323, 43)))
import numpy as np


operators = ['add', 'sub', 'mul', 'div']
input_ = "add(10,2)"
#input_ = "add(sub(3,4),1)"
#input_ = "sub(add(238943, 2343), add(1, sub(323, 43)))"

# operator wont be a leaf. operands will be
map = {'add':'a',
       'sub': 's',
       'mul': 'm',
       'div': 'd'}

operator_map = {'a' : np.add,
                's' : np.subtract,
                'm' : np.multiply,
                'd' : np.divide}


for word, initial in map.items():
    input_ = input_.replace(word.lower(), initial)

#tokens = list(input_)
tokens = ['a', 's', '10', '9', '1']

# def remove_items(test_list, item):
#     res = [i for i in test_list if i != item]
#     return res
    
# tokens = remove_items(tokens, "(")
# tokens = remove_items(tokens, ")")
# tokens = remove_items(tokens, ",")

def evaluate(tmp, operator_index):

    operator = tmp[operator_index]
    left = tmp[operator_index + 1]
    right = tmp[operator_index + 2]

    if left.isdigit() and right.isdigit():
        operator = operator_map[operator]
        return operator(int(left), int(right))

    if not left.isdigit():
        left = evaluate(tmp, operator_index+1)
    if not right.isdigit():
        right = evaluate(tmp, operator_index+2)
    operator = operator_map[operator]
    print(operator)
    return operator(int(left), int(right))
        
print("Expression ", input_, " evaluated to: ", evaluate(tokens, 0))
        
