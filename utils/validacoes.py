import re
from datetime import datetime


def validar_texto_vazio(valor: str, campo: str):
    if not valor or valor.strip() == "":
        raise ValueError(f"{campo} não pode estar vazio")


def validar_cpf(cpf: str):
    """
    Validação simples de CPF (formato).
    Ex: 12345678900
    """
    if not re.fullmatch(r"\d{11}", cpf):
        raise ValueError("CPF deve conter 11 números")


def validar_horario(horario: str):
    """
    Formato esperado: YYYY-MM-DD HH:MM
    """
    try:
        datetime.strptime(horario, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError(
            "Horário inválido. Use formato YYYY-MM-DD HH:MM"
        )


def validar_numero_positivo(valor: int, campo: str):
    if valor <= 0:
        raise ValueError(f"{campo} deve ser maior que zero")