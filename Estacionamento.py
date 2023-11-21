from veiculo import Veiculo
from vaga import Vaga

from datetime import datetime

def calcular_tempo_estacionamento(entrada, saida):
    formato = "%H:%M"
    hora_entrada = datetime.strptime(entrada, formato)
    hora_saida = datetime.strptime(saida, formato)

    diferenca_tempo = hora_saida - hora_entrada

    return diferenca_tempo.total_seconds() / 60


class Estacionamento:
    def __init__(self, capacidade, valor_hora):
        self.capacidade = capacidade
        self.valor_hora = valor_hora
        
        self.veiculos = [Vaga(numero) for numero in range(1, capacidade + 1)]
        self.veiculos_estacionados = {}
        self.veiculos_estacionados_lista = []
        self.veiculos_estacionados_hoje = 0
        self.veiculos_estacionados_total = 0
        self.veiculos_estacionados_max = 0
        self.lucro = 0
    

    def get_veiculos_estacionados(self):
        if not self.veiculos_estacionados_lista:
            return "Nenhum veículo estacionado hoje."
        for veiculo_info in self.veiculos_estacionados_lista:
            print("=====================================")
            print(f"Tipo do veículo: {veiculo_info['tipo_veiculo']}")
            print(f"Placa: {veiculo_info['placa']}")
            print(f"Horário de entrada: {veiculo_info['horario_entrada']}")
            print(f"Vaga: {veiculo_info['vaga']}")


    def get_vagas_disponiveis(self):
        vagas_disponiveis = [
            vaga.numero for vaga in self.veiculos if vaga.disponivel
        ]
        return vagas_disponiveis


    def get_vagas_ocupadas(self):
        vagas_ocupadas = [
            (vaga.numero, vaga.veiculo.placa) for vaga in self.veiculos if not vaga.disponivel
        ]
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
                self.veiculos_estacionados_lista.append({
                    'tipo_veiculo': veiculo.tipo_veiculo,
                    'placa': veiculo.placa,
                    'horario_entrada': veiculo.horario_entrada,
                    'vaga': vaga.numero
                })

                # Controle estatístico
                self.veiculos_estacionados_hoje += 1
                self.veiculos_estacionados_total += 1
                if self.veiculos_estacionados_total > self.veiculos_estacionados_max:
                    self.veiculos_estacionados_max = self.veiculos_estacionados_total
    
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
            valor_cobranca = vaga_ocupada.veiculo.calcular_cobranca(tempo_estacionamento_minutos, self.valor_hora)

            # Atualizar o lucro do estacionamento
            self.lucro += valor_cobranca

            # Liberar a vaga
            vaga_ocupada.disponivel = True
            vaga_ocupada.veiculo = None
            del self.veiculos_estacionados[veiculo_placa]

            self.veiculos_estacionados_total -= 1

            return f'Vaga {vaga_ocupada.numero} liberada. Cobrança total: R${valor_cobranca:.2f}'

        return f'Veículo {veiculo_placa} não encontrado no estacionamento'
    

    def aproveitamento_vagas(self):
        vagas_ocupadas = self.get_vagas_ocupadas()
        total_vagas_ocupadas = len(vagas_ocupadas)

        percentual_utilizado_atual = (total_vagas_ocupadas / self.capacidade) * 100
        percentual_utilizado_max = (self.veiculos_estacionados_max / self.capacidade) * 100

        return percentual_utilizado_atual, percentual_utilizado_max
    
    
    def aproveitamento_tipos_veiculos(self):
        vagas_ocupadas = self.get_vagas_ocupadas()
        total_vagas_ocupadas = len(vagas_ocupadas)
            
        # Contar veículos por tipo
        tipos_veiculos = {}
        for veiculo_info in self.veiculos_estacionados_lista:
            tipo_veiculo = veiculo_info['tipo_veiculo']
            tipos_veiculos[tipo_veiculo] = tipos_veiculos.get(tipo_veiculo, 0) + 1
        
        # Calcular percentuais
        percentuais = {}
        for tipo, quantidade in tipos_veiculos.items():
            percentual = (quantidade / self.veiculos_estacionados_hoje) * 100
            percentuais[tipo] = f'{percentual:.2f}%'

        return percentuais


    def resumo_dia(self):
        lucro = self.lucro
        veiculos_estacionados = self.veiculos_estacionados_hoje
        percentual_utilizado_atual, percentual_utilizado_max = self.aproveitamento_vagas()
        percentuais = self.aproveitamento_tipos_veiculos()

        percentual_carro = percentuais.get('carro', '0.00%')
        percentual_moto = percentuais.get('moto', '0.00%')
        percentual_caminhao = percentuais.get('caminhao', '0.00%')

        return f'{veiculos_estacionados} veículos estacionados hoje.\nLucro: R${lucro:.2f}\nAproveitamento máximo do estacionamento hoje : {percentual_utilizado_max:.2f}%\nPercentual de veículos que usaram o estacionamento hoje: Carro: {percentual_carro}\nMoto: {percentual_moto}\nCaminhão: {percentual_caminhao}'