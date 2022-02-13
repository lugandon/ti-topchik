fuck = {
    'Romance': ['It Happened One Night', 'Casablanca', 'The Philadelphia Story'],
    'Action': ['Lethal Weapon 2', 'Atomic Blonde', 'Enter the Dragon'],
    'Comedy': ['Elf', 'The General', 'Shaun of the Dead'],
}

genre = input('Enter the genre (Romance, Action, Comedy)')
if genre in fuck:
    print('Films of', genre, 'genre')
    print(fuck[genre])
