import math
an = int(input("Digite o valor do ângulo: "))
ang = math.radians(an)
sen = math.sin(ang)
cos = math.cos(ang)
tg = math.tan(ang)
print("O valor do cosseno de {}° é {:.2f}, o seno vale {:.2f} e a tangente {:.2f}".format(an,cos,sen,tg))
