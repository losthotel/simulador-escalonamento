import heapq
def srtf(processos):
    fila = []
    tempo_atual = 0
    processos.sort(key=lambda x: x[2])  # Ordenar por tempo de chegada

    i = 0 
    processo_atual = None
    tempo_restante = 0

    while i < len(processos) or fila or processo_atual:
        while i < len(processos) and processos[i][2] <= tempo_atual:
            heapq.heappush(fila, (processos[i][1], processos[i][0], processos[i][2]))  # (tempo_exec, nome, chegada)
            i += 1

        if processo_atual:          heapq.heappush(fila, (tempo_restante, processo_atual, tempo_atual))

        if fila:  
            tempo_restante, processo_atual, chegada = heapq.heappop(fila)
            print(f"Tempo {tempo_atual}: Executando {processo_atual} (restante: {tempo_restante})")
            tempo_atual += 1
            tempo_restante -= 1

            if tempo_restante == 0:
                print(f"Tempo {tempo_atual}: Processo {processo_atual} concluído.")
                processo_atual = None
        else:
            tempo_atual +=1  

        print("-" * 40)

def main():
    while True:
       
        processos = [
            ("Carregando arquivos do sistema", 3, 0),
            ("Verificando atualizações", 4, 2),
            ("Inicializando os serviços", 1, 1),
            ("Configurando ambiente", 2, 3),
        ]

        print("\nIniciando escalonamento SRTF...\n")
        srtf(processos)

        comando = input("\nDigite 'reiniciar' para rodar novamente ou ENTER para sair: ").strip().lower() # Comando Reiniciar para começar todo o processo novamente
        if comando != "reiniciar":
            break
main()