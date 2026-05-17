class NRegine:
    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
    # ================================APPROCCIO 2=============================================
    # rappresentiamo soluzione come un vettore di n regine ognungo rappresentante una regina come riga e colonna
    def solve2(self , N):
        self.ricorsione2([] , N)


    #parziale è un vettore di coppie (riga, colonna)
    def ricorsione2(self , parziale , N ):
        self.n_chiamate += 1
        # ho messo n regine
        if len(parziale) == N:
            if self.is_soluzione(parziale):
                self.n_soluzioni += 1
                print(parziale)
        # ho messo meno di n regine
        else:
            for riga in range(N):
                for col in range(N):
                    nuova_regina = [riga , col]
                    # verifico se la nuova regina sia ammissibile
                    if self.step_is_valid(nuova_regina , parziale):
                        # aggiungi questo pezzo di soluzione in parziale
                        parziale.append(nuova_regina)
                        #amdare avanti con la ricorsione
                        self.ricorsione2(parziale , N)
                        # backtraking
                        parziale.pop()

    def step_is_valid(self, nuova_regina , parziale):
        for regina in parziale:
            if not self.is_pair_admissible(nuova_regina , regina):
                return False
        return True


    def is_pair_admissible(self , regina1 , regina2):
        # 1) verifico la riga
        if regina1[0] == regina2[0]:
            return False
        # 2) verifo la colonna
        if regina1[1] == regina2[1]:
            return False
        # 3) verifico diagolane 1
        # per fare questa verifica devo controllare che:
        # colonna di regina1 - riga di regina1 == colonna di regina2 - riga di regina2
        if regina1[0]-regina1[1] == regina2[0]-regina2[1]:
            return False
        # 4) verifico diagonale 2)
        # colonna di regina1 + riga di regina1 == colonna di regina2 + riga di regina2
        if regina1[0]+regina1[1] == regina2[0]+regina2[1]:
            return False
        # 5) ho passato tutti i controlli, return true
        return True

    def is_soluzione(self , soluzione_possibile):
        for i in range(len(soluzione_possibile)-1):
            for j in range(i+1 , len(soluzione_possibile)):
               if not  self.is_pair_admissible(soluzione_possibile[i] , soluzione_possibile[j]):
                   return False
        return True


if __name__ == "__main__":
    nreg = NRegine()
    nreg.solve2(4)
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate {nreg.n_chiamate}")
