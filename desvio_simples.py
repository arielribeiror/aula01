viagem_tempo = float(input("Digite a duração da sua viagem"))

viagem_distancia = float(input("Digite a distância percorrida na viagem"))

velocidade_media = viagem_distancia / viagem_tempo

if velocidade_media >= 80:
  print("Atenção! Com a velocidade média de {}, pode ser que você tenha tomado uma multa!".format(velocidade_media))