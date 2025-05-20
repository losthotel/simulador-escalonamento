# Processo: nome, tempo de execução, prioridade
processos = [
    {"nome": "P1", "tempo": 4, "prioridade": 2},
    {"nome": "P2", "tempo": 3, "prioridade": 1},
    {"nome": "P3", "tempo": 2, "prioridade": 4},
    {"nome": "P4", "tempo": 1, "prioridade": 3},
]

# Ordena os processos pela prioridade (menor valor = maior prioridade)
processos_ordenados = sorted(processos, key=lambda x: x["prioridade"])

tempo_atual = 0
print("Ordem de execução e tempos:")
for p in processos_ordenados:
    print(f"{p['nome']} (Prioridade: {p['prioridade']}) - Início: {tempo_atual}, Fim: {tempo_atual + p['tempo']}")
    tempo_atual += p["tempo"]