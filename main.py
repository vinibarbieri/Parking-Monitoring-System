from estacionamento import Estacionamento
from veiculo import Veiculo
from menu import exibir_menu

def main():
    # Inicializando o programa
    capacidade_estacionamento = int(
        input("Digite a capacidade do estacionamento: "))
    valor_hora = int(input("Digite o valor da hora: "))
    estacionamento = Estacionamento(capacidade_estacionamento, valor_hora)

    while True:
        escolha = exibir_menu()

        # 1. Estacionar veículo
        if escolha == '1':
            placa = input("Digite a placa do veículo: ")
            horario_entrada = input("Digite o horário de entrada (HH:MM): ")
            veiculo = Veiculo(placa, horario_entrada)
            resultado = estacionamento.estacionar_veiculo(veiculo)
            print(resultado)

        # 2. Ver vagas disponíveis
        elif escolha == '2':
            vagas_disponiveis = estacionamento.get_vagas_disponiveis()
            print("Vagas Disponíveis:", vagas_disponiveis)

        # 3. Ver carros estacionados
        elif escolha == '3':
            vagas_ocupadas = estacionamento.get_vagas_ocupadas()
            for vaga, placa in vagas_ocupadas:
                print(f"O carro com a placa {placa} está estacionado na vaga {vaga}")

        # 4. Liberar vaga
        elif escolha == '4':
            placa = input("Digite a placa do veículo a ser liberado: ")
            horario_saida = input("Digite o horário de saída (HH:MM): ")
            resultado = estacionamento.liberar_vaga(placa, horario_saida)
            print(resultado)

        # 5. Veículos estacionados no dia
        elif escolha == '5':
            resumo = estacionamento.resumo_dia()
            print(resumo)

        # 0. Sair
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()