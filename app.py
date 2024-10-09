import random
import tkinter as tk
from tkinter import messagebox

# Funciones para el juego
def elegir_palabra():
    palabras = ["python", "programacion", "ahorcado", "desarrollador", "computadora"]
    return random.choice(palabras)

def mostrar_estado():
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    return estado.strip()

def dibujar_hombre(intentos):
    etapas = [
        "  -----  \n  |     |  \n  |     O  \n  |    /|\\ \n  |    / \\ \n  |      \n---------",
        "  -----  \n  |     |  \n  |     O  \n  |    /|\\ \n  |    /   \n  |      \n---------",
        "  -----  \n  |     |  \n  |     O  \n  |    /|\\ \n  |          \n  |      \n---------",
        "  -----  \n  |     |  \n  |     O  \n  |     |  \n  |          \n  |      \n---------",
        "  -----  \n  |     |  \n  |     O  \n          \n  |          \n  |      \n---------",
        "  -----  \n  |     |  \n          \n          \n  |          \n  |      \n---------"
    ]
    return etapas[intentos]

def hacer_adivinanza():
    global intentos
    letra = letra_entry.get().lower()
    
    if letra in letras_adivinadas:
        messagebox.showinfo("Info", "Ya has adivinado esa letra. Intenta de nuevo.")
        return

    letras_adivinadas.append(letra)

    if letra not in palabra_secreta:
        intentos -= 1
        messagebox.showinfo("Info", "¡Letra incorrecta!")

    estado_actual = mostrar_estado()
    estado_label.config(text=estado_actual)
    dibujo_label.config(text=dibujar_hombre(intentos))
    
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        messagebox.showinfo("Felicidades", f"¡Has adivinado la palabra: {palabra_secreta}!")
        reiniciar_juego()
    elif intentos == 0:
        messagebox.showinfo("Perdiste", f"¡Perdiste! La palabra era: {palabra_secreta}")
        reiniciar_juego()

def reiniciar_juego():
    global palabra_secreta, letras_adivinadas, intentos
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos = 5
    estado_label.config(text=mostrar_estado())
    dibujo_label.config(text=dibujar_hombre(intentos))
    letra_entry.delete(0, tk.END)

# Inicializar la ventana
root = tk.Tk()
root.title("Juego del Ahorcado")

# Variables globales
palabra_secreta = elegir_palabra()
letras_adivinadas = []
intentos = 5

# Widgets
estado_label = tk.Label(root, text=mostrar_estado(), font=("Helvetica", 24))
estado_label.pack(pady=20)

dibujo_label = tk.Label(root, text=dibujar_hombre(intentos), font=("Courier", 16))
dibujo_label.pack(pady=20)

letra_entry = tk.Entry(root, font=("Helvetica", 20))
letra_entry.pack(pady=10)

adivinanza_button = tk.Button(root, text="Adivinar letra", command=hacer_adivinanza, font=("Helvetica", 16))
adivinanza_button.pack(pady=10)

# Iniciar el juego
estado_label.config(text=mostrar_estado())
dibujo_label.config(text=dibujar_hombre(intentos))

# Ejecutar la aplicación
root.mainloop()
