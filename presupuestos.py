from typing import Any
import utils
from pandas import DataFrame
from pandas.core.groupby import DataFrameGroupBy
from pandas.core.series import Series, Dtype

creditos_columnas = [
    "credito_presupuestado",
    "credito_vigente",
    "credito_comprometido",
    "credito_devengado",
    "credito_pagado"
]

# =========================
# * REQUEST PRESUPUESTO API
# =========================



# =============================
# * UTILIDADES PRESUPUESTARIAS
# =============================

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

# def sanitizarVariosIdentificadores(value)->identificador:
#     value 

def construirIdDescDic(group: DataFrameGroupBy) -> dict[int, str]:
    """
    Construye un diccionario dónde cada clave es el identificador y su valor un string
    conteniendo una descripción
    """
    dic: dict[int, str] = {}
    for raw_id_desc in group:
        id, desc = sanitizarIdDescTouple(raw_id_desc)
        if (dic.get(id) is not None):
            raise TypeError("hay más de un valor posible para este diccionario, " +
                            "es decir que hay más de una descripción posible para este id")
        dic[id] = desc

    return dic


def sanitizarIdDescTouple(value: Any) -> tuple[int, str]:
    value: tuple[str, Any] = utils.sanitizeKeyValueTouple(value)


    index = utils.sanitizeInt64(value[0])
    desc = utils.sanitizeStr(value[1])
    return (int(index), desc)
