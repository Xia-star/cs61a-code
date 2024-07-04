empty = 'empty'

def is_linklist(s):
    # if (len(s) == 2 and is_linklist(s[1])) or s == empty :
    #     return True
    # else :
    #     return False
    return s == empty or (len(s) == 2 and is_linklist(s[1]))


def linklist(first,rest):
    assert is_linklist(rest),"rest 必须是一个链表"
    return [first,rest]

def first(s):
    assert is_linklist(s),"must be a linklist"
    assert s != empty ,"if s is empty, s not have first item"
    return s[0]

def rest(s):
    assert is_linklist(s),"must be a linklist"
    assert s != empty ,"if s is empty, s not have rest item"
    return s[1]
four = linklist(4,linklist(3,linklist(2,linklist(1,linklist(0,empty)))))

def len_link(s):
    length = 0
    while s != empty:
        s ,length = rest(s) , length + 1
    return length

def get_link(s,k):
    i = 0
    while i < k:
        s = rest(s)
        i = i + 1
    return first(s)

def len_link_recursive(s):
    if s == empty:
        return 0
    else:
        return 1 + len_link_recursive(rest(s))

def get_link_recursive(s,k):
    if k == 0:
        return first(s)
    else:
        return get_link(rest(s), k-1)

def extend_link(s,t):
    assert is_linklist(s) and is_linklist(t)
    if s == empty:
        return t
    else:
        return linklist(first(s),extend_link(rest(s),t))

def apply_to_all_linklist(mk_fun,s):
    assert is_linklist(s),"s must be linklist"
    if s == empty:
        return s
    return linklist(mk_fun(first(s)),apply_to_all_linklist(mk_fun,rest(s)))

def keep_if_link(sel_fun,s):
    assert is_linklist(s),"s must be linklist"
    if s ==empty:
        return s
    else:
        if sel_fun(first(s)) :
            return linklist(s,keep_if_link(sel_fun,rest(s)))
        else:
            return keep_if_link(sel_fun,rest(s))

def join_link(s,separator):
    assert is_linklist(s),"s must be a linklist"
    if s == empty:
        return ""
    
    else:
        return str(first(s)) + separator+ join_link(rest(s),separator )

print(four)
print(len_link(four))
print(get_link(four,1))
print(len_link_recursive(four))
print(get_link_recursive(four,1))
print(join_link(four,", "))


