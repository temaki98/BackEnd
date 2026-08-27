lista = []

lista.append("item1")
lista.append("item2")
lista.append("item3")
lista.append("item2")  # Adding a duplicate item to the list
print(lista)

print(lista[0])  # Accessing the first item in the list
print(lista[1])  # Accessing the second item in the list

print(len(lista))  # Getting the length of the list

chamado = {
    "id": 1,
    "titulo": "Problema com o sistema",
    "situação": "Aberto",
    "responsável": "João",
    "urgente": True
}
print(type(chamado))  # Printing the type of the chamado variable

chamado2 = {
    "id": 2,
    "titulo": "Erro no login",
    "situação": "Fechado",
    "responsável": "Maria",
    "urgente": False
}
#aa
lista = [chamado, chamado2]
print(lista)  # Creating a list with the two chamado dictionaries