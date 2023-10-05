n = int(input())
peliculas_vistas = 0
tiempo_actual = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a >= tiempo_actual:
        peliculas_vistas += 1
        tiempo_actual = b
print(peliculas_vistas)