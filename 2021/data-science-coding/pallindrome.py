


def check(s):

    l_ = list(s)
    is_pal = True
    for i, letter in enumerate(l_):

        if l_[i] != l_[len(l_) - 1 - i]:
            print("No")
            is_pal = False
            break;
        
    return is_pal
        

if(check("malayalam")):
    print("hiii")
check("malayalam1")
