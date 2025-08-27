import campeao
import random

#Me lembre a forma de criar um objeto em python

def main():
    time1 = campeao.Time()
    time2 = campeao.Time()

    jinx = campeao.Jinx()
    garen = campeao.Garen()
    ahri = campeao.Ahri()
    yasuo = campeao.Yasuo()
    darius = campeao.Darius()
    lux = campeao.Lux()
    zed = campeao.Zed()
    katarina = campeao.Katarina()
    teemo = campeao.Teemo()
    morgana = campeao.Morgana()

    time1.adicionarCampeao(jinx)
    time1.adicionarCampeao(garen)
    time1.adicionarCampeao(ahri)
    time1.adicionarCampeao(yasuo)
    time1.adicionarCampeao(darius)

    time2.adicionarCampeao(lux)
    time2.adicionarCampeao(zed)    
    time2.adicionarCampeao(katarina)
    time2.adicionarCampeao(teemo)
    time2.adicionarCampeao(morgana)

    time1.listarTime()
    print()
    time1.UsarHabilidadeDeTodos()
    print()
    time2.listarTime()
    print()
    time2.UsarHabilidadeDeTodos()

    batalha = campeao.Batalha(random.choice(time1.listaCampeoes), random.choice(time2.listaCampeoes))
    

if __name__ == "__main__":
    main()