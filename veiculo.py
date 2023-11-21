class Veiculo:
    def __init__(self, placa, horario_entrada, tipo_veiculo):
        self.placa = placa
        self.horario_entrada = horario_entrada
        self.tipo_veiculo = tipo_veiculo

    def calcular_cobranca(self, tempo_estacionamento_minutos, valor_hora):
        if (tempo_estacionamento_minutos < 60):
            valor_cobranca = valor_hora
        elif (tempo_estacionamento_minutos % 60 == 0):
            valor_cobranca = tempo_estacionamento_minutos / 60 * valor_hora
        else:
            valor_cobranca = (tempo_estacionamento_minutos // 60 + 1) * valor_hora

        return valor_cobranca


class Carro(Veiculo):
    def __init__(self, placa, horario_entrada):
        super().__init__(placa, horario_entrada, tipo_veiculo='carro')

    def calcular_cobranca(self, tempo_estacionamento_minutos, valor_hora):
        # Chama o método da classe base para obter a lógica padrão
        valor_cobranca_padrao = super().calcular_cobranca(tempo_estacionamento_minutos, valor_hora)

        return valor_cobranca_padrao


class Moto(Veiculo):
    def __init__(self, placa, horario_entrada):
        super().__init__(placa, horario_entrada, tipo_veiculo='moto')

    def calcular_cobranca(self, tempo_estacionamento_minutos, valor_hora):
        valor_cobranca_padrao = super().calcular_cobranca(tempo_estacionamento_minutos, valor_hora)
        valor_cobranca_moto = valor_cobranca_padrao * 0.5

        return valor_cobranca_moto
    

class Caminhao(Veiculo):
    def __init__(self, placa, horario_entrada):
        super().__init__(placa, horario_entrada, tipo_veiculo='caminhao')

    def calcular_cobranca(self, tempo_estacionamento_minutos, valor_hora):
        valor_cobranca_padrao = super().calcular_cobranca(tempo_estacionamento_minutos, valor_hora)
        valor_cobranca_caminhao = valor_cobranca_padrao * 1.5

        return valor_cobranca_caminhao


