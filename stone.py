def is_even(n):
    if n == 0 :
        return True
    else :
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else :
        return is_even(n-1)
    
def a_play(n):
        if n == 0:
            print("Bob wins!")
        else:
            b_play(n-1)

def b_play(n):
    if n == 0 :
        print("a win")
    elif is_even(n) :
        return a_play(n-2)
    else  :
        return a_play(n-1)


a_play(20)