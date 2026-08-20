tarefas = []

while True:
    print("\n===== MENU DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação de uma tarefa")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ").strip()
        prioridade = input("Digite a prioridade (baixa, média ou alta): ").strip().lower()

        if not titulo:
            print("Erro: o título não pode ficar vazio.")
        elif prioridade not in ("baixa", "média", "alta"):
            print("Erro: prioridade inválida. Use baixa, média ou alta.")
        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso!")

    elif opcao == "2":
        if not tarefas:
            print("Não há tarefas cadastradas.")
        else:
            print("\n===== TAREFAS CADASTRADAS =====")
            for numero, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{numero} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    elif opcao == "3":
        if not tarefas:
            print("Não há tarefas cadastradas.")
        else:
            entrada = input("Digite o número da tarefa que deseja concluir: ").strip()

            if not entrada.isdigit():
                print("Número inválido.")
            else:
                numero = int(entrada)
                indice = numero - 1

                if 0 <= indice < len(tarefas):
                    tarefas[indice]["situacao"] = "concluída"
                    print("Tarefa atualizada com sucesso!")
                else:
                    print("Tarefa inexistente.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")
