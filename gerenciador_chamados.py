chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Erro ao acessar o e-mail",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 4,
        "titulo": "Computador lento",
        "prioridade": "baixa",
        "situacao": "resolvido",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "Problema no sistema financeiro",
        "prioridade": "alta",
        "situacao": "em atendimento",
        "categoria": "software"
    }
]


print("========== TODOS OS CHAMADOS ==========")

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("-" * 30)


situacao_desejada = "aberto"
encontrou_chamado = False

print("\n========== FILTRO POR SITUAÇÃO ==========")
print(f"Situação procurada: {situacao_desejada}")

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"\nID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado para essa situação.")


situacao_desejada = "cancelado"
encontrou_chamado = False

print("\n========== TESTE DE SITUAÇÃO INEXISTENTE ==========")
print(f"Situação procurada: {situacao_desejada}")

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"\nID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado para essa situação.")


id_chamado = 3
nova_situacao = "resolvido"
chamado_encontrado = False

print("\n========== ATUALIZAÇÃO DE CHAMADO ==========")

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao
        print(f"Chamado {id_chamado} atualizado com sucesso!")
        print(f"Nova situação: {chamado['situacao']}")
        chamado_encontrado = True
        break

if not chamado_encontrado:
    print("Chamado não encontrado.")


id_chamado = 10
nova_situacao = "em atendimento"
chamado_encontrado = False

print("\n========== TESTE DE ID INEXISTENTE ==========")

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao
        print(f"Chamado {id_chamado} atualizado com sucesso!")
        chamado_encontrado = True
        break

if not chamado_encontrado:
    print("Chamado não encontrado.")


categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print("\n========== CATEGORIAS ==========")

for categoria in categorias:
    print(f"- {categoria}")
