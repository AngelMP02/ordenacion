def contar_identificadores_unicos(n, identificadores):
    contador_unicos = 0
    for i in range(n):
        es_unico = True
        for j in range(i):
            if identificadores[i] == identificadores[j]:
                es_unico = False
                break
        if es_unico:
            contador_unicos += 1
    return contador_unicos
t = int(input())
for _ in range(t):
    n = int(input())
    identificadores = list(map(int, input().split()))
    resultado = contar_identificadores_unicos(n, identificadores)
    print(resultado)