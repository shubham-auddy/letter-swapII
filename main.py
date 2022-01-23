# Letter Swap II - e021Rt-Sj6d -> E021rT-sJ6D

import string


def swap_letter(str):
    op=''
    for i in str:
        if i in string.ascii_lowercase[:26]:
            op = op + i.upper()
        elif i in string.ascii_uppercase[:26]:
            op = op + i.lower()
        else :
            op = op + i

    return op 

def main():
    param = input("Input your custom string here : ")
    result = swap_letter(param)
    print(f'{param} -> {result}')

if __name__ == "__main__":
    main()