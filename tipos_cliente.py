valor_compra = float(input("Por favor, informe o valor da sua compra"))
tipo_cliente = input("Por favor, informe o tipo do cliente")

if "NORMAL" == tipo_cliente.upper():
  if valor_compra < 1000:
    total = valor_compra * .97
  elif valor_compra < 2000:
    total = valor_compra * .96
  else:
    total = valor_compra * .95
elif "VIP" == tipo_cliente.upper():
  if valor_compra < 1000:
    total = valor_compra * .95
  elif valor_compra < 2000:
    total = valor_compra * .93
  else:
    total = valor_compra * .92
elif "VIP PREMIUM" == tipo_cliente.upper():
  if valor_compra < 1000:
    total = valor_compra * .9
  elif valor_compra < 2000:
    total = valor_compra * .85
  else:
    total = valor_compra * .8
else: 
  print("O tipo de usuário não foi reconhecido. Não serão concedidos descontos")
  total = valor_compra
  
print("Você fez uma compra de R${}. Por ser um cliente {}, sua compra custará R${}".format(valor_compra, tipo_cliente, total))