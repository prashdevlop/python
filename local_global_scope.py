def spam():
    eggs = 99
    bacon()
    print(eggs)
    print(ham)
def bacon():
    global ham
    hat = 20
    ham = 101
    eggs = 0
    print(hat)
spam()
ham = 201
print(ham)
bacon()
