#Listas de reclamações
nomes = []
assuntos = []
reclamacoes = []

while True:

    print("\n1. Listar \n2. Adicionar \n3. Remover \n4. Pesquisar \n5. Sair\n")

    #Variável de opção
    opcao = int(input("Digite qual opção deseja: "))

    if opcao == 1:

        #SE não tiver reclamações na lista
        if len(reclamacoes) == 0:
            print("\nNão há reclamações no momento.\n")
            continue

        #SE tiver vai mostrar o nome e o assunto
        else:
            for indice in range(len(reclamacoes)):
                print(indice + 1, "-","Nome:",nomes[indice],"\nAssunto:",assuntos[indice])

    elif opcao == 2:

        nomeCliente = input("Digite seu nome: ")
        nomes.append(nomeCliente)

        assuntoCliente = input("Digite o assunto: ")
        assuntos.append(assuntoCliente)

        reclamacaoCliente = input("Digite sua reclamação (mais que 10 caracteres): ")

        #SE a reclamação tiver mais que 10 caracteres
        if len(reclamacaoCliente) > 10:
            reclamacoes.append(reclamacaoCliente)
            print("\nSua reclamação foi válidada! Obrigado.\n")

        #SE não, a reclamação fica inválida
        else:
            print("\nSua reclamação não possui mais de 10 caracteres, por favor, reescreva.\n")

    elif opcao == 3:

        #SE não tiver reclamações
        if len(reclamacoes) == 0:
            print("\nNão há reclamações a serem excluídas.\n")
            continue

        #SE tiver vai mostrar o nome do cliente e o assunto
        else:

            for indice in range(len(reclamacoes)):
                print(indice + 1, "-","Nome:",nomes[indice],"\nAssunto:",assuntos[indice])

        #Código para exclusão
        codigoExclusao = int(input("Digite o código da reclamação que deseja excluir: "))

        #SE o número for menor ou maior que a lista
        if codigoExclusao < 1 or codigoExclusao > len(reclamacoes):
            print("\nCódigo inválido.\n")

        #SE o número for válido
        else:
            nomes.pop(codigoExclusao - 1)
            assuntos.pop(codigoExclusao - 1)
            reclamacoes.pop(codigoExclusao - 1)
            print("\nReclamação excluída com sucesso!\n")

    elif opcao == 4:

        #SE não tiver reclamações na lista
        if len(reclamacoes) == 0:
            print("\nNão há reclamações no momento.\n")

        #SE tiver vai mostrar a lista
        else:
            for indice in range(len(reclamacoes)):
                print(indice + 1, "-","Nome:",nomes[indice],"\nAssunto:",assuntos[indice])

            #Código para verificar a reclamação
            codigoVerificacao = int(input("Digite o código da reclamação que deseja verificar: "))

            #SE o código de verificação for menor ou maior que o tamanho da lista o código vai ser inválido
            if codigoVerificacao < 1 or codigoVerificacao > len(reclamacoes):
                print("\nCódigo inválido\n")

            #SE for um código válido ele vai mostrar o nome do usuário, assunto e a reclamação
            else:
                for reclamacao in range(1):
                    print("Nome:",nomes[codigoVerificacao - 1],"\nAssunto:",assuntos[codigoVerificacao - 1],"\nReclamação:",reclamacoes[codigoVerificacao - 1])

    elif opcao == 5:
        break

    else:
        print("\nOpção inválida. Tente novamente\n")

print("\nObrigado por utilizar nossa ouvidoria!")
