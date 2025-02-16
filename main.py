import random
import string
import os

GREEN = '\033[92m'

def generate_links(num_links):
    links = []
    for _ in range(num_links):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        link = f'https://discord.gift/{code}'
        links.append(link)
    return links

BLUE = "\033[94m"
RESET = "\033[0m"

print(f"{BLUE}"
      "$$$$$$$\\   $$$$$$\\  $$$$$$$\\  $$\\      $$\\ $$$$$$$$\\ $$$$$$$$\\  $$$$$$\\  $$\\   $$\\ \n"
      "$$  __$$\\ $$  __$$\\ $$  __$$\\ $$$\\    $$$ |$$  _____|\\__$$  __|$$  __$$\\ $$$\\  $$ |\n"
      "$$ |  $$ |$$ /  $$ |$$ |  $$ |$$$$\\  $$$$ |$$ |         $$ |   $$ /  $$ |$$$$\\ $$ |\n"
      "$$$$$$$\\ |$$$$$$$$ |$$ |  $$ |$$\\$$\\$$ $$ |$$$$$\\       $$ |   $$$$$$$$ |$$ $$\\$$ |\n"
      "$$  __$$\\ $$  __$$ |$$ |  $$ |$$ \\$$$  $$ |$$  __|      $$ |   $$  __$$ |$$ \\$$$$ |\n"
      "$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\\$  /$$ |$$ |         $$ |   $$ |  $$ |$$ |\\$$$ |\n"
      "$$$$$$$  |$$ |  $$ |$$$$$$$  |$$ | \\_/ $$ |$$$$$$$$\\    $$ |   $$ |  $$ |$$ | \\$$ |\n"
      "\\_______/ \\__|  \\__|\\_______/ \\__|     \\__|\\________|   \\__|   \\__|  \\__|\\__|  \\__|\n"
      f"{RESET}")




num_links = int(input('Enter the number of links to generate: '))
generated_links = generate_links(num_links)

directory_name = 'generated_links'
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

file_path = os.path.join(directory_name, 'discord_gift_links.txt')
with open(file_path, 'w') as file:
    for link in generated_links:
        file.write(link + '\n')

print(f'\nGenerated Links:')
for link in generated_links:
    print(f'{GREEN}{link}{RESET}')

print(f'\nLinks have been saved in \'{file_path}\', openable with Notepad.')

input('Press Enter to close the terminal...')
