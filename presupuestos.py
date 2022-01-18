from typing import Any
import utils
from pandas import DataFrame
from pandas.core.series import Series, Dtype

creditos_columnas = [
    "credito_presupuestado",
    "credito_vigente",
    "credito_comprometido",
    "credito_devengado",
    "credito_pagado"
]


def calcularSumaCreditos(presupuesto: DataFrame) -> Series:
    utils.sanitizeDecimals(presupuesto, creditos_columnas)
    creditos = presupuesto[creditos_columnas].sum()
    return creditos


identificador = tuple[str, str]
"""
a travez de una tupla se identifica un año, y el archivo con el presupuesto de dicho año, a travez de este identificador pueden generarse varias tablas que identifican varios creditos con un ejercicio presupuestario determinado 
"""


def sanitizarIdentificador(value) -> identificador:
    value: tuple[str, Any]= utils.sanitizeKeyValueTouple(value)
    key = utils.sanitizeStr(value[0])
    index = utils.sanitizeStr(value[1])
    return (key, index)

def sanitizarVariosIdentificadores(value)->identificador:
    value 

# def sumaHitorica(index: tuple[str, str]):
