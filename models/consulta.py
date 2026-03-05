class Consulta:
    
    def __init__(self, id, paciente_id, medico_id,horario):
        self.id = id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.horario = horario
        
    def to_dict(self):
        return self.__dict__