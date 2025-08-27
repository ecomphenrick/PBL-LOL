class Campeao:
    def __init__(self):
        self.nome = ""
        self.nivel = 0
        self.vida = 0
    
    def exibirStatus(self):
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida}")

    def receberDano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")


class Garen(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Garen"
        self.nivel = 1
        self.vida = 620
    
    def usarHabilidade(self):
        print("Garen usa Justiça Demacianal")

    def ataqueBasico(self, alvo):
        dano = 60  # Dano alto fixo
        print(f"Garen ataca {alvo.nome} causando {dano} de dano!")
        alvo.receberDano(dano)

class Jinx(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Jinx"
        self.nivel = 1
        self.vida = 540
    
    def usarHabilidade(self):
        print("Jinx usa Super Mega Míssil de Morte")

    def ataqueBasico(self, alvo):
        import random
        dano = 40
        critico = random.random() < 0.25  # 25% de chance de crítico
        if critico:
            dano *= 2
            print(f"Jinx acerta um CRÍTICO em {alvo.nome}! Dano: {dano}")
        else:
            print(f"Jinx ataca {alvo.nome} causando {dano} de dano.")
        alvo.receberDano(dano)

class Ahri(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Ahri"
        self.nivel = 1
        self.vida = 480
    
    def usarHabilidade(self):
        print("Ahri Lança Encanto")

    def ataqueBasico(self, alvo):
        dano = 35
        cura = 15
        print(f"Ahri ataca {alvo.nome} causando {dano} de dano e se cura em {cura}!")
        alvo.receberDano(dano)
        self.vida += cura
        print(f"Ahri vida atual: {self.vida}")


class Katarina(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Katarina"
        self.nivel = 1
        self.vida = 510
    
    def usarHabilidade(self):
        print("Katarina usa Lótus da Morte")


class Teemo(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Teemo"
        self.nivel = 1
        self.vida = 480
    
    def usarHabilidade(self):
        print("Teemo planta Armadilhas Venenosas")

    def ataqueBasico(self, alvo):
        dano = 30
        print(f"Teemo ataca {alvo.nome} causando {dano} de dano e envenena!")
        alvo.receberDano(dano)
        # Efeito de veneno: dano extra na próxima rodada
        if not hasattr(alvo, 'envenenado'):
            alvo.envenenado = 0
        alvo.envenenado += 15


class Morgana(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Morgana"
        self.nivel = 1
        self.vida = 500
    
    def usarHabilidade(self):
        print("Morgana usa Prisão das Trevas")

    def ataqueBasico(self, alvo):
        dano = 35
        print(f"Morgana ataca {alvo.nome} causando {dano} de dano e reduz ataque!")
        alvo.receberDano(dano)
        if not hasattr(alvo, 'ataqueReduzido'):
            alvo.ataqueReduzido = 0
        alvo.ataqueReduzido += 1




class Time:
    def __init__(self):
        self.listaCampeoes = []

    def adicionarCampeao (self, c = Campeao):
        self.listaCampeoes.append(c)
    
    def listarTime(self):
        for campeao in self.listaCampeoes:
            campeao.exibirStatus()
    
    def UsarHabilidadeDeTodos(self):
        for campeao in self.listaCampeoes:
            campeao.usarHabilidade()



def Batalha(campeao1, campeao2):
    print(f"{campeao1.nome} vs {campeao2.nome}")
    while campeao1.vida > 0 and campeao2.vida > 0:
        dano = 50  # Exemplo de dano fixo
        campeao2.receberDano(dano)
        if campeao2.vida <= 0:
            print(f"{campeao1.nome} venceu!")
            break
        campeao1, campeao2 = campeao2, campeao1  # Troca de papéis
    
#Dentro de batalha seria interessante mostrar quem atacou primeiro, o dano causado e a vida restante de cada campeão após cada ataque.
