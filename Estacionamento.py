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
        self.veiculos_estacionados_hoje = 0
        self.lucro = 0

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

    def resumo_dia(self):
        lucro = self.lucro
        veiculos_estacionados = self.veiculos_estacionados_hoje
        return f'{veiculos_estacionados} veículos estacionados hoje.\nLucro: R${lucro:.2f}'