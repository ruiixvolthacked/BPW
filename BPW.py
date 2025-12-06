
# Ruiix_.volt (⁠ ⁠´⁠◡⁠‿⁠ゝ⁠◡⁠`⁠)
# tool basic gini mau di colong (⁠.⁠ ⁠❛⁠ ⁠ᴗ⁠ ⁠❛⁠.⁠)

import random
import os,sys
os.system("clear")
print(f"\033[1;31m ▄▄▄▄    ██▓███   █     █░")
print(f"▓█████▄ ▓██░  ██▒▓█░ █ ░█░")
print(f"▒██▒ ▄██▓██░ ██▓▒▒█░ █ ░█ ")
print(f"▒██░█▀  ▒██▄█▓▒ ▒░█░ █ ░█ ")
print(f"░▓█  ▀█▓▒██▒ ░  ░░░██▒██▓ ")
print(f"░▒▓███▀▒▒▓▒░ ░  ░░ ▓░▒ ▒  ")
print(f"▒░▒   ░ ░▒ ░       ▒ ░ ░  ")
print(f" ░    ░ ░░         ░   ░  ")
print(f" ░                   ░    ")
print(f"      ░")
print(f"")
print(f"\033[1;35m      Ruiix_.volt - cindycate greyhat (⁠.⁠ ⁠❛⁠ ⁠ᴗ⁠ ⁠❛⁠.⁠)")
print(f"")
print(f"\033[1;33m[WARNING] \033[1;31mToo many rows can cause a crash !!!")
word = input("\033[1;35mEnter a word > ")
limit = int(input("\033[1;35mEnter a line > "))
special_input = input("\033[1;35mEnter special characters (press ENTER if none): ")

symbols = special_input if special_input.strip() != "" else ""

digits = "0123456789"


case_variants = [
    word.lower(),
    word.capitalize(),
    word.upper()
]

generated = set()

while len(generated) < limit:
    base = random.choice(case_variants)


    num_len = random.randint(1, 5)
    num = ''.join(random.choice(digits) for _ in range(num_len))


    if symbols:
        sym_count = random.randint(0, 2)
        sym = ''.join(random.choice(symbols) for _ in range(sym_count))
    else:
        sym = ""


    pattern = f"{base}{num}{sym}"

    generated.add(pattern)


with open("wordlist.txt", "w") as f:
    for item in generated:
        f.write(item + "\n")

print(f"\033[1;36m[INFO]\033[1;95m Wordlist is finished [✓] : {len(generated)} row saved success")
