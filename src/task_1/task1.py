from Dictionary import *

def main():
    d = Dictionary()

    d.newentry('Apple', 'A fruit that grows on trees')

    print(d.look('Apple'))
    print(d.look('Banana'))


if __name__ == '__main__':
    main()