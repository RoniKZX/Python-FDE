def chunker(iterable, size):
    # Implement function here
    # Separa cuatro posiciones [A, B, C, D]
    for i in range(0, len(iterable), size):
        # Retorna del iterable, la iteracion
        # actual hasta 'size' posiciones
        # despues
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))