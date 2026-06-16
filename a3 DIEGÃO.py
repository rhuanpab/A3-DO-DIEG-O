class SimuladorRover:
    def __init__(self, tamanho=15):
        self.tamanho = tamanho
        self.rover_x = 7
        self.rover_y = 7
        self.direcao = 'N'
        self.lista_direcoes = ['N', 'E', 'S', 'W']

        self.obstaculos = [(3, 3), (3, 4), (10, 10), (7, 5), (12, 2)]

    def imprimir_ambiente(self):
        print("\n--- STATUS ATUAL ---")
        for y in range(self.tamanho):
            linha = ""
            for x in range(self.tamanho):
                if x == self.rover_x and y == self.rover_y:
                    if self.direcao == 'N':
                        linha += "[^] "
                    elif self.direcao == 'S':
                        linha += "[v] "
                    elif self.direcao == 'E':
                        linha += "[>] "
                    elif self.direcao == 'W':
                        linha += "[<] "
                elif (x, y) in self.obstaculos:
                    linha += "[X] "
                else:
                    linha += " .  "
            print(linha)
        print(f"Posição: ({self.rover_x}, {self.rover_y}) | Direção: {self.direcao}\n")

    def girar_direita(self):
        idx_atual = self.lista_direcoes.index(self.direcao)
        self.direcao = self.lista_direcoes[(idx_atual + 1) % 4]

    def girar_esquerda(self):
        idx_atual = self.lista_direcoes.index(self.direcao)
        self.direcao = self.lista_direcoes[(idx_atual - 1) % 4]

    def avancar(self, passos):
        for _ in range(passos):
            novo_x = self.rover_x
            novo_y = self.rover_y

            if self.direcao == 'N':
                novo_y -= 1
            elif self.direcao == 'S':
                novo_y += 1
            elif self.direcao == 'E':
                novo_x += 1
            elif self.direcao == 'W':
                novo_x -= 1

            if 0 <= novo_x < self.tamanho and 0 <= novo_y < self.tamanho:
                if (novo_x, novo_y) in self.obstaculos:
                    print("ALERTA: Obstáculo detectado! Movimento interrompido.")
                    break
                else:
                    self.rover_x = novo_x
                    self.rover_y = novo_y
            else:
                print("ALERTA: Limite do grid atingido! Movimento interrompido.")
                break

    def recuar(self, passos):
        for _ in range(passos):
            novo_x = self.rover_x
            novo_y = self.rover_y

            if self.direcao == 'N':
                novo_y += 1
            elif self.direcao == 'S':
                novo_y -= 1
            elif self.direcao == 'E':
                novo_x -= 1
            elif self.direcao == 'W':
                novo_x += 1

            if 0 <= novo_x < self.tamanho and 0 <= novo_y < self.tamanho:
                if (novo_x, novo_y) in self.obstaculos:
                    print("ALERTA: Obstáculo detectado na traseira! Movimento interrompido.")
                    break
                else:
                    self.rover_x = novo_x
                    self.rover_y = novo_y
            else:
                print("ALERTA: Limite do grid atingido! Movimento interrompido.")
                break

    def detectar_obstaculo(self):
        alvo_x = self.rover_x
        alvo_y = self.rover_y

        if self.direcao == 'N':
            alvo_y -= 1
        elif self.direcao == 'S':
            alvo_y += 1
        elif self.direcao == 'E':
            alvo_x += 1
        elif self.direcao == 'W':
            alvo_x -= 1

        if (alvo_x, alvo_y) in self.obstaculos:
            print(f"SENSOR: Obstáculo detectado diretamente à frente na coordenada ({alvo_x}, {alvo_y})!")
            return True
        else:
            print("SENSOR: Caminho livre à frente.")
            return False

    def executar_script(self, script):
        linhas = script.strip().split('\n')

        for num_linha, linha in enumerate(linhas, 1):
            partes = linha.strip().split()
            if not partes:
                continue

            comando = partes[0].upper()

            try:
                if comando == "AVANCA":
                    if len(partes) < 2:
                        raise ValueError("Falta o parâmetro de passos.")
                    passos = int(partes[1])
                    self.avancar(passos)

                elif comando == "RECUA":
                    if len(partes) < 2:
                        raise ValueError("Falta o parâmetro de passos.")
                    passos = int(partes[1])
                    self.recuar(passos)

                elif comando == "GIRA_DIR":
                    self.girar_direita()

                elif comando == "GIRA_ESQ":
                    self.girar_esquerda()

                elif comando == "DETECTA":
                    self.detectar_obstaculo()

                else:
                    print(f"ERRO SINTÁTICO: Comando '{comando}' não reconhecido.")
                    break

            except ValueError as e:
                print(f"ERRO DE PARÂMETRO: {e} (Ex: AVANCA 5)")
                break
            except Exception as e:
                print(f"ERRO: {e}")
                break

            self.imprimir_ambiente()

# === TESTANDO O SISTEMA ===
if __name__ == "__main__":
    simulador = SimuladorRover(tamanho=15)

    print("=== SIMULADOR DO ROVER ESPACIAL ===")
    print("Ambiente Inicial:")
    simulador.imprimir_ambiente()

    print("\n--- MODO DE COMANDO AO VIVO ---")
    print("Digite os comandos para mover o rover.")
    print("Comandos válidos: AVANCA [n], RECUA [n], GIRA_DIR, GIRA_ESQ, DETECTA")
    print("Digite 'SAIR' para finalizar a apresentação.")

    while True:
        entrada_usuario = input("\nComando > ").strip()

        if entrada_usuario.upper() == "SAIR":
            print("Encerrando o simulador. Apresentação finalizada com sucesso!")
            break
        elif entrada_usuario == "":
            continue
        else:
            simulador.executar_script(entrada_usuario)