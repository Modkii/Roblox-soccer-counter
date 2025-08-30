import time

def soccer_timer():
    real_time = 17  ###17 segundos = 1 minuto do robok
    game_minute = 0

    ####first half
    print("primeiro tempo")
    while game_minute < 45:
        game_minute += 1
        print(f"Minuto {game_minute} do primeiro tempo")
        time.sleep(real_time)

    print("\nFim do primeiro tempo")

    ###press enter to start second half
    input("Pressione enter para iniciar o segundo tempo...")

    ###second half
    print("\nsegundo tempo")
    while game_minute < 90:
        game_minute += 1
        print(f"Minuto {game_minute} do segundo tempo")
        time.sleep(real_time)

    print("\nFim do segundo tempo")


soccer_timer()

###CADE LIZPINGUIM???
