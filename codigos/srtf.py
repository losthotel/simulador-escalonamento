import heapq

def srtf(processos):
    fila = []
    tempo_atual = 0
    processos.sort(key=lambda x: x[2]) 

    i = 0
    processo_atual = None
    tempo_restante = 0
    log = ""
    tempo_anterior = 0

    while i < len(processos) or fila or processo_atual:

        while i < len(processos) and processos[i][2] <= tempo_atual:
            heapq.heappush(fila, (processos[i][1], processos[i][0], processos[i][2]))
            i += 1

        if processo_atual:
            heapq.heappush(fila, (tempo_restante, processo_atual, tempo_anterior))

        if fila:
            tempo_restante, processo_atual, tempo_anterior = heapq.heappop(fila)
            log += f"Tempo {tempo_atual}: Executando {processo_atual} (restante: {tempo_restante})\n"
            tempo_atual += 1
            tempo_restante -= 1

            if tempo_restante == 0:
                log += f"Tempo {tempo_atual}: Processo {processo_atual} concluído.\n"
                processo_atual = None
        else:
            tempo_atual += 1

    return log

def executar():
    processos = [
        ("Carregando arquivos do sistema", 3, 0),
        ("Verificando atualizações", 4, 2),
        ("Inicializando os serviços", 1, 1),
        ("Configurando ambiente", 2, 3),
    ]
    return srtf(processos)
