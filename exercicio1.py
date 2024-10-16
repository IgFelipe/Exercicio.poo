class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def info(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f'{self.titulo} - {self.autor} - {status}'


class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    return f'O livro "{titulo}" foi emprestado.'
                return f'O livro "{titulo}" não está disponível.'
        return f'O livro "{titulo}" não foi encontrado.'

    def mostrar_inventario(self):
        return '\n'.join(livro.info() for livro in self.livros)


livraria = Livraria()
livraria.adicionar_livro("1984", "George Orwell")
livraria.adicionar_livro("O Senhor dos Anéis", "J.R.R.")

print(livraria.mostrar_inventario())
print(livraria.emprestar_livro("1984"))
print(livraria.mostrar_inventario())
