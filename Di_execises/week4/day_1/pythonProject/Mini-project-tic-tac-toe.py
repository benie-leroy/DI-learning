

tableau = [['1','|','2','|','3'],['-','|','-','|','-'],['4','|','5','|','6'],['-','|','-','|','-'],['7','|','8','|','9']]
lst = ['1','2','3','4','5','6','7','8','9']


def display_board():
    for i in tableau:
        print(''.join(i))



def player_input(player):
    position = input('Dans quelle case voulez-vous jouer? :')
    while lst.count(position) == 0:
        position = input('entre une nouvelle valeur svp :')
    else:
        for i in tableau:
            try:
                i_pos = i.index(position)
                i[i_pos] = player
            except ValueError:
                continue
        lst.remove(position)
    print(tableau)
    display_board()


def play():
    display_board()
    player1 = input('entrer x svp:')
    player2 = input('entrer o svp :')
    turn = 0
    while turn <9:
        turn +=1
        if turn%2 != 0:
            player_input(player1)
        else:
            player_input(player2)
play()

def check_win():

    new_tab = tableau[0:5:2]

    a = new_tab[0][0:5:2]
    if a[0] == a[1] == a[2] == 'x':
        print('Player x, you are a winner')  
    if a[0] == a[1] == a[2] == 'o':
        print('player o, you are a winner')
        
    b = new_tab[1][0:5:2]
    if b[0] == b[1] == b[2] == 'x':
        print('Player x, you are a winner')
    if b[0] == b[1] == b[2] == 'o':
        print('player o, you are a winner')
        
    c = new_tab[2][0:5:2]
    if c[0] == c[1] == c[2] == 'x':
        print('Player x, you are a winner')
    if c[0] == c[1] == c[2] == 'o':
        print('player o, you are a winner')

    if new_tab[0][0] == new_tab[1][0] == new_tab[2][0] == 'x':
        print('Player x, you are a winner')
    if new_tab[0][0] == new_tab[1][0] == new_tab[2][0] == 'o':
        print('player o, you are a winner')
    if new_tab[0][1] == new_tab[1][1] == new_tab[2][1] == 'x':
        print('Player x, you are a winner')
    if new_tab[0][1] == new_tab[1][1] == new_tab[2][1] == 'o':
        print('player o, you are a winner')
    if new_tab[0][3] == new_tab[1][3] == new_tab[2][3] == 'x':
        print('Player x, you are a winner')
    if new_tab[0][3] == new_tab[1][3] == new_tab[2][3] == 'o':
        print('player o, you are a winner')
    if new_tab[0][0] == new_tab[1][1] == new_tab[2][2] == 'x':
        print('Player x, you are a winner')
    if new_tab[0][0] == new_tab[1][1] == new_tab[2][2] == 'o':
        print('player o, you are a winner')
    if new_tab[0][2] == new_tab[1][1] == new_tab[2][0] == 'x':
        print('Player x, you are a winner')
    if new_tab[0][2] == new_tab[1][1] == new_tab[2][0] == 'o':
        print('player o, you are a winner')
check_win()











