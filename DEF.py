from random import choices, choice, randrange


d10f = (randrange(1, 11)-7)
d10e = (randrange(1, 11) - 7)
d10l = (randrange(1, 11) - 7)

def wellcome():
    print(f'"Bem vindo a Nigth City choomba" diz o guarda na fronteira.')
    print()


def roll_roles():
    roles = ["Rockerboy", "Solo", "Netrunner", "Tech", "Medtech", "Media", "Exec", "Lawman", "Fixer", "Nomad" ]
    role = choice(roles)
    return role


def roll_origins():
    global select_or
    origins = ['North American', 'South/Central American', 'Western European', 'Eastern European',
               'Middle Eastern/North African', 'Sub-Saharan African', 'South Asian', 'South East Asian',
               'East Asian', 'Oceania/Pacific Islander']
    select_or = choice(origins)
    return select_or


def roll_languages():
    if (select_or == 'North American'):
        n = "Chinese, Cree, Creole, English,French, Navajo, Spanish"
    elif (select_or == 'South/Central American'):
        n = "Creole, English, German, Guarani,Mayan, Portuguese, Quechua, Spanish"
    elif (select_or == 'Western European'):
        n = "Dutch, English, French, German, Italian, Norwegian, Portuguese, Spanish"
    elif (select_or == 'Eastern European'):
        n = "English, Finnish, Polish, Romanian, Russian, Ukrainian"
    elif (select_or == 'Middle Eastern/North African'):
        n = "Arabic, Berber, English, Farsi, French, Hebrew, Turkish"
    elif (select_or == 'Sub-Saharan African'):
        n = "Arabic, English, French, Hausa, Lingala,\nOromo, Portuguese, Swahili, Twi, Yoruba"
    elif (select_or == 'South Asian'):
        n = "Bengali, Dari, English, Hindi, Nepali,\nSinhalese, Tamil, Urdu"
    elif (select_or == 'South East Asian'):
        n = "Arabic, Burmese, English, Filipino, Hindi,\nIndonesian, Khmer, Malayan, Vietnamese"
    elif (select_or == 'East Asian'):
        n = "Cantonese Chinese, English, Japanese, Korean,\nMandarin Chinese, Mongolian"
    else:
        n = "English, French, Hawaiian, Maori,\nPama-Nyungan, Tahitian"

    return n


def roll_personality():
    personality = ["Shy", "Secretive", "Rebellious", "Antisocial", "Violent", "Arrogant",
                   "Proud", "Aloof", "Moody", "Rash", "Frivolous", "Headstrong", "Fussy", "Nervous",
                   "Stable", "Serious", "Silly", "Fluff – Hearted", "Deceptive", "Intellectual",
                   "Detached", "Friendly", "Outgoing", "Mysteriuos", "Blabbermouth", "Nosy",
                   "Compassionate", "Idealistc", "Perfectionist", "Apathetic", "Fatalistc", "Subtle", "Cunning",
                   "Hedonistic", "Gracious", "Self-critical", "Tidy", "Adaptable", "Blunt", "Complacent"]

    list = []
    nova_list = []

    num = randrange(2, 4)
    for count in range(num):
        list.append(choice(personality))
        for element in list:
            if element not in nova_list:
                nova_list.append(element)
    if len(nova_list) < num:
        nova_list.append(choice(personality))

    if num == 2:
        return ("{} e {}".format(nova_list[0], nova_list[1]))
    else:
        return ("{}, {} e {}".format(nova_list[0], nova_list[1], nova_list[2]))


