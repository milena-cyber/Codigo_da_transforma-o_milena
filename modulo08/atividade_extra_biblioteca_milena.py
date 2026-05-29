class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Biblioteca:

    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado!')

    def listar_livros(self):

        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")

        else:
            print(f"\n=== Biblioteca {self.nome} ===")

            for livro in self.livros:
                print(livro)


# Teste
biblioteca = Biblioteca("Biblioteca Central")

livro1 = Livro("Percy Jackson", "Rick Riordan")
livro2 = Livro("Quarta Asa", "Rebecca Yarros")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()