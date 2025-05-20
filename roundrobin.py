from collections import deque

class Processo:
    def __init__(self, nome, tempo_execucao):
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao

def escalonador_round_robin(processos, quantum):
    fila = deque(processos)
    tempo_total = 0

    while fila:
        processo = fila.popleft()
        if processo.tempo_restante > quantum:
            print(f"Executando {processo.nome} por {quantum} unidades de tempo.")
            processo.tempo_restante -= quantum
            tempo_total += quantum
            fila.append(processo)
        else:
            print(f"Executando {processo.nome} por {processo.tempo_restante} unidades de tempo. {processo.nome} concluído.")
            tempo_total += processo.tempo_restante

    print(f"Tempo total de execução: {tempo_total} unidades de tempo.")

# Exemplo de uso
processos = [
    Processo("P1", 10),
    Processo("P2", 5),
    Processo("P3", 8)
]
quantum = 3

escalonador_round_robin(processos, quantum)