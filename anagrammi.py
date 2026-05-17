import copy


def anagrammi(parola):
    soluzioni = []
    ricorsione([] , parola , soluzioni)
    return soluzioni

def ricorsione(parziale, rimanenti , soluzioni):
    if len(rimanenti) ==0:
        soluzioni.append(copy.deepcopy(parziale))
    else:
        for i in range(len(rimanenti)):
            parziale.append(rimanenti[i])
            nuovi_rimanenti = rimanenti[:i]+rimanenti[i+1:]
            ricorsione(parziale , nuovi_rimanenti , soluzioni)
            parziale.pop()


def anagrammi_set(parola):
    soluzioni = []
    ricorsione_set("" , parola , soluzioni)
    return soluzioni

def ricorsione_set(parziale, rimanenti , soluzioni):
    if len(rimanenti) ==0:
        soluzioni.append(copy.deepcopy(parziale))
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i]+rimanenti[i+1:]
            ricorsione_set(parziale+rimanenti[i] , nuovi_rimanenti , soluzioni)


if __name__ == "__main__":
    print(anagrammi('dog'))
    print(anagrammi_set('casa'))
