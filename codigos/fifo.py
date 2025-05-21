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

def executar():
    processos = [
        Processo(pid=1, tempo_chegada=0, tempo_execucao=5),
        Processo(pid=2, tempo_chegada=2, tempo_execucao=3),
        Processo(pid=3, tempo_chegada=4, tempo_execucao=1),
    ]
    processos.sort(key=lambda p: p.tempo_chegada)
    escalonamento_fifo(processos)

    cabecalho = f"{'PID':<5}{'Chegada':<10}{'Execução':<10}{'Espera':<10}{'Saída':<10}\n"
    linha_sep = "-" * 45 + "\n"

    resultado = cabecalho + linha_sep
    for p in processos:
        resultado += f"{p.pid:<5}{p.tempo_chegada:<10}{p.tempo_execucao:<10}{p.tempo_espera:<10}{p.tempo_saida:<10}\n"

    return resultado