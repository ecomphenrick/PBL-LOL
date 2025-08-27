import campeao

def test_parametros():
    garen = campeao.Garen()

    assert garen.nome == "Garen"
    assert garen.nivel == 1     
    assert garen.vida == 620

def main():
    test_parametros()


