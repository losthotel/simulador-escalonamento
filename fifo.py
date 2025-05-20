# Simulação do escalonamento FIFO

class Processo:
    def __init__(self, pid, tempo_chegada, tempo_execucao):
        self.pid = pid
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.tempo_espera = 0
        self.tempo_saida = 0

def escalonamento_fifo(processos):
    tempo_atual = 0
    for processo in processos:
        if tempo_atual < processo.tempo_chegada:
            tempo_atual = processo.tempo_chegada
        processo.tempo_espera = tempo_atual - processo.tempo_chegada
        tempo_atual += processo.tempo_execucao
        processo.tempo_saida = tempo_atual

    # Exibir os resultados
    print("PID | Chegada | Execução | Espera | Saída")
    for p in processos:
        print(f"{p.pid:>3} | {p.tempo_chegada:>7} | {p.tempo_execucao:>8} | {p.tempo_espera:>6} | {p.tempo_saida:>5}")

# Exemplo de uso
processos = [
    Processo(pid=1, tempo_chegada=0, tempo_execucao=5),
    Processo(pid=2, tempo_chegada=2, tempo_execucao=3),
    Processo(pid=3, tempo_chegada=4, tempo_execucao=1),
]

# Ordena os processos pela ordem de chegada
processos.sort(key=lambda p: p.tempo_chegada)

escalonamento_fifo(processos)
