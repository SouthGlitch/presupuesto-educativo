from numpy import int64
from pandas import DataFrame, Period
from pandas.core.groupby import DataFrameGroupBy
from typing import Any

def createsTimePeriod(*args: list[str]) -> list[Period]:
    times = []
    for date in args:
        times.append(Period(date, freq="Y"))
    return times

def decimalARtoUSA(value: Any):
    stringDecimal = sanitizeStr(value)
    return stringDecimal.replace(',', '.')


def sanitizeDecimals(df: DataFrame, columns: list[str]):
    for column in columns:
        df[column] = df[column].apply(lambda x: float(decimalARtoUSA(x)))


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
    value: tuple[str, Any] = sanitizeKeyValueTouple(value)


    index = sanitizeInt64(value[0])
    desc = sanitizeStr(value[1])
    return (int(index), desc)


def concat(values: list[str], separator: str = ".") -> str:
    """
    Takes a list of strings and concatenates it to form one unique string,
    uses separator to define which character (or string) is between each workd
    """
    res = ""
    for value in values:
        res = res + value + separator
    return res[:-1]


def sanitizeStr(value) -> str:
    """
    Asserts that the value is a string and returns it, if not just throw
    """
    if (isinstance(value, str)):
        return value
    raise TypeError("value isn't a valid string")


def sanitizeInt64(value) -> int64:
    """
    Asserts that the value is a string and returns it, if not just throw
    """
    if (isinstance(value, int64)):
        return value
    raise TypeError(f"value isn't a valid int\nvalue:{type(value)}")


def sanitizeKeyValueTouple(value) -> tuple[str, Any]:
    value = sanitizeTouple(value)
    if (len(value) > 2):
        raise TypeError(
            f"a key value tuple can't have more than two elements\n{str(value)}")


def sanitizeTouple(value) -> tuple:
    if(isinstance(value, tuple)):
        return value
    raise TypeError(f"value isn't a valid tuple\nvalue:{type(value)}")
