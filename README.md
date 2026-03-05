# Hospital Scheduling System (Python)

Projeto simples de **sistema de agendamento hospitalar** desenvolvido em **Python puro**, com foco em **aprendizado de arquitetura de software, organização de código e boas práticas de desenvolvimento**.

Este projeto começou como uma implementação simples usando **JSON como persistência de dados**, mas será **evoluído gradualmente** para se aproximar de arquiteturas utilizadas no mercado.

O objetivo é transformar este projeto em um **sistema mais maduro**, aplicando conceitos como:

* Clean Code
* Arquitetura em camadas
* Boas práticas de Python
* Separação de responsabilidades
* Testes automatizados
* Persistência de dados mais robusta

---

# Objetivo do Projeto

O objetivo principal é construir um sistema de agendamento que permita:

* cadastrar pacientes
* cadastrar médicos
* agendar consultas
* verificar conflitos de horário
* organizar dados de forma estruturada

Ao longo do desenvolvimento o projeto será evoluído para incluir conceitos utilizados em projetos profissionais.

---

# Arquitetura Atual

O projeto já segue uma **estrutura modular**, separando responsabilidades em diferentes camadas.

```
hospital_agendamento/
│
├── main.py
│
├── data/
│   └── banco.json
│
├── models/
│   ├── paciente.py
│   ├── medico.py
│   └── consulta.py
│
├── services/
│   └── agendamento_service.py
│
├── repositories/
│   └── database.py
│
└── utils/
    └── validacoes.py
```

### Camadas

**models**

* Representação das entidades do sistema.

**services**

* Regras de negócio.

**repositories**

* Camada de acesso aos dados.

**utils**

* Funções auxiliares e validações.

---

# Tecnologias Utilizadas

* Python 3
* JSON (persistência simples de dados)
* Estrutura modular de projeto

---

# Como executar o projeto

Clone o repositório:

```bash
git git clone https://github.com/EdBispoDev/hospital-appointment-system.git
```

Entre na pasta do projeto:

```bash
cd hospital_agendamento
```

Execute o sistema:

```bash
python3 main.py
```

---

# Persistência de Dados

Atualmente o sistema utiliza um arquivo JSON simples:

```
data/banco.json
```

Isso permite focar inicialmente na **arquitetura e lógica do sistema**.

No futuro esse mecanismo poderá ser substituído por:

* SQLite
* PostgreSQL
* ORM

---

# Evoluções Futuras

O projeto será evoluído gradualmente para incluir:

* CLI interativa
* tratamento de exceções
* logging
* testes automatizados
* banco de dados real
* API REST
* containerização com Docker
* princípios de Clean Architecture

---

# Motivação

Este projeto faz parte de um processo de aprendizado focado em:

* Engenharia de software
* Estruturação de projetos Python
* Evolução de código simples para arquiteturas mais maduras

A ideia é começar **simples**, mas evoluir o sistema seguindo práticas utilizadas em projetos profissionais.

---

# Autor

Desenvolvido por **Edinaldo Bispo**

