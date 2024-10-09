import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Juego del Ahorcado')

# Fuentes
FUENTE_GRANDE = pygame.font.SysFont('comicsans', 60)
FUENTE_MEDIA = pygame.font.SysFont('comicsans', 40)
FUENTE_PEQUENA = pygame.font.SysFont('comicsans', 20)

# Cargar imágenes del ahorcado
imagenes_ahorcado = []
for i in range(7):
    imagen = pygame.image.load(f'ahorcado{i}.png')
    imagenes_ahorcado.append(imagen)

# Palabras para el juego
palabras = ["python", "programacion", "ahorcado", "desarrollador", "computadora"]

# Función para elegir una palabra al azar
def elegir_palabra():
    return random.choice(palabras)

# Función para dibujar la palabra con guiones bajos y letras adivinadas
def mostrar_palabra(pantalla, palabra, letras_adivinadas):
    estado_palabra = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            estado_palabra += letra + ' '
        else:
            estado_palabra += '_ '
    
    texto = FUENTE_GRANDE.render(estado_palabra, True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2))

# Función para mostrar mensajes de ganar o perder
def mostrar_mensaje(pantalla, mensaje):
    texto = FUENTE_GRANDE.render(mensaje, True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2))
    pygame.display.update()
    pygame.time.delay(2000)

# Juego del ahorcado
def juego_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos = 6
    letras_correctas = []
    
    # Bucle principal del juego
    corriendo = True
    while corriendo:
        pantalla.fill(BLANCO)

        # Dibujar la imagen del ahorcado
        pantalla.blit(imagenes_ahorcado[6 - intentos], (150, 100))

        # Mostrar la palabra con guiones bajos y letras adivinadas
        mostrar_palabra(pantalla, palabra_secreta, letras_adivinadas)

        # Dibujar letras incorrectas
        letras_incorrectas = [letra for letra in letras_adivinadas if letra not in palabra_secreta]
        texto_incorrectas = FUENTE_PEQUENA.render("Letras incorrectas: " + ', '.join(letras_incorrectas), True, NEGRO)
        pantalla.blit(texto_incorrectas, (20, 500))

        # Evento del teclado
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                letra = chr(evento.key).lower()
                if letra.isalpha() and letra not in letras_adivinadas:
                    letras_adivinadas.append(letra)
                    if letra not in palabra_secreta:
                        intentos -= 1

        # Condiciones de victoria o derrota
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            mostrar_mensaje(pantalla, "¡Ganaste!")
            corriendo = False
        if intentos == 0:
            mostrar_mensaje(pantalla, f"Perdiste. La palabra era: {palabra_secreta}")
            corriendo = False

        pygame.display.update()

# Ejecutar el juego
juego_ahorcado()

# Finalizar Pygame
pygame.quit()
