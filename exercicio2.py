
port = int(input("Insira a porta do user"))

if port == 80:
    print("porta HTTP detectada")
elif port == 443:
    print("porta HTTPS detectada")
else:
    print("sei lá que djabo é isso")