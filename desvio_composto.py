viagem_tempo = int(input("Digite a duração da sua viagem"))

viagem_distancia = int(input("Digite a distância percorrida na viagem"))

velocidade_media = viagem_distancia / viagem_tempo

if velocidade_media >= 80:
  print("Atenção! Com a velocidade média de {}, pode ser que você tenha tomado uma multa!".format(velocidade_media))
else:
  print("Parabéns! Sua velocidade média de {} você provavelmente não foi multado".format(velocidade_media))