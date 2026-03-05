from services.agendamento_service import agendar_consulta

def menu():
    while True:
        print("\n=== Hospital ===")
        print("1 - Agendar consulta")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            paciente = int(input("ID paciente: "))
            medico = int(input("ID médico: "))
            horario = input("Horário: ")

            agendar_consulta(paciente, medico, horario)

        elif op == "0":
            break


menu()