def roll_clothing():
    clothing = ['Generic Chic (Standard, Colorful, Modular)', 'Leisurewear (Comfort, Agility, Athleticism)',
                'Urban Flash (Flashy, Technological, Streetwear)', 'Businesswear (Leadership, Presence, Authority)',
                'High Fashion (Exclusive, Designer, Couture)', 'Bohemian (Folksy, Retro, Free-spirited)',
                'Bag Lady Chic (Homeless, Ragged, Vagrant)', 'Gang Colors (Dangerous, Violent, Rebellious)',
                'Nomad Leathers (Western, Rugged, Tribal)', 'Asia Pop (Bright, Costume-like, Youthful)',
                'Cyber Grunge (Neon, Individualist, Defiant)', 'Crypto Core (Weird, Practical, Academic)',
                'VSCO (Relaxed, Soft, Pastel)', 'Y2K (Eccentric, Playful, 00s)',
                'Retro Chic (Old-school Cool, Traditional, Distinguished )',
                'Glam Witch (Dark, Occult, Spiritual )', 'Corpo Punk (Understated, Enticing, Edgy)',
                'Dolly Key (Antique, Distressed, Layered)',
                'Mall Goth (Spiky, Provocative, Accessorised)', 'Military Chic (Tactical, Camo, Intimidating)']
    c = choice(clothing)
    return c


def roll_hairstyle():
    hairstyle = ['Mohawk', 'Long and ratty', 'Short and spiked', 'Wild and all over', 'Bald', 'Striped', 'Wild colors',
                 'Neat and short', 'Short and curly', 'Long and straight', 'Short sides long top',
                 'Chin Length & Thick',
                 'Slicked Back', 'Mullet', 'Messy Coils', 'Tightly Braided', 'Military Cut', 'Side Parted',
                 'Multicoloured', 'Asymmetrical']
    h = choice(hairstyle)
    return h


def roll_affectation():
    affectation = ['Tattoos', 'Mirrorshades', 'Ritual scars', 'Spiked gloves', 'Nose rings',
                   'Tongue or other piercings',
                   'Strange fingernail implants', 'Spiked boots or heels', 'Fingerless gloves', 'Strange contacts',
                   'Jacket coverd in sewn on patches ', 'Personalised Lighter', 'Particular shade of lipstick',
                   'A favourite hat', 'Large, retro headphones', 'Excessive jewellery', 'Stylish bag/backpack',
                   'Particularly funky socks/stockings', 'Decorated/Personalised airhypo', 'Cool retro hip flash',
                   'Distinct belt buckle']
    aff = choice(affectation)
    return aff


def roll_value_most():
    value_most = ['Money', 'Honor', 'Your word', 'Honesty', 'Knowledge', 'Vengeance', 'Love', 'Power', 'Family',
                  'Friendship', 'Faith', 'Loyalty', 'Image', 'Life', 'Stability', 'Compassion', 'Independence',
                  'Courage',
                  'Justice', 'Pleasure']
    vm = choice(value_most)
    return vm


def roll_people():
    people = ['I stay neutral', 'I stay neutral', 'I like almost everyone', 'I hate almost everyone',
              'People are tools. Use them for your own goals then discard them',
              'Every person is a valuable individual',
              'People are obstacles to be destroyed if they cross me',
              'People are untrustworthy. Do not depend on anyone',
              'Wipe ‘em all out and let the cockroaches take over', 'People are wonderful!',
              'I either love or hate them. It changes by the hour.',
              'People are like stickers. Collect as many as you can.', 'I like them better than I like myself.',
              'You need the right one for the right job.', 'They are fascinating to watch. From afar.',
              'I stop thinking about them the moment they are out of my bed.', 'I avoid them like the plague.',
              'They aways find new ways to disappoint me.', 'I crave and fear their presence at the same time.',
              'People are like little puzzles for me to crack.', 'I find them hard to understand.']
    pp = choice(people)
    return pp


def roll_people_most():
    people_most = ['A parent', 'A brother or sister', 'A lover', 'A friend', 'Yourself', 'A pet', 'A teacher or mentor',
                   'A public figure', 'A personal hero', 'No one', "A religious figure",
                   "A person who doesn't know you exist.",
                   "Your boss.", "Your therapist.", "A child.", "Someone you’ve only met on the net.",
                   "Someone who is dead.",
                   "A rival.", "A fictional character."]
    pm = choice(people_most)
    return  pm


