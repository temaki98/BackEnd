email = "nathanlupus@gmail.com"
nome = "nathan de almeida"

posicao = email.find("@")
servidor = email[posicao + 1:]
print(servidor)

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)

mensagem = f"olá! meu nome é {primeiro_nome} e o meu email: {email}."
print(mensagem)
# teste
