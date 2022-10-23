import random

def play():
    user = input ("Faça sua Escolha: '1' para pedra, '2' para papel, '3' para tesoura\n")
    computer = random.choice(['1', '2', '3'])

#criando retorno de empate vitoria e derrota
    if user == computer:
        return 'EMPATE!'

    if is_win(user, computer):
        return 'Parabéns, Você venceu!'

    return 'Que pena, Você perdeu!'
       #esse return em vc perdeu so sera válido se as outras opções nao forem por isso nao foi adicionado ifelse, lembrando da identação correta para o python identificar a estrutura

               

def is_win(player, opponent):
    if (player == '1' and opponent == '3') or (player == '3' and opponent =='2') \
         or (player == '2' and opponent == '1'):
         return True 

print(play())