from tkinter import *
from pickle import dump, load

from menu import canvas, window


def pause_toggle():
    global pause
    pause = not pause
    if pause:
        set_status('ПАУЗА')
    else:
        set_status('Вперед')

def save_game(event):
    x1 = canvas.coords(player1_id) [0]
    x2 = canvas.coords(player2_id) [0]
    data = [x1, x2]
    with open ('save.dat', 'wb') as f:
        dump(data, f)
        set_status('Сохранено')

def load_game(event):
    global x1, x2
    with open ('save.dat', 'wb') as f:
        data = load(f)
        x1, x2 = data
        canvas.coords(player1_id, x1, y1, x1 + player_size, y1 + player_size)
        canvas.coords(player2_id, x2, y2, x2 + player_size, y2 + player_size)
        set_status('Загружено')

def key_handler(event):
    if game_over:
        return

    if event.keycode == KEY_PAUSE:
        pause_toggle()

    if pause:
        return

    set_status('Вперёд!')

    if event.keycode == KEY_FORWARD1:
        canvas.move(player1_id, SPEED, 0)
    elif event.keycode == KEY_FORWARD2:
        canvas.move(player2_id, SPEED, 0)

    check_finish()

def set_status(status_text, color='black'):
    canvas.itemconfig(text_status_id, text=status_text, fill=color)

def check_finish():
    global game_over
    coords_player1 = canvas.coords(player1_id)
    coords_player2 = canvas.coords(player2_id)
    coords_finish = canvas.coords(finish_id)

    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]

    if x1_right >= x_finish:
        set_status('Победа верхнего игрока', player1_color)
        game_over = True
    if x2_right >= x_finish:
        set_status('Победа нижнего игрока', player2_color)
        game_over = True

KEY_FORWARD1 = 39
KEY_FORWARD2 = 68
KEY_PAUSE = 19

game_width = 800
game_height = 800
game_over = False
pause = False

player_size = 100
SPEED = 12
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'
x_finish = game_width - 50

window = Tk()
window.title('Догони меня, если сможешь')
canvas = Canvas(window)


