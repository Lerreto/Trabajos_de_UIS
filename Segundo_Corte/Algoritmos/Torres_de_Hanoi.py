def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        print(altura, origen, destino, intermedio)
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(altura,origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)


def moverDisco(altura,desde,hacia):
    print("mover disco",altura,"de",desde,"a",hacia)

moverTorre(5,"A","B","C")