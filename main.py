import random
import curses
import time

def main_menu(screen):
    # Setup layar curses
    curses.curs_set(0)
    screen.nodelay(1)
    screen.clear()

    # Tampilkan judul game
    screen.addstr(0, 0, "=== TEBAK ANGKA ===", curses.A_BOLD)
    screen.addstr(2, 0, "1. Mulai permainan")
    screen.addstr(3, 0, "2. Keluar")

    # Animasikan pilihan menu
    x = 0
    y = 2
    while True:
        screen.addstr(y, x, ">")
        screen.refresh()
        time.sleep(0.1)
        screen.addstr(y, x, " ")
        screen.refresh()
        time.sleep(0.1)

        # Periksa masukan pengguna
        key = screen.getch()
        if key == curses.KEY_UP and y > 2:
            y -= 1
        elif key == curses.KEY_DOWN and y < 3:
            y += 1
        elif key == ord("\n"):
            if y == 2:
                play_game(screen)
            elif y == 3:
                break

    # Reset layar curses
    curses.curs_set(1)
    screen.nodelay(0)
    screen.clear()

def play_game(screen):
    # Kode permainan sama seperti contoh sebelumnya
    secret_number = random.randint(1, 100)
    guesses = []

    while len(guesses) < 10:
        try:
            guess = int(input("Tebak angka antara 1 dan 100: "))
        except ValueError:
            print("Mohon masukkan angka yang valid.")
            continue

        if guess == secret_number:
            print("Anda berhasil menebak angka!")
            break
        elif guess < secret_number:
            print("Angka yang Anda tebak terlalu kecil.")
        else:
            print("Angka yang Anda tebak terlalu besar.")

        guesses.append(guess)

    print("Jawaban yang benar adalah", secret_number)
    main_menu(screen)

if __name__ == "__main__":
    # Inisialisasi layar curses dan jalankan menu utama
    curses.wrapper(main_menu)
