from repositories.database import carregar, salvar
from models.consulta import Consulta


def agendar_consulta(paciente_id, medico_id, horario):

    banco = carregar()

    # verificar paciente
    if not any(p["id"] == paciente_id for p in banco["pacientes"]):
        print("Paciente não encontrado")
        return

    # verificar medico
    if not any(m["id"] == medico_id for m in banco["medicos"]):
        print("Médico não encontrado")
        return

    # verificar conflito de horario
    for c in banco["consultas"]:
        if c["medico_id"] == medico_id and c["horario"] == horario:
            print("Médico já possui consulta nesse horário")
            return

    nova = Consulta(
        id=len(banco["consultas"]) + 1,
        paciente_id=paciente_id,
        medico_id=medico_id,
        horario=horario
    )

    banco["consultas"].append(nova.to_dict())
    salvar(banco)

    print("Consulta agendada com sucesso")