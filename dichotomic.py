def dichotmic(input_list , val):
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        index = len(input_list) //2
        return dichotmic(input_list[:index] , val) or dichotmic(input_list[index :] , val)

if __name__ == "__main__":
    sequenza = [1 ,2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
    print(dichotmic(sequenza , 4))
    print(dichotmic(sequenza , 11))
