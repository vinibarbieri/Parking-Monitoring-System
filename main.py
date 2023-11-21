from estacionamento import Estacionamento
from veiculo import Carro, Moto, Caminhao


def exibir_menu():
    print("\nMenu:")
    print("1. Estacionar veículo")
    print("2. Ver vagas disponíveis")
    print("3. Ver veículos estacionados")
    print("4. Liberar vaga")
    print("5. Aproveitamento do estacionamento")
    print("6. Resumo do dia")
    print("0. Sair")
    return input("Escolha a opção: ")

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
            print("===============================================================")

            tipo_veiculo = input("Digite o tipo do veículo (carro, moto ou caminhão): ").lower()

            if tipo_veiculo == 'carro' or tipo_veiculo == 'c':
                placa = input("Digite a placa do veículo: ")
                horario_entrada = input("Digite o horário de entrada (HH:MM): ")
                veiculo = Carro(placa, horario_entrada)
                resultado = estacionamento.estacionar_veiculo(veiculo)
                print(resultado)
            
            elif tipo_veiculo == 'moto' or tipo_veiculo == 'm':
                placa = input("Digite a placa do veículo: ")
                horario_entrada = input("Digite o horário de entrada (HH:MM): ")
                veiculo = Moto(placa, horario_entrada)
                resultado = estacionamento.estacionar_veiculo(veiculo)
                print(resultado)

            elif tipo_veiculo == 'caminhao' or tipo_veiculo == 'caminhão':
                placa = input("Digite a placa do veículo: ")
                horario_entrada = input("Digite o horário de entrada (HH:MM): ")
                veiculo = Caminhao(placa, horario_entrada)
                resultado = estacionamento.estacionar_veiculo(veiculo)
                print(resultado)
            
            else:
                print("Tipo de veículo inválido. Tente novamente.")
            
            print("===============================================================")


        # 2. Ver vagas disponíveis
        elif escolha == '2':
            vagas_disponiveis = estacionamento.get_vagas_disponiveis()
            print("==================================================")
            print("Vagas Disponíveis:", vagas_disponiveis)
            print("==================================================")

        # 3. Ver carros estacionados
        elif escolha == '3':
            print('')
            print("Veículos estacionados:")
            veiculos_estacionados = estacionamento.get_veiculos_estacionados()
            if not veiculos_estacionados == None:
                print(veiculos_estacionados)
            print("==================================================")
                     
        # 4. Liberar vaga
        elif escolha == '4':
            placa = input("Digite a placa do veículo a ser liberado: ")
            horario_saida = input("Digite o horário de saída (HH:MM): ")
            resultado = estacionamento.liberar_vaga(placa, horario_saida)
            print("===============================================")
            print(resultado)
            print("===============================================")

        # 5. Aproveitamento do estacionamento
        elif escolha == '5':
            aproveitamento_atual, aproveitamento_max = estacionamento.aproveitamento_vagas()
            percentuais = estacionamento.aproveitamento_tipos_veiculos()

            percentual_carro = percentuais.get('carro', '0.00%')
            percentual_moto = percentuais.get('moto', '0.00%')
            percentual_caminhao = percentuais.get('caminhao', '0.00%')

            print("===========================================================")
            print(f"Aproveitamento do estacionamento atual: {aproveitamento_atual:.2f}%")
            print(f"Aproveitamento máximo do estacionamento: {aproveitamento_max:.2f}%")
            print("")
            print(f"Percentual de veículos que usaram o estacionamento:")
            print(f"Carro: {percentual_carro}")
            print(f"Moto: {percentual_moto}")
            print(f"Caminhão: {percentual_caminhao}")
            print("===========================================================")

        # 6. Resumo do dia
        elif escolha == '6':
            resumo = estacionamento.resumo_dia()
            print("=====================================")
            print("Resumo do dia:")
            print(resumo)
            print("=====================================")

        # 0. Sair
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()