def roll_possession_most():
    possession_most = ['A weapon', 'A tool', 'A piece of clothing', 'A photograph', 'A book or diary', 'A recording',
                       'A musical instrument', 'A piece of jewelry', 'A toy', 'A letter', "A data chip", "A recipe",
                       "And old console",
                       "A figurine", "A piece of art", "A bottle of vintage alcohol", "A family collection",
                       "A piece of military memorabilia",
                       "A set of dice", "A deed", "A seed"]
    po = choice(possession_most)
    return po


def roll_back_family():
    background_family = ['Corporate Execs', 'Corporate Managers', 'Corporate Technicians', 'Nomad Pack',
                         'Ganger "Family"',
                         'Combat Zoners',
                         'Urban Homeless', 'Megastructure Warren Rats', 'Reclaimers', 'Edgerunners']
    bf = choice(background_family)
    return bf


def roll_description():
    arquivo = open("descricao.txt", "r")
    bloco = []

    for linha in arquivo:
        linha = linha.split("**")
        bloco.append(choice(linha))

    arquivo.close()
    de = choice(bloco)
    return de


def roll_life_goals():
    life_goals = ["Get rid of a bad reputation.", "Gain power and control.",
                  "Get off The Street no matter what it takes.",
                  "Cause pain and suffering to anyone who crosses you.",
                  "Live down your past life and try to forget it.",
                  "Hunt down those responsible for your miserable life and make them pay.",
                  "Get what's rightfully yours.",
                  "Save, if possible, anyone else involved in your background, like a lover, or family member.",
                  "Gain fame and recognition.", "Become feared and respected."]
    lg = choice(life_goals)
    return lg


def roll_family_crisis():
    family_crisis = ['Your family lost everything through betrayal.',
                     'Your family lost everything through badmanagement.',
                     'Your family was exiled or otherwise driven from their original home/nation/Corporation.',
                     'Your family is imprisoned, and you alone escaped.',
                     'Your family vanished. You are the only remaining member.',
                     'Your family was killed, and you were the only survivor.',
                     'Your family is involved in a long-term conspiracy, organization, or association, such as a crime family or revolutionary group.',
                     'Your family was scattered to the winds due to misfortune.',
                     'Your family is cursed with a hereditary feud that has lasted for generations.',
                     'You are the inheritor of a family debt; you must honor this debt before moving on with your life.']
    fc = choice(family_crisis)
    return fc


def roll_enviroment_child():
    enviroment_child = ["Ran on The Street, with no adult supervision.",
                        'Spent in a safe Corp Zone walled off from the rest of the City.',
                        'In a Nomad pack moving from place to place.',
                        'In a Nomad pack with roots in transport (ships, planes, caravans).',
                        'In a decaying, once upscale neighborhood,now holding off the boosters to survive.',
                        'In the heart of the Combat Zone, living in a wrecked building or other squat.',
                        'In a huge "megastructure" building controlled by a Corp or the City.',
                        'In the ruins of a deserted town or city taken over by Reclaimers.',
                        'In a Drift Nation (a floating offshore city) that is a meeting place for all kinds of people.',
                        'In a Corporate luxury "starscraper," high above the rest of the teeming rabble.']
    ec = choice(enviroment_child)
    return ec


def roll_friends(d10f):
    friends = ['Like an older sibling to you.', 'Like a younger sibling to you.', 'A teacher or mentor.',
               'A partner or coworker.', 'A former lover.', 'An old enemy.', 'Like a parent to you.',
               'An old childhood friend.', 'Someone you know from The Street.',
               'Someone with a common interest or goal.']

    if d10f<=0:
        f = 'Não. Ninguém'
        return f
    elif d10f == 1:
        amigo = choice(friends)
        return f'Sim, 1 amigo. {amigo}'

    elif d10f == 2:
        amigo = choice(friends)
        amigo2 = choice(friends)
        return f'Sim, 2 amigos.\n--{amigo}\n--{amigo2}'
    else:
        amigo = choice(friends)
        amigo2 = choice(friends)
        amigo3 = choice(friends)
        return f'Sim, 3 amigos.\n--{amigo}\n--{amigo2}\n--{amigo3}'


