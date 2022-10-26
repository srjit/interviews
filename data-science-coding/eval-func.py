def evaluate(tmp):

    for index, element in enumerate(tmp):
        if element in ['a', 's', 'm', 'd']:

            operator = operator_map[element]

            operand_l = tmp[2*index+1]
            operand_r = tmp[2*index+2]

            if operand_l.isdigit() and operand_r.isdigit():
                return operator(int(operand_l), int(operand_r))
            
            elif operand_l.isdigit():
                operand_r = evaluate(tmp[2*index+1:])
                return operator(int(operand_l), int(operand_r))
            
            elif operand_r.isdigit():
                ipdb.set_trace()
                operand_l = evaluate(tmp[2*index+2:])
                return operator(int(operand_l), int(operand_r))
            
            else:
                operand_l = evaluate(tmp[(2*index+1):])
                operand_r = evaluate(tmp[(2*index+2):])
                
                return operator(int(operand_l), int(operand_r))
        
