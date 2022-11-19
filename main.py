from DEF import *

class Ficha():
    def __init__(self,role, origins, languages, personality, clothing, hair, affec,
                 value, people, ppmost, psmost, backf, desc, lf, fcrisis, enchild,
                 friends, enemys, revenge, love, stts):
        self.role = role
        self.origins = origins
        self.languages = languages
        self.personality = personality
        self.clothing = clothing
        self.hairstyle = hair
        self.affectation = affec
        self.value_most = value
        self.people = people
        self.people_most = ppmost
        self.possession_most = psmost
        self.back_family = backf
        self.description = desc
        self.life_goals = lf
        self.family_crisis = fcrisis
        self.enviroment_child = enchild
        self.friends = friends
        self.enemys = enemys
        self.sweet_revenge = revenge
        self.love = love
        self.stats = stts

def menu2(obj):
    while True:
        m = str(input("Deseja rolar novamente alguma tabela?[S/N] ")).upper()[0].strip()
        if m == 'S':
            print('_' * 45)
            print(f'{"TABELAS":^45}')
            print(f'1-Role\n'
                  f'2-Origem\n'
                  f'3-Personalidade\n'
                  f'4-Clothing\n'
                  f'5-Hairstyle\n'
                  f'6-Affectation\n'
                  f'7-Value Most\n'
                  f'8-People\n'
                  f'9-People Most\n'
                  f'10-Possession Most\n'
                  f'11-Original Background\n'
                  f'12-Description\n'
                  f'13-Objetivo na vida\n'
                  f'14-Crise Familiar\n'
                  f'15-Ambiente na infancia\n'
                  f'16-Amigos\n'
                  f'17-Inimigos\n'
                  f'18-Vingança\n'
                  f'19-Amores Perdidos\n'
                  f'20-Stats\n'
                  f'00-Cancelar')

            tbl = int(input('Qual tabela? '))
            if tbl == 1:
                while True:
                    rr = roll_roles()
                    setattr(obj, 'role', rr)
                    print(f'Seu novo Papel é {rr}')
                    p2 = str(input('Deseja rolar Papel novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 2:
                while True:
                    rr = roll_origins()
                    setattr(obj, 'origins', rr)
                    if (rr == 'North American'):
                        n = "Chinese, Cree, Creole, English,French, Navajo, Spanish"
                    elif (rr == 'South/Central American'):
                        n = "Creole, English, German, Guarani,Mayan, Portuguese, Quechua, Spanish"
                    elif (rr == 'Western European'):
                        n = "Dutch, English, French, German, Italian, Norwegian, Portuguese, Spanish"
                    elif (rr == 'Eastern European'):
                        n = "English, Finnish, Polish, Romanian, Russian, Ukrainian"
                    elif (rr == 'Middle Eastern/North African'):
                        n = "Arabic, Berber, English, Farsi, French, Hebrew, Turkish"
                    elif (rr == 'Sub-Saharan African'):
                        n = "Arabic, English, French, Hausa, Lingala,\nOromo, Portuguese, Swahili, Twi, Yoruba"
                    elif (rr == 'South Asian'):
                        n = "Bengali, Dari, English, Hindi, Nepali,\nSinhalese, Tamil, Urdu"
                    elif (rr == 'South East Asian'):
                        n = "Arabic, Burmese, English, Filipino, Hindi,\nIndonesian, Khmer, Malayan, Vietnamese"
                    elif (rr == 'East Asian'):
                        n = "Cantonese Chinese, English, Japanese, Korean,\nMandarin Chinese, Mongolian"
                    else:
                        n = "English, French, Hawaiian, Maori,\nPama-Nyungan, Tahitian"
                    setattr(obj, 'languages', n)
                    print(f'Sua nova origem é {rr}')
                    p2 = str(input('Deseja rolar Origem novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 3:
                while True:
                    rr = roll_personality()
                    setattr(obj, 'personality', rr)
                    print(f'Sua nova Personalidade é {rr}')
                    p2 = str(input('Deseja rolar Personlidade novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 4:
                while True:
                    rr = roll_clothing()
                    setattr(obj, 'clothing', rr)
                    print(f'Sua nova Clothing é {rr}')
                    p2 = str(input('Deseja rolar Clothing novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 5:
                while True:
                    rr = roll_hairstyle()
                    setattr(obj, 'hairstyle', rr)
                    print(f'Seu novo Hairstyle é {rr}')
                    p2 = str(input('Deseja rolar Hairstyle novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 6:
                while True:
                    rr = roll_affectation()
                    setattr(obj, 'affectation', rr)
                    print(f'Seu novo Affectation é {rr}')
                    p2 = str(input('Deseja rolar Affectation novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 7:
                while True:
                    rr = roll_value_most()
                    setattr(obj, 'value_most', rr)
                    print(f'Seu novo Mais valoriza é {rr}')
                    p2 = str(input('Deseja rolar "Mais valoriza" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 8:
                while True:
                    rr = roll_people()
                    setattr(obj, 'people', rr)
                    print(f'Seu novo "O que vc sente sobre as pessoas" é {rr}')
                    p2 = str(input('Deseja rolar "O que vc sente sobre as pessoas?" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 9:
                while True:
                    rr = roll_people_most()
                    setattr(obj, 'people_most', rr)
                    print(f'Seu novo "Pessoa mais importante da sua vida" é {rr}')
                    p2 = str(input('Deseja rolar "Pessoa mais importante da sua vida" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 10:
                while True:
                    rr = roll_possession_most()
                    setattr(obj, 'possession_most', rr)
                    print(f'Seu novo "Objeto que vc mais valoriza" é {rr}')
                    p2 = str(input('Deseja rolar "Objeto que vc mais valoriza" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 11:
                while True:
                    rr = roll_back_family()
                    setattr(obj, 'back_family', rr)
                    print(f'Seu novo "Original Background" é {rr}')
                    p2 = str(input('Deseja rolar "Original Background" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 12:
                while True:
                    rr = roll_description()
                    setattr(obj, 'description', rr)
                    print(f'Seu novo "Description" é {rr}')
                    p2 = str(input('Deseja rolar "Description" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 13:
                while True:
                    rr = roll_life_goals()
                    setattr(obj, 'life_goals', rr)
                    print(f'Seu novo "Objetivos na Vida" é {rr}')
                    p2 = str(input('Deseja rolar "Objetivos na Vida" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 14:
                while True:
                    rr = roll_family_crisis()
                    setattr(obj, 'family_crisis', rr)
                    print(f'Sua nova "Crise Familiar" é {rr}')
                    p2 = str(input('Deseja rolar "Crise Familiar" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 15:
                while True:
                    rr = roll_enviroment_child()
                    setattr(obj, 'enviroment_child', rr)
                    print(f'Seu novo "Ambiente na infância" é {rr}')
                    p2 = str(input('Deseja rolar "Ambiente na infância" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 16:
                while True:
                    rr = roll_friends(d10f)
                    setattr(obj, 'friends', rr)
                    print(f'Seu novo "Possui Amigos" é {rr}')
                    p2 = str(input('Deseja rolar "Possui Amigos" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 17:
                while True:
                    rr = roll_enemy(d10e)
                    setattr(obj, 'enemys', rr)
                    print(f'Seu novo "Possui Inimigos" é {rr}')
                    p2 = str(input('Deseja rolar "Possui Inimigos" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 18:
                while True:
                    rr = roll_sr(d10e)
                    setattr(obj, 'sweet_revenge', rr)
                    print(f'Seu novo "Vingança" é {rr}')
                    p2 = str(input('Deseja rolar "Vingança" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 19:
                while True:
                    rr = roll_love(d10l)
                    setattr(obj, 'love', rr)
                    print(f'Seu novo "Amores Perdidos" é {rr}')
                    p2 = str(input('Deseja rolar "Amores Perdidos" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 20:
                while True:
                    rr = roll_stats()
                    setattr(obj, 'stats', rr)
                    print(f'Seus novos "Stats" é\n{rr}')
                    p2 = str(input('Deseja rolar "Stats" novamente?[S/N] ')).upper()[0]
                    if p2 == 'N':
                        break
            elif tbl == 00:
                break
        elif m == 'N':
            break
