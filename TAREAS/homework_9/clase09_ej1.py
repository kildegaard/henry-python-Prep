import sys


def main(argumentos):
    if len(argumentos) != 3:
        raise SystemExit(
            'ERROR: se necesitan exactamente 3 argumentos para poder avanzar')
    for idx, arg in enumerate(argumentos, start=1):
        print(f'Argumento {idx}: {arg}')


if __name__ == '__main__':
    main(sys.argv[1:])
