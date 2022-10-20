"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    #
    # Inserte su código aquí
    #

    df = open('clusters_report.txt', 'r')
    line1 = re.sub("\s{3,}", "  ", df.readline().strip()).split("  ")
    line2 = df.readline().replace("\n", "").strip().split("  ")

    for i in range(len(line1)):
        line1[i] = (line1[i].strip().lower()).replace(" ", "_")
        if i == 1 or i == 2:
            line1[i] = (line1[i] + ' ' + line2[i-1].lower()
                        ).replace(" ", "_")
    df.readline(), df.readline()
    doc = df.readlines()
    cont = []
    text = ''

    for line in doc:
        line = re.sub(r"\s{2,}", " ", line.strip()).replace('\n', '')
        line += ' '
        if '%' in line:
            if text != '':
                aux = cont.pop()
                text = text.replace('.', '').strip()
                aux[3] = aux[3] + text
                cont.append(aux)
                text = ''
            indice = line.index('%')
            l = line[:indice].strip().replace(',', '.').split(" ")
            cont.append(l + [line[indice + 2:]])
        else:
            text += line

    aux = cont.pop()
    text = text.replace('.', '').strip()
    aux[3] = aux[3] + text
    cont.append(aux)
    df = pd.DataFrame(cont, columns=line1)
    df['cluster'] = df['cluster'].astype('int64')
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(
        'int64')
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(
        'float64')

    return df
