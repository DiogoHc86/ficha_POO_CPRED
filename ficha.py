from FICHA_POO.main import *
from DEF import *

f = Ficha(roll_roles(),roll_origins(),roll_languages(),roll_personality(),roll_clothing(), roll_hairstyle(),
          roll_affectation(), roll_value_most(), roll_people(), roll_people_most(), roll_possession_most(),
          roll_back_family(), roll_description(), roll_life_goals(), roll_family_crisis(), roll_enviroment_child(),
          roll_friends(d10f), roll_enemy(d10e), roll_sr(d10e), roll_love(d10l), roll_stats())


wellcome()
print(f'Seu papel? {f.role}')
print(f'Sua Origem? {f.origins}')
print(f'Qual desses idiomas vc fala? {f.languages}')
print(f'Sua personalidade? {f.personality}')
print(f'Seu estilo de roupa? {f.clothing}')
print(f'Seu estilo de cabelo? {f.hairstyle}')
print(f'Sua afetação? {f.affectation}')
print(f'O que vc mais valoriza? {f.value_most}')
print(f'O que vc sente sobre as pessoas? {f.people}')
print(f'Quem é a pessoa mais importante da sua vida? {f.people_most}')
print(f'Um objeto que vc mais valoriza? {f.possession_most}')
print(f'E sua família(Original Back)? {f.back_family}')
print(f'de que tipo (Description)? {f.description}')
print(f'Qual seu objetivo na vida? {f.life_goals}')
print(f'Sua crise familiar? {f.family_crisis}')
print(f'Como foi seu ambiente na infância? {f.enviroment_child}')
print(f'Possui amigos? {f.friends}')
print(f'Inimigos? {f.enemys}')
print(f'Vingança? {f.sweet_revenge}')
print(f'Amores perdidos? {f.love}')
print(f.stats)
menu2(f)
perg = ' '
while perg not in 'S':
    perg = str(input('Deseja salvar a ficha?[S/N] ')).strip().upper()[0]
    if perg == 'N':
        bye()
        break
    elif perg == 'S':
        print('Salvnado ficha...')
        nome = name()
        jogador = player()
        criararq(nome,jogador)
        a = open(nome+'.txt', 'w', encoding='utf-8')
        a.write(f'Personagem: {nome}\nJogador: {jogador}\nRole: {f.role}\nOrigem: {f.origins}'
                f'\nIdiomas: {f.languages}\nPersonalidade: {f.personality}\nRoupas: {f.clothing}'
                f'\nCabelo: {f.hairstyle}\nAfetação: {f.affectation}\nO que vc mais valoriza: {f.value_most}'
                f'\nSobre as pessoas: {f.people}\nPessoa mais importante: {f.people_most}\nObjeto mais valioso: {f.possession_most}'
                f'\nOriginal Background: {f.back_family}\nDescription: {f.description}\nObjetivos na vida: {f.life_goals}'
                f'\nCrise familiar: {f.family_crisis}\nAmbiente de infância: {f.enviroment_child}\nAmigos: {f.friends}'
                f'\nInimigos: {f.enemys}\nVingança? {f.sweet_revenge}\nAmores? {f.love}\n{f.stats}')
        a.close()

    else:
        print('Valor invalido')
        continue

