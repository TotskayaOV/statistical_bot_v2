

def conversion_standard_timestamp(total_seconds: float) -> str:
    """
    преобразует метку времени в формат mm:ss
    :param total_seconds: float
    :return: str
    """
    min, sec = divmod(total_seconds * 60, 60)
    return ("00:%02d:%02d" % (min, sec))
