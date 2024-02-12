def generator(num_primeiro = 0, maximum_primeiro = 1000):
    while(True):
        yield num_primeiro
        num_primeiro+=1
        if num_primeiro >= maximum_primeiro:
            return
gen = generator(maximum_primeiro=10) # altere o numero maximo 
for i in gen:
    print(i)
    