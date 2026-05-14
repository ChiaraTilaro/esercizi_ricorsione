def quicksort(sequenza):
    if len(sequenza) <=1:
        return sequenza
    else:
        # scelta pivot
        pivot = sequenza[0]
        #dividere sequenza secondo pivot
        sequenza_smaller = []
        sequenza_pivot = []
        sequenza_larger = []
        for i in sequenza:
            # il numero è minore di pivot
            if i < pivot:
                sequenza_smaller.append(i)
            # il numero è uguale al pivot
            elif i == pivot:
                sequenza_pivot.append(i)
            # il numero è maggiore del pivot
            else:
                sequenza_larger.append(i)

        #sequenza_smaller = [n for n in sequenza if n < pivot]
       # sequenza_pivot = [n for n in sequenza if n == pivot]
        #sequenza_larger = [n for n in sequenza if n >=pivot]
        return quicksort(sequenza_smaller) + sequenza_pivot + quicksort(sequenza_larger)



if __name__ == "__main__":
    sequenza = [9 , 3 ,2 , 6 ,8  , 5 , 199]
    print(quicksort(sequenza))
