veiculos_detalhados = {}

def estacionar_veiculo(placa, marca, modelo, cor, proprietario):   # O def é utilizado para as funções/caracteristicas dos veiculos estacionados;
    if placa in veiculos_detalhados:
        print("Veículo já está estacionado.")
    else:
        veiculos_detalhados[placa] = {
            'marca': marca,
            'modelo': modelo,
            'cor': cor,
            'proprietario': proprietario
        }
        print(f"Veículo {placa} estacionado com sucesso!")
        veiculos_estacionados.append(placa)  
# Adiciona a placa à lista de veículos estacionados

def adicionar_veiculo_por_padrao():
    placa = "ARI7070"
    marca = "Mitsubishi"
    modelo = "Lancer"
    cor = "Preto"
    proprietario = "Angelitus dos Paranaue"
    estacionar_veiculo(placa, marca, modelo, cor, proprietario)

veiculos_estacionados = []

def retirar_veiculo(placa):
    if placa in veiculos_estacionados:
        veiculos_estacionados.remove(placa)
        del veiculos_detalhados[placa] 
        print(f"Veículo {placa} retirado com sucesso!")
    else:
        print(f"Veículo {placa} não está estacionado")

def listar_veiculos_estacionados():
    if veiculos_estacionados:
        print("Veículos estacionados:")
        for veiculo in veiculos_estacionados:
            detalhes = veiculos_detalhados[veiculo]
            print(f"Placa: {veiculo}, Marca: {detalhes['marca']}, Modelo: {detalhes['modelo']}, Cor: {detalhes['cor']}, Proprietário: {detalhes['proprietario']}")
    else:
        print("Não há veículos estacionados")

def esta_estacionado(placa):
    if placa in veiculos_estacionados:
        print(f"Veículo {placa} está estacionado")
    else:
        print(f"Veículo {placa} não está estacionado")
# aqui ira listar os veiculos estacionandos e a utilização do if e else para criar as condições necessárias.
def menu():
    while True:
        print("\nMenu:")
        print("1 - Estacionar veículo")
        print("2 - Retirar veículo")
        print("3 - Veículos estacionados")
        print("4 - Está estacionado?")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
#Na parte de cima é as opções que o  usuário deve escolher para o estacionamento do carro, ou a retirada.
        try:
            if opcao == "1":
                placa = input("Digite a placa do veículo: ")
                marca = input("Digite a marca do veículo: ")
                modelo = input("Digite o modelo do veículo: ")
                cor = input("Digite a cor do veículo: ")
                proprietario = input("Digite o proprietário do veículo: ")
                estacionar_veiculo(placa, marca, modelo, cor, proprietario)
            elif opcao == "2":
                placa = input("Digite a placa do veículo: ")
                retirar_veiculo(placa)
            elif opcao == "3":
                listar_veiculos_estacionados()
            elif opcao == "4":
                placa = input("Digite a placa do veículo: ")
                esta_estacionado(placa)
            elif opcao == "0":
                print("Saindo")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    adicionar_veiculo_por_padrao()
    menu()
#Na parte de cima é as opções que o  usuário deve adicionar de acordo com o seu veiculo