def roll_enemy(d10e):
    enemys = ["Ex-friend", 'Ex-lover', 'Estranged relative', 'Childhood enemy', 'Person working for you',
              'Person you work for',
              'Partner or coworker', 'Corporate exec', 'Government official', 'Boosterganger']
    cause = ['Caused the other to lose face or status.', 'Caused the loss of lover, friend, or relative',
             'Caused a major public humiliation', 'Accused the other of cowardice or some othermajor personal flaw.',
             'Deserted or betrayed the other.', "Turned down the other's offer of a job or romantic involvement.",
             "You just don't like each other.", "One of you was a romantic rival.", "One of you was a business rival.",
             "One of you set the other up for a crime they didn't commit."]
    throw_in_u = ["Just themselves and even they won't go out of their way.", "Just themselves.",
                  "Just themselves and a close friend.",
                  "Themselves and a few (1d6/2) friends.", "Themselves and a few (1d10/2) friends.",
                  "An entire gang (at least 1d10 + 5 people).",
                  "The local cops or other Lawmen.", "A powerful gang lord or small Corporation.",
                  "A powerful Corporation.", "An entire city or government or agency."]
    if d10e <= 0:
        return 'Não, nenhum.'
    elif d10e == 1:
        global inimigo,motivo, tinu
        inimigo = choice(enemys)
        motivo = choice(cause)
        tinu = choice(throw_in_u)
        return f'Sim, 1 inimigo.\n--{inimigo}\nE por que? {motivo}\nCom o que te ataca? {tinu}'
    elif d10e == 2:
        global inimigo2, motivo2, tinu2
        inimigo = choice(enemys)
        motivo = choice(cause)
        tinu = choice(throw_in_u)
        inimigo2 = choice(enemys)
        motivo2 = choice(cause)
        tinu2 = choice(throw_in_u)
        return f'Sim, 2 inimigos.\n--"{inimigo}"\nE por que? {motivo}\nCom o que te ataca? {tinu}\n' \
               f'--"{inimigo2}"\nE por que? {motivo2}\nCom o que te ataca? {tinu2}'

    else:
        global inimigo3, motivo3, tinu3
        inimigo = choice(enemys)
        motivo = choice(cause)
        tinu = choice(throw_in_u)
        inimigo2 = choice(enemys)
        motivo2 = choice(cause)
        tinu2 = choice(throw_in_u)
        inimigo3 = choice(enemys)
        motivo3 = choice(cause)
        tinu3 = choice(throw_in_u)
        return f'Sim, 3 inimigos.\n--{inimigo}\nE por que? {motivo}\nCom o que te ataca? {tinu}\n' \
               f'--{inimigo2}\nE por que? {motivo2}\nCom o que te ataca? {tinu2}\n' \
               f'--{inimigo3}\nE por que? {motivo3}\nCom o que te ataca? {tinu3}'


def roll_sr(d10e):
    sw = ["Avoid the scum.", "Go into a murderous rage and try to physically rip their face off.",
          "Backstab them indirectly.", "Verbally attack them.",
          "Set them up for a crime or other transgression they didn't commit.",
          "Set out to murder or maim them."]
    weights = [20, 20, 20, 20, 10, 10]
    if d10e <= 0:
        return 'Sem inimigos, sem vingança'
    else:
        sr = choices(sw, weights)
        sr2 = choices(sw,weights)
        sr3 = choices(sw, weights)
        if d10e == 1:
            return f'Sweet Revenge!\n__O que "{inimigo}" fara a respeito:\n{sr}'
        elif d10e == 2:
            return f'Sweet Revenge!\n__O que "{inimigo}" fara a respeito:\n{sr}\n' \
                   f'__O que "{inimigo2}" fara a respeito:\n{sr2}'
        else:
            return f'Sweet Revenge!\n__O que "{inimigo}" fara a respeito:\n{sr}\n' \
                   f'O que "{inimigo2}" fara a respeito:\n{sr2}\n' \
                   f'O que "{inimigo3}" fara a respeito:\n{sr3}'


