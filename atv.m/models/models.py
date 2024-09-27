
class Personagens:
    def __init__(self, id, nome, especie, arma, EstadoAtual):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.arma = arma
        self.EstadoAtual = EstadoAtual


personagens = []


novo_personagem = Personagens(1, "Dean", "Humano", "Espada de Caim", "Morto")
personagens.append(novo_personagem)
