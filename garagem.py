clientes = []


estados_civis = {
    1: "Solteiro(a)",
    2: "Casado(a)",
    3: "Divorciado(a)",
    4: "Viúvo(a)"
}




def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))


    print("Estado civil:")
    for k, v in estados_civis.items():
        print(f"{k}. {v}")
    opcao_estado = int(input("Digite o número correspondente: "))
    estado_civil = estados_civis.get(opcao_estado, "Não informado")


    possui_veiculo = input("Possui veículo? (s/n): ").lower() == 's'
    veiculo = {}


    if possui_veiculo:
        veiculo['modelo'] = input("Modelo do veículo: ")
        veiculo['placa'] = input("Placa do veículo: ")
        veiculo['ano'] = input("Ano de fabricação: ")


    cliente = {
        'nome': nome,
        'idade': idade,
        'estado_civil': estado_civil,
        'veiculo': veiculo if possui_veiculo else None
    }


    clientes.append(cliente)
    print(" Cliente cadastrado com sucesso!\n")




def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return


    for i, c in enumerate(clientes, 1):
        print(f"Cliente {i}: {c['nome']} ({c['idade']} anos) - {c['estado_civil']}")
        if c['veiculo']:
            print(f"  Veículo: {c['veiculo']['modelo']} | Placa: {c['veiculo']['placa']} | Ano: {c['veiculo']['ano']}")
        print()




def buscar():
    termo = input("Buscar por nome, modelo ou placa: ").lower()
    encontrados = []


    for c in clientes:
        if termo in c['nome'].lower():
            encontrados.append(c)
        elif c['veiculo']:
            if termo in c['veiculo']['modelo'].lower() or termo in c['veiculo']['placa'].lower():
                encontrados.append(c)


    if encontrados:
        for c in encontrados:
            print(f"Cliente: {c['nome']} ({c['idade']} anos) - {c['estado_civil']}")
            if c['veiculo']:
                print(f"  Veículo: {c['veiculo']['modelo']} | Placa: {c['veiculo']['placa']} | Ano: {c['veiculo']['ano']}")
            print()
    else:
        print(" Nenhum resultado encontrado.\n")




def menu():
    while True:
        print("=== SISTEMA DE GARAGEM ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente/veículo/placa")
        print("4. Sair")


        opcao = input("Escolha uma opção: ")


        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")





menu()


