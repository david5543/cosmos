import subprocess
from PIL import Image, ImageTk
import tkinter as tk
import pygame
from pygame import mixer
import random

mixer.init()
window = tk.Tk()
window.geometry('1000x600')
window.title('Conociendo los cosmos')

x = 150
y = 300
score = 0
speed = 10
game_over = False

img_bird = Image.open('images/astronauta1.png')
img_bird = ImageTk.PhotoImage(img_bird)

img_pipe_down = Image.open('images/pipe.png')           # 104x900
img_pipe_top = img_pipe_down.rotate(180)

img_pipe_down = ImageTk.PhotoImage(img_pipe_down)
img_pipe_top = ImageTk.PhotoImage(img_pipe_top)

img_reset1 = Image.open('images/regresar0.png')
img_reset1 = ImageTk.PhotoImage(img_reset1)

img_reset2 = Image.open('images/reiniciar.png')
img_reset2 = ImageTk.PhotoImage(img_reset2)

canvas = tk.Canvas(window, highlightthickness=0, bg='#00bfff')
canvas.place(relwidth=1, relheight=1)

text_score = canvas.create_text(50, 50, text='0', fill='white', font=('D3 Egoistism outline', 30))

bird = canvas.create_image(x, y, anchor='nw', image=img_bird)
pipe_top = canvas.create_image(1200, -550, anchor='nw', image=img_pipe_top)
pipe_down = canvas.create_image(1200, 550, anchor='nw', image=img_pipe_down)

mixer.music.load('audio/swoosh.wav')
mixer.music.play(loops=0)


def move_bird_key(event):
    global x, y
    if not game_over:
        y -= 30
        canvas.coords(bird, x, y)
        mixer.music.load('audio/wing.wav')
        mixer.music.play(loops=0)


window.bind("<space>", move_bird_key)


def move_bird():
    global x, y
    y += 5
    canvas.coords(bird, x, y)
    if y < 0 or y > window.winfo_height():
        game_end()

    if not game_over:
        window.after(50, move_bird)


def show_message():
    if score == 0 and score ==0:  # Mostrar mensaje cada vez que el puntaje sea 1
        message = canvas.create_text(500, 300, text="Aprendamos sobre nuestro universo", fill="white",
            font=("D3 Egoistism outline", 17))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score ==1:  # Mostrar mensaje cada vez que el puntaje sea 1
        message = canvas.create_text(500, 300, text="Tierra: Nuestro hogar, con un diámetro de alrededor de 12,742 kilómetros.", fill="white",
            font=("D3 Egoistism outline", 15))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos

    if score > 0 and score ==2:  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text="Mercurio: Es el planeta más pequeño del sistema solar.", fill="white",
            font=("D3 Egoistism outline", 20))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score ==3:  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text="Venus es el planeta más brillante en el cielo nocturno", fill="white",
            font=("D3 Egoistism outline", 20))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score ==4:  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text="Júpiter: Es el gigante gaseoso más grande del sistema solar", fill="white",
            font=("D3 Egoistism outline", 20))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score ==5:  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text=" Saturno concido pos sus enormes anillos, tiene un diámetro alrededor de 9 veces el de la Tierra.", fill="white",
            font=("D3 Egoistism outline", 15))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score ==6:  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text="Urano: Es un planeta gaseoso con un diámetro aproximadamente 4 veces el de la Tierra.", fill="white",
            font=("D3 Egoistism outline", 15))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score ==7:  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text="Neptuno: Similar a Urano, Neptuno es también un gigante gaseoso ", fill="white",
            font=("D3 Egoistism outline", 15))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos
    if score > 0 and score >7 :  # Mostrar mensaje cada vez que el puntaje sea 2
        message = canvas.create_text(500, 300, text="Continua el siguiente juego, ya aprendimos lo basico ", fill="white",
            font=("D3 Egoistism outline", 20))
        window.after(100, lambda: canvas.delete(message))  # Eliminar el mensaje después de 2 segundos

def move_pipe():
    global score, game_over, speed
    canvas.move(pipe_top, -speed, 0)
    canvas.move(pipe_down, -speed, 0)
    if canvas.coords(pipe_down)[0] < -100:
        score += 1
        speed += 1
        canvas.itemconfigure(text_score, text=str(score))
        h = window.winfo_height()
        num = random.choice([i for i in range(160, h, 160)])
        canvas.coords(pipe_down, window.winfo_width(), num + 160)
        canvas.coords(pipe_top, window.winfo_width(), num - 900)

    if 0 < canvas.coords(pipe_down)[0] < 160:
        channel = mixer.Channel(1)
        channel.set_volume(1.0)
        sound = mixer.Sound('audio/point.wav')
        channel.play(sound, loops=0)

    if canvas.coords(pipe_down):
        if canvas.bbox(bird)[0] < canvas.bbox(pipe_down)[2] and canvas.bbox(bird)[2] > canvas.bbox(pipe_down)[0]:
            if canvas.bbox(bird)[1] < canvas.bbox(pipe_top)[3] or canvas.bbox(bird)[3] > canvas.bbox(pipe_down)[1]:
                game_end()
    if not game_over:
        show_message()
        window.after(50, move_pipe)


def reset_game():
    global x, y, score, speed, game_over
    x = 150
    y = 300
    score = 0
    speed = 10
    game_over = False
    canvas.coords(bird, x, y)
    canvas.coords(pipe_top, 1200, -550)
    canvas.coords(pipe_down, 1200, 550)
    canvas.itemconfigure(text_score, text="0")
    lbl_game_over.place_forget()
    bt_reset1.place_forget()
    bt_reset2.place_forget()
    move_bird()
    move_pipe()
    mixer.music.load('audio/swoosh.wav')
    mixer.music.play(loops=0)


def game_end():
    global game_over
    game_over = True
    lbl_game_over.place(relx=0.5, rely=0.5, anchor='center')
    bt_reset1.place(relx=0.4, rely=0.7, anchor='center')
    bt_reset2.place(relx=0.6, rely=0.7, anchor='center')
    mixer.music.load('audio/hit.wav')
    mixer.music.play(loops=0)
    while mixer.music.get_busy():
        continue
    mixer.music.load('audio/die.wav')
    mixer.music.play(loops=0)


def open_another_file():
    window.destroy()
    subprocess.run(["python", "index.py"])  # Reemplaza "another_file.py" con el nombre del archivo a ejecutar

lbl_game_over = tk.Label(window, text='Fin de Juego! Puedes Volver a jugar o Continuar', font=('D3 Egoistism outline', 30), fg='white', bg='#00bfff')
bt_reset1 = tk.Button(window, border=0, image=img_reset1, activebackground='#00bfff', bg='#00bfff', command=open_another_file)
bt_reset2 = tk.Button(window, border=0, image=img_reset2, activebackground='#00bfff', bg='#00bfff', command=reset_game)

window.after(50, move_bird)
window.after(50, move_pipe)

window.call('wm', 'iconphoto', window._w, img_bird)
window.mainloop()
