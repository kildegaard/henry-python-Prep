montañas = {'nombre': ['Everest', 'K2', 'Kanchenjunga', 'Lhotse', 'Makalu',
                       'Cho Oyu', 'Dhaulagiri', 'Manaslu', 'Nanga Parbat', 'Annapurna I'],
            'orden': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'cordillera': ['Himalaya', 'Karakórum', 'Himalaya', 'Himalaya', 'Himalaya', 'Himalaya', 'Himalaya', 'Himalaya', 'Karakórum', 'Himalaya'],
            'pais': ['Nepal', 'Pakistán', 'Nepal', 'Nepal', 'Nepal', 'Nepal', 'Nepal', 'Nepal',
                     'Pakistán', 'Nepal'],
            'altura': [8849, 8611, 8586, 8516, 8485, 8188, 8167, 8163, 8125, 8091]}


headers = [header for header in montañas.keys()]


def dict_a_lista(diccio):
    lista_inicial = list(diccio.values())
    lista_final = [[str(elem[i]) for elem in lista_inicial]
                   for i in range(len(diccio.values()))]
    return lista_final


def main():

    lista_magica = dict_a_lista(montañas)

    with open('clase09_ej3.csv', 'w', encoding='utf-8') as file:
        file.write((',').join(headers))
        file.write('\n')
        for linea in lista_magica:
            file.write((',').join(linea))
            file.write('\n')


if __name__ == '__main__':
    main()
