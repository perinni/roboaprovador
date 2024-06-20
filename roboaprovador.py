import time, pyautogui, pyscreeze, sys
from art import text2art
from tqdm import tqdm
from colorama import Fore, Style

# Define os tempos dos modos de operação
safemode = (1.7, 1.5, 1)
fastmode = (0.9, 1.2, 0.6)

# Mensagem de boas-vindas
def print_mensagem_tartaruga(): 
    tartarura = r"""
                 _,.---.---.---.--.._           |R|   !INSTALE OS REQUIREMENTS!
           _.-' `--.`---.`---'-. _,`--.._       |O|    Os pacotes só podem ser
          /`--._ .'.     `.     `,`-.`-._\      |B|   baixados FORA da Intranet
         ||   \  `.`---.__`__..-`. ,'`-._/      |Ô|
    _  ,`\ `-._\   \    `.    `_.-`-._,``-.
 ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.   |A|   !NÃO USE SEM AUTORIZAÇÃO!
(_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \  |P|        !LEIA O TXT!
 `---'    `._ `---._/__,----`           `-. `-\ |R|
           /_, ,  _..-'                    `-._\|O|
           
           \_, \/ ._(                           |V|
            \_, \/ ._\                          |A|
             `._,\/ ._\                         |D|
               `._// ./`-._                     |O|
                 `-._-_-_.-'                    |R|   (•ᴗ•) HP.Inc® 2024 (•ᴗ•)
"""                                                     

    mensagem = "Aprovador IEC - Uso Restrito"

    # Adiciona a cor verde ao texto da mensagem
    mensagem_formatada = f"{Fore.GREEN}{mensagem}{Style.RESET_ALL}" 
    # Imprime o desenho e a mensagem formatada
    print(tartarura)
    print(mensagem_formatada)

print_mensagem_tartaruga()

# Isso faz o mouse não quitar o programa ao bater nos limites de tela (tipo (0,0), (max, max))
pyautogui.FAILSAFE = False

# Pergunta pelo endereço do arquivo TXT
print("\nOBS: O arquivo TXT DEVE estar no mesmo local que o arquivo executável Python!")
txt_file_path = input("\nDigite o nome do arquivo TXT contendo os códigos a serem processados: ")

# Pergunta pelo modo de operação desejado
modo_operacao = input("\nEscolha o modo de operação (Digite 'r' para modo Revogação ou 'a' para modo Aprovação): ")

# Define os atalhos com base no modo escolhido
if modo_operacao == 'r':
    atalho_revogacao = 'ctrl', 'f4'
elif modo_operacao == 'a':
    atalho_revogacao = 'ctrl', 'f5'
else:
    input("\nModo de operação inválido. Use 'r' para revogação ou 'a' aprovação. Pressione Enter para sair. ")
    sys.exit()

# Pergunta pelo modo de velocidade desejado
modo_velocidade = input("\nEscolha o modo de velocidade (Digite 'f' para modo rápido ou 's' para modo seguro): ")

# Define os tempos com base no modo de velocidade escolhido
if modo_velocidade == 'f':
    tempos = fastmode
elif modo_velocidade == 's':
    tempos = safemode
else:
    input("\nModo de velocidade inválido. Use 'f' para fast ou 's' para safe. Pressione qualquer tecla para sair. ")
    sys.exit()

continuar = input("\nTem certeza que deseja continua? (Digite 's' para sim ou 'n' para não): ")

if continuar == 'n':
    input('Programa encerrado. Pressione qualquer tecla para sair. ')
    sys.exit()
    
# Passo 1: Ler os códigos do arquivo TXT
with open(txt_file_path, 'r') as file:
    codigos = [line.strip() for line in file if line.strip()]

try:
    prod = pyautogui.locateOnScreen('productioncheck.png', confidence=0.95)
    resposta = input("\nVocê provavelmente está no ambiente de PRODUÇÃO! Tem MESMO certeza que deseja continuar? (Digite 's' para sim ou 'n' para não): ")

    if resposta == 'n':
        sys.exit()

except pyautogui.ImageNotFoundException:   
    pass

print('\nIniciando processo de aprovação/revogação, não toque mais no computador!')

for i in range(5, 0, -1):
    print("Iniciando em: ", i, " segundos.")
    time.sleep(1)

# Encontra o botão e leva até o WCTL  
try:      
    found_button = pyautogui.locateOnScreen('button.png', confidence=0.95)
    pyautogui.moveTo(pyautogui.center(found_button))

except pyautogui.ImageNotFoundException:
    decisao = input("\nNão foi encontrado o botão de check de transações na tela! Se quiser continuar, tente posicionar o mouse exatamente em cima do botão 'Continuar'' do sap. Digite 'c' para continuar, ou 's' para sair.: ")
    if decisao == 's':
        sys.exit()

pyautogui.moveRel(100,0)
pyautogui.click()
time.sleep(0.1)
pyautogui.write('WCTL')
time.sleep(0.2)
pyautogui.hotkey('enter')
time.sleep(0.5)

# Passo 2: Iterar sobre os códigos
for codigo in tqdm(codigos, desc="Progresso", unit="código"):
    # Digita o código
    pyautogui.write(codigo)
    # Entra na tela
    pyautogui.press('enter')
    time.sleep(tempos[0])
    # Executa o atalho correspondente ao modo de operação
    pyautogui.hotkey(*atalho_revogacao)
    time.sleep(tempos[1])
    # Salva e fecha
    pyautogui.hotkey('ctrl', 's')
    time.sleep(tempos[2])

print("\n__________________________________________\n")
print("Finalizado! Verifique se as aprovações e revogações foram realizadas adequadamente.")
input("\nAperte enter para sair.")