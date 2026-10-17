from colorama import Fore, Style, init

init()

niveis = [
    "Nível 1 - Muito baixo (Crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)",
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE
    
def exibir_situacao(nivel):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(f"{cor}{mensagem}{Style.RESET_ALL}")

print("=== Monitoramento do Reservatório ===\n")
for nivel_atual in [1, 2, 3, 4, 5]:
    exibir_situacao(nivel_atual)

print(Style.RESET_ALL)
