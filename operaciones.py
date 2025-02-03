def realizar_operacion(expresion):
    try:
        resultado = eval(expresion)
        return resultado
    except Exception as e:
        raise ValueError("Expresión no válida")
