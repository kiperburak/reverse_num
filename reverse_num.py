def func(n):
    if len(n) == 0 :
        return ""
    last_str = n[len(n)-1] + ", "
    n = n[0:len(n)-1]  
    return last_str + func(n)
n="390626"
print(func(n))