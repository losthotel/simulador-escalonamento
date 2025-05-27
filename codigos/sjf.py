class Processo:
    
    def __init__(self, nome, tempo_execucao, prioridade):
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
        self.inicio = 0
        self.fim = 0

def escalonador_sjf(processos):

    processos_ordenados = sorted(processos, key=lambda p: p.tempo_execucao)
    tempo_atual = 0
    for p in processos_ordenados:
        p.inicio = tempo_atual
        tempo_atual += p.tempo_execucao
        p.fim = tempo_atual
    return processos_ordenados

def executar():
    processos = [
        Processo("p1", tempo_execucao=4, prioridade=2),
        Processo("p2", tempo_execucao=3, prioridade=1),
        Processo("p3", tempo_execucao=2, prioridade=4),
        Processo("p4", tempo_execucao=1, prioridade=3),
    ]

    processos_executados = escalonador_sjf(processos)

    resultado = "Ordem de execução e tempos (SJF):\n"
    resultado += f"{'Nome':<6}{'Tempo':<8}{'Início':<8}{'Fim':<8}\n"
    resultado += "-" * 34 + "\n"
    
    for p in processos_executados:
        resultado += f"{p.nome:<6}{p.tempo_execucao:<8}{p.inicio:<8}{p.fim:<8}\n"

    return resultado
