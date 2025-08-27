import campeao
import random

#Me lembre a forma de criar um objeto em python
class partida(campeao.Observador):
    def atualizar(self, evento: str):
        print(f"Evento na partida: {evento}")

def main(): 
    print("Bem-vindo ao jogo de campeões!")
    time1 = campeao.Time()
    time2 = campeao.Time()

    # Criar campeões
    katarina = campeao.Katarina()       
    teemo = campeao.Teemo()
    morgana = campeao.Morgana()
    garen = campeao.Garen()
    jinx = campeao.Jinx()
    ahri = campeao.Ahri()

    katarina.definirEstrategia(campeao.EstrategiaAssassino())
    teemo.definirEstrategia(campeao.EstrategiaAtirador())
    morgana.definirEstrategia(campeao.EstrategiaMago())

    time1.adicionarCampeao(katarina)
    time1.adicionarCampeao(teemo)   
    time1.adicionarCampeao(morgana)
    time2.adicionarCampeao(garen)
    time2.adicionarCampeao(jinx)
    time2.adicionarCampeao(ahri)

    partida_observador = partida()

    for c in time1.listaCampeoes + time2.listaCampeoes:
        c.adicionarObservador(partida_observador)


    # Loop de batalha até que todos os campeões de um time estejam mortos
    while True:
        # Filtra campeões vivos
        vivos_time1 = [c for c in time1.listaCampeoes if c.vida > 0]
        vivos_time2 = [c for c in time2.listaCampeoes if c.vida > 0]

        # Verifica condição de fim de jogo
        if not vivos_time1:
            print("Time 2 venceu!")
            break
        if not vivos_time2:
            print("Time 1 venceu!")
            break

        # Escolhe aleatoriamente um campeão vivo de cada time
        batalhador1 = random.choice(vivos_time1)
        batalhador2 = random.choice(vivos_time2)

        campeao.Batalha(batalhador1, batalhador2)

if __name__ == "__main__":
    main()