def roll_love(d10l):
    t_love = ["Your lover died in an accident.", "Your lover mysteriously vanished.", "It just didn't work out.",
              "A personal goal or vendetta came between you and your lover.",
              "Your lover was kidnapped", "Your lover went insane or cyberpsycho.", "Your lover committed suicide.",
              "Your lover was killed in a fight", "A rival cut you out of the action",
              "Your lover is imprisoned or exiled."]
    tl = choice(t_love)
    tl2 = choice(t_love)
    tl3 = choice(t_love)

    if d10l <= 0:
        return 'Não, nenhum.'
    elif d10l == 1:
        return f'Sim, somente um. {tl}'
    elif d10l == 2:
        return f'Sim, dois.\n__{tl}\n__{tl2} '
    else:
        return f'Sim, três.\n__{tl}\n__{tl2}\n__{tl3}'


def roll_stats():
    # METHOD 2 - EDGERUNERS
    from random import randint
    stt = ' '
    int = ref = dex = tech = cool = will = luck = move = body = emp = 0
    #print("Seus status são:")
    for c in range(1, 11):
        d10 = randint(1, 10)
        if c == 1:
            stt = 'INT'
            if d10 == 1:
                int = 6
            elif d10 == 2:
                int = 7
            elif d10 == 3:
                int = 5
            elif d10 == 4:
                int = 5
            elif d10 == 5:
                int = 6
            elif d10 == 6:
                int = 7
            elif d10 == 7:
                int = 7
            elif d10 == 8:
                int = 7
            elif d10 == 9:
                int = 7
            else:
                int = 6
            #print(f'Vc rolou {d10} e tem {int} em {stt}.')
        elif c == 2:
            stt = 'REF'
            if d10 == 1:
                ref = 7
            elif d10 == 2:
                ref = 8
            elif d10 == 3:
                ref = 8
            elif d10 == 4:
                ref = 8
            elif d10 == 5:
                ref = 6
            elif d10 == 6:
                ref = 7
            elif d10 == 7:
                ref = 7
            elif d10 == 8:
                ref = 8
            elif d10 == 9:
                ref = 7
            else:
                ref = 6
            #print(f'Vc rolou {d10} e tem {ref} em {stt}.')
        elif c == 3:
            stt = 'DEX'
            if d10 == 1:
                dex = 7
            elif d10 == 2:
                dex = 6
            elif d10 == 3:
                dex = 7
            elif d10 == 4:
                dex = 6
            elif d10 == 5:
                dex = 7
            elif d10 == 6:
                dex = 6
            elif d10 == 7:
                dex = 6
            elif d10 == 8:
                dex = 7
            elif d10 == 9:
                dex = 6
            else:
                dex = 8
            #print(f'Vc rolou {d10} e tem {dex} em {stt}.')
        elif c == 4:
            stt = 'TECH'
            if d10 == 1:
                tech = 3
            elif d10 == 2:
                tech = 3
            elif d10 == 3:
                tech = 4
            elif d10 == 4:
                tech = 4
            elif d10 == 5:
                tech = 5
            elif d10 == 6:
                tech = 5
            elif d10 == 7:
                tech = 5
            elif d10 == 8:
                tech = 5
            elif d10 == 9:
                tech = 4
            else:
                tech = 5
            #print(f'Vc rolou {d10} e tem {tech} em {stt}.')
        elif c == 5:
            stt = 'COOL'
            if d10 == 1:
                cool = 8
            elif d10 == 2:
                cool = 6
            elif d10 == 3:
                cool = 7
            elif d10 == 4:
                cool = 6
            elif d10 == 5:
                cool = 7
            elif d10 == 6:
                cool = 7
            elif d10 == 7:
                cool = 6
            elif d10 == 8:
                cool = 6
            elif d10 == 9:
                cool = 6
            else:
                cool = 6
            #print(f'Vc rolou {d10} e tem {cool} em {stt}.')
        elif c == 6:
            stt = 'WILL'
            if d10 == 1:
                will = 6
            elif d10 == 2:
                will = 6
            elif d10 == 3:
                will = 7
            elif d10 == 4:
                will = 7
            elif d10 == 5:
                will = 6
            elif d10 == 6:
                will = 6
            elif d10 == 7:
                will = 7
            elif d10 == 8:
                will = 6
            elif d10 == 9:
                will = 6
            else:
                will = 6
            #print(f'Vc rolou {d10} e tem {will} em {stt}.')
        elif c == 7:
            stt = 'LUCK'
            if d10 == 1:
                luck = 5
            elif d10 == 2:
                luck = 7
            elif d10 == 3:
                luck = 6
            elif d10 == 4:
                luck = 6
            elif d10 == 5:
                luck = 7
            elif d10 == 6:
                luck = 6
            elif d10 == 7:
                luck = 7
            elif d10 == 8:
                luck = 5
            elif d10 == 9:
                luck = 6
            else:
                luck = 5
            #print(f'vc rolou {d10} e tem {luck} em {stt}')
        elif c == 8:
            stt = 'MOVE'
            if d10 == 1:
                move = 5
            elif d10 == 2:
                move = 5
            elif d10 == 3:
                move = 7
            elif d10 == 4:
                move = 5
            elif d10 == 5:
                move = 6
            elif d10 == 6:
                move = 7
            elif d10 == 7:
                move = 6
            elif d10 == 8:
                move = 6
            elif d10 == 9:
                move = 5
            else:
                move = 6
            #print(f'vc rolou {d10} e tem {move} em {stt}')
        elif c == 9:
            stt = 'BODY'
            if d10 == 1:
                body = 5
            elif d10 == 2:
                body = 7
            elif d10 == 3:
                body = 6
            elif d10 == 4:
                body = 6
            elif d10 == 5:
                body = 7
            elif d10 == 6:
                body = 6
            elif d10 == 7:
                body = 7
            elif d10 == 8:
                body = 5
            elif d10 == 9:
                body = 6
            else:
                body = 5
            #print(f'vc rolou {d10} e tem {body} em {stt}')
        else:
            stt = 'EMP'
            if d10 == 1:
                emp = 5
            elif d10 == 2:
                emp = 6
            elif d10 == 3:
                emp = 5
            elif d10 == 4:
                emp = 6
            elif d10 == 5:
                emp = 4
            elif d10 == 6:
                emp = 5
            elif d10 == 7:
                emp = 6
            elif d10 == 8:
                emp = 4
            elif d10 == 9:
                emp = 5
            else:
                emp = 5
            #print(f'vc rolou {d10} e tem {emp} em {stt}')

    return f'Seus Stats são:\nINT({int}), REF({ref}), DEX({dex}), TECH({tech}), COLL({cool})\nWILL({will}), LUCK({luck}), MOVE({move}), BODY({body}), EMP({emp})'


def roll_tabel(txt, lista):
    a = choice(lista)
    return a


def bye():
    print(f'"PRÓXIMO"\ndiz o guarda com um sorriso predatório no rosto')


def name():
    global n
    n = input('Qual o nome do personagem? ').strip()
    if n == '':
        n = 'NPC'
    return n


def player():
    global p
    p = input('Insira o nome do jogador(a)').capitalize().strip()
    if p == '':
        p = 'Mestre'
    return p


def criararq(player, nome):
    a = open(nome + '.txt', 'w', encoding = 'utf-8')
    a.close()
    print(f'Arquivo de {nome}/{player} criado com sucesso')


def save():
    perg = ' '
    while perg not in 'S':
        perg = str(input('Deseja salvar a ficha?[S/N] ')).strip().upper()[0]
        if perg == 'N':
            bye()
            break
        elif perg == 'S':
            print('Salvanado ficha...')
            criararq(name(),player())
        else:
            print('Valor inválido')
            continue

