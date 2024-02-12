string = "oi tudo bem"
metode = "upper" #Pemite alterar o metodo para upper, lo , werstrip etc...
    
if hasattr(string,metode):
    print(getattr(string,metode)())
    print(f"É um metodo {string} é um {metode}")
else:
    print(f"Não é um metodo{metode}")