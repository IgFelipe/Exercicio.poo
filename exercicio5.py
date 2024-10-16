class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula

    def mostrar_info(self):
        print(f'Nome: {self.nome}, Matrícula: {self.matricula}')


class Curso:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f'Alunos matriculados no curso {self.nome} ({self.codigo}):')
        for aluno in self.alunos:
            aluno.mostrar_info()


class Escola:
    def __init__(self, nome: str):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso: Curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f'Cursos oferecidos pela escola {self.nome}:')
        for curso in self.cursos:
            print(f'Curso: {curso.nome} ({curso.codigo})')
            curso.mostrar_alunos()


aluno1 = Aluno("Alice", "2021001")
aluno2 = Aluno("Bob", "2021002")
aluno3 = Aluno("Carol", "2021003")


curso1 = Curso("Engenharia de Software", "ES101")
curso2 = Curso("Data Science", "DS202")


curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)
curso2.adicionar_aluno(aluno3)


escola = Escola("Escola de Tecnologia")
escola.adicionar_curso(curso1)
escola.adicionar_curso(curso2)


escola.mostrar_cursos()


aluno4 = Aluno("David", "2021004")
curso2.adicionar_aluno(aluno4)

curso3 = Curso("Inteligência Artificial", "IA303")
escola.adicionar_curso(curso3)

print("\nApós adicionar um novo aluno e curso:")
escola.mostrar_cursos()
