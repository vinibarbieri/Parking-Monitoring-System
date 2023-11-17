class Veiculo:
    def __init__(self, placa):
        self.placa = placa

class Vaga:
    def __init__(self, numero, disponivel=True):
        self.numero = numero
        self.disponivel = disponivel

class Estacionamento:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.veiculos = [Vaga(numero) for numero in range(1, capacidade + 1)]
        self.veiculos_estacionados = {}
        self.veiculos_estacionados_hoje = 0  

    def get_vagas_disponiveis(self):
        vagas_disponiveis = [vaga.numero for vaga in self.veiculos if vaga.disponivel]
        return vagas_disponiveis

    def get_vagas_ocupadas(self):
        vagas_ocupadas = [vaga.numero for vaga in self.veiculos if not vaga.disponivel]
        return vagas_ocupadas

    def estacionar_veiculo(self, veiculo):
        for vaga in self.veiculos:
            if vaga.disponivel:
                vaga.disponivel = False
                self.veiculos_estacionados[veiculo.placa] = vaga
                self.veiculos_estacionados_hoje += 1 
                return f'Veículo {veiculo.placa} estacionado na vaga {vaga.numero}'
        return f'Veículo {veiculo.placa} não pode ser estacionado. Estacionamento lotado!'

    def liberar_vaga(self, veiculo_placa):
        if veiculo_placa in self.veiculos_estacionados:
            vaga_ocupada = self.veiculos_estacionados[veiculo_placa]
            vaga_ocupada.disponivel = True
            del self.veiculos_estacionados[veiculo_placa]
            return f'Vaga {vaga_ocupada.numero} liberada'
        return f'Veículo {veiculo_placa} não encontrado no estacionamento'

    def veiculos_estacionados_no_dia(self):
        return self.veiculos_estacionados_hoje

def exibir_menu():
    print("\nMenu:")
    print("1. Estacionar veículo")
    print("2. Ver vagas disponíveis")
    print("3. Liberar vaga")
    print("4. Veículos estacionados no dia")
    print("0. Sair")
    return input("Escolha a opção: ")

# Função principal
def main():
    capacidade_estacionamento = int(input("Digite a capacidade do estacionamento: "))
    valor_hora = int(input("Digite o valor da hora: "))
    estacionamento = Estacionamento(capacidade_estacionamento)

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            placa = input("Digite a placa do veículo: ")
            veiculo = Veiculo(placa)
            resultado = estacionamento.estacionar_veiculo(veiculo)
            print(resultado)

        elif escolha == '2':
            vagas_disponiveis = estacionamento.get_vagas_disponiveis()
            print("Vagas Disponíveis:", vagas_disponiveis)

        elif escolha == '3':
            placa = input("Digite a placa do veículo a ser liberado: ")
            resultado = estacionamento.liberar_vaga(placa)
            print(resultado)

        elif escolha == '4':
            total_veiculos = estacionamento.veiculos_estacionados_no_dia()
            print(f"Total de veículos estacionados hoje: {total_veiculos}")

        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
