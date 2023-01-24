import sys
import datetime as dt


def armar_string(timestamp, temp, hum, lluvia):
    lista_a_grabar = [str(timestamp), temp, hum, lluvia]
    texto = ','.join(lista_a_grabar)
    return texto


def grabar_a_archivo(path, argumentos):
    temp, hum, has_rained = argumentos

    date = dt.datetime.now()

    with open(path, 'a', encoding='utf-8') as file:
        file.write(armar_string(date, temp, hum, has_rained))
        file.write('\n')


def main(argumentos):
    if len(argumentos) != 3:
        raise SystemExit('ERROR: mal ingresados los argumentos')

    path = 'clase09_ej2.csv'
    grabar_a_archivo(path, argumentos)


if __name__ == '__main__':
    main(sys.argv[1:])
