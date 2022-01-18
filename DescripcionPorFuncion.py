from numpy import int64
from pandas.core.frame import DataFrame
from utils import concat, sanitizeInt64, sanitizeStr

class DescripcionFuncion:
    """
    Describe una funcion en el presupuesto, con el identificador del ejercicio presupuestario, la finalidad, la función y una descripción simple
    """
    ejercicio_presupuestario: int
    finalidad_id: int64
    funcion_id: int64
    descripcion: str


def generarIdentificadorUniversal(DescFunc: DescripcionFuncion) -> str:
    """
    Genera un string que contiene <<ejercicio_presupuestario>>.<<finalidad_id>>.<<funcion_id>>
    """
    ep = DescFunc.ejercicio_presupuestario
    fin = DescFunc.finalidad_id
    fun = DescFunc.funcion_id
    return concat([str(ep), str(fin), str(fun)])


def generarCodigoFinalidadFuncion(DescFunc: DescripcionFuncion) -> str:
    """
    Genera un string que contiene <<finalidad_id>>.<<funcion_id>>
    """
    fin = DescFunc.finalidad_id
    fun = DescFunc.funcion_id
    return concat([str(fin), str(fun)])


def extraerDescripcion(dataFrame: DataFrame) -> DescripcionFuncion:
    """
    Extrae la información de ejercicio_presupuestario, finalidad_id, funcion_id
    y funcion_desc para crear un objecto DescripcionFuncion
    """

    indexValues = dataFrame.index.values
    if (len(indexValues) > 1):
        raise ValueError("you passed a data frame with more than one row")
    loc = indexValues[0]

    row = dataFrame.loc[loc]
    ep = row.at["ejercicio_presupuestario"]
    fin_id = sanitizeInt64(row.at["finalidad_id"])
    fun_id = sanitizeInt64(row.at["funcion_id"])
    desc = sanitizeStr(row.at["funcion_desc"])

    funcion = DescripcionFuncion()
    funcion.ejercicio_presupuestario = ep
    funcion.finalidad_id = fin_id
    funcion.funcion_id = fun_id
    funcion.descripcion = desc

    return funcion
