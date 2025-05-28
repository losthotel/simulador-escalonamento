
# Projeto Simulador de Escalonamento de Processos

# 🖥️ Simulador de Escalonamento de Processos na Perspectiva do Usuário  
Este projeto tem como objetivo o desenvolvimento de um sistema que simula algoritmos de escalonamento de processos, com foco na visualização clara e interativa do comportamento dos algoritmos do ponto de vista do usuário final. A ferramenta foi pensada para fins educacionais, facilitando o entendimento dos principais métodos de escalonamento utilizados em Sistemas Operacionais.

## 1. Objetivos do Projeto

### 1.1. Objetivo Geral  
Desenvolver um simulador visual de escalonamento de processos que permita a compreensão prática e interativa dos algoritmos, oferecendo uma interface intuitiva e de fácil uso.

## 2. Escopo do Projeto

### 2.1. Funcionalidades  
- Simulação dos algoritmos:
  - **FIFO (First In, First Out)**
  - **Prioridade (Não Preemptiva)**
  - **Round Robin**
  - **SRTF (Shortest Remaining Time First)**
  - **SJF (Shortest Job First**
  - **Multinível**
- Entrada de processos (tempo de chegada, duração, prioridade)  
- Exibição gráfica da linha do tempo
- Interface amigável utilizando **CustomTkinter**  
- Relatório final com tempos médios de espera e turnaround  

### 2.2. Tecnologias Utilizadas  
- Python 3  
- CustomTkinter  
- Programação modular (interface separada dos algoritmos)  

## 3. Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/losthotel/simulador-escalonamento.git
   ```

2. Instale as dependências:
   ```bash
   pip install customtkinter
   ```

3. Execute o sistema:
   ```bash
   python interfacegrafica.py
   ```

> ⚠️ Certifique-se de estar com o Python 3 instalado corretamente.

## 4. Atualizações no Repositório  
Em desenvolvimento contínuo. Futuras versões incluirão:
- Animações aprimoradas  
