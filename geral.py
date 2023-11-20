from datetime import datetime

def calcular_tempo_estacionamento(entrada, saida):
    formato = "%H:%M"
    hora_entrada = datetime.strptime(entrada, formato)
    hora_saida = datetime.strptime(saida, formato)

    diferenca_tempo = hora_saida - hora_entrada

    return diferenca_tempo.total_seconds() / 60

class Veiculo:
    def __init__(self, placa, horario_entrada):
        self.placa = placa
        self.horario_entrada = horario_entrada


class Vaga:
    def __init__(self, numero, disponivel=True, veiculo=None):
        self.numero = numero
        self.disponivel = disponivel
        self.veiculo = veiculo



class Estacionamento:
    def __init__(self, capacidade, valor_hora):
        self.capacidade = capacidade
        self.valor_hora = valor_hora
        
        self.veiculos = [Vaga(numero) for numero in range(1, capacidade + 1)]
        self.veiculos_estacionados = {}
        self.veiculos_estacionados_hoje = 0
        self.lucro = 0

    def get_vagas_disponiveis(self):
        vagas_disponiveis = [
            vaga.numero for vaga in self.veiculos if vaga.disponivel]
        return vagas_disponiveis

    def get_vagas_ocupadas(self):
        vagas_ocupadas = [
            (vaga.numero, vaga.veiculo.placa) for vaga in self.veiculos if not vaga.disponivel]
        return vagas_ocupadas

    def estacionar_veiculo(self, veiculo):
        # Verificar se o veículo já está estacionado
        if veiculo.placa in self.veiculos_estacionados:
            return f'Veículo {veiculo.placa} já está estacionado'
        # Verificar se há vagas disponíveis
        for vaga in self.veiculos:
            if vaga.disponivel:
                vaga.disponivel = False
                vaga.veiculo = veiculo
                self.veiculos_estacionados[veiculo.placa] = vaga
                self.veiculos_estacionados_hoje += 1
                return f'Veículo {veiculo.placa} estacionado na vaga {vaga.numero}'
        return f'Veículo {veiculo.placa} não pode ser estacionado. Estacionamento lotado!'

    def liberar_vaga(self, veiculo_placa, horario_saida):
        # Verificar se o veículo está estacionado
        if veiculo_placa in self.veiculos_estacionados:
            vaga_ocupada = self.veiculos_estacionados[veiculo_placa]
            hora_entrada = vaga_ocupada.veiculo.horario_entrada

            # Calcular o tempo de estacionamento
            tempo_estacionamento_minutos = calcular_tempo_estacionamento(
                hora_entrada, horario_saida)

            # Calcular o valor da cobrança
            if (tempo_estacionamento_minutos < 60):
                valor_cobranca = self.valor_hora
            elif (tempo_estacionamento_minutos % 60 == 0):
                valor_cobranca = tempo_estacionamento_minutos / 60 * self.valor_hora
            else:
                valor_cobranca = (tempo_estacionamento_minutos // 60 + 1) * self.valor_hora

            # Atualizar o lucro do estacionamento
            self.lucro += valor_cobranca

            # Liberar a vaga
            vaga_ocupada.disponivel = True
            vaga_ocupada.veiculo = None
            del self.veiculos_estacionados[veiculo_placa]

            return f'Vaga {vaga_ocupada.numero} liberada. Cobrança total: R${valor_cobranca:.2f}'

        return f'Veículo {veiculo_placa} não encontrado no estacionamento'


    def veiculos_estacionados_no_dia(self):
        return self.veiculos_estacionados_hoje

    def lucro_dia(self):
        return self.lucro




def exibir_menu():
    print("\nMenu:")
    print("1. Estacionar veículo")
    print("2. Ver vagas disponíveis")
    print("3. Ver carros estacionados")
    print("4. Liberar vaga")
    print("5. Veículos estacionados no dia")
    print("6. Lucro do dia")
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
            total_veiculos = estacionamento.veiculos_estacionados_no_dia()
            print(f"Total de veículos estacionados hoje: {total_veiculos}")

        # 6. Lucro do dia
        elif escolha == '6':
            lucro = estacionamento.lucro_dia()
            print(f"Lucro do dia: R${lucro:.2f}")

        # 0. Sair
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()