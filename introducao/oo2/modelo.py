class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme("Vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao}'
      f'- Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} '
      f'- Likes: {atlanta.likes}')