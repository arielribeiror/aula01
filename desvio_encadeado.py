lixo1 = float(input("Por favor, difite o peso do primeiro lixo"))
lixo2 = float(input("Por favor, difite o peso do segundo lixo"))
lixo3 = float(input("Por favor, difite o peso do terceiro lixo"))

if lixo1 < lixo2 and lixo1 < lixo3:
  print("O primeiro lixo é o mais leve e será carregado")
else:
  if lixo2 < lixo1 and lixo2 < lixo3:
    print("O segundo lixo é o ais leve e será carregado")
  else:
    if lixo3 < lixo1 and lixo3 < lixo2:
      print("O terceiro lixo é o mais leve e será carregado")
    else:
      print("Existem lixos com o mesmo peso. Entre em contato com a equipe de manutenção")