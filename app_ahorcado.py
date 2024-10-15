import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE_AGUA = (0, 255, 200)  # Color verde agua sólido
VERDE_AGUA_TRANSLUCIDO = (0, 255, 200, 128)  # Color verde agua translúcido

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Juego del Ahorcado')

# Fuentes
FUENTE_GRANDE = pygame.font.SysFont('comicsans', 60)
FUENTE_MEDIA = pygame.font.SysFont('comicsans', 30)  # Tamaño más pequeño para los botones
FUENTE_PEQUEÑA = pygame.font.SysFont('comicsans', 25)

# Cargar imágenes del ahorcado y fondo
imagenes_ahorcado = []
for i in range(6):
    imagen = pygame.image.load(f'ahorcado{i}.png')
    imagen = pygame.transform.scale(imagen, (int(ANCHO * 0.7), int(ALTO * 0.7)))  #
    imagenes_ahorcado.append(imagen)

fondo_menu = pygame.image.load('inicio3.png')
fondo_menu = pygame.transform.scale(fondo_menu, (int(ANCHO * 0.7), int(ALTO * 0.7)))  #

# Cargar la imagen inicial del ahorcado
imagen_inicial = pygame.image.load('ahorcado.png')
imagen_inicial = pygame.transform.scale(imagen_inicial, (int(ANCHO * 0.5), int(ALTO * 0.5)))

# Cargar sonido de clic
try:
    sonido_clic = pygame.mixer.Sound('sonido2.wav')  
except pygame.error:
    print("Error al cargar el sonido.")

# Palabras para el juego
palabras = ["python", "programacion", "ahorcado", "desarrollador", "computadora", "Variable", "Función", "objeto", "metodo", "Compilador", "Sintaxis", "Algoritmo", "Parámetro"]

# Función para elegir una palabra al azar
def elegir_palabra():
    return random.choice(palabras)

# Función para dibujar la palabra
def mostrar_palabra(pantalla, palabra, letras_adivinadas):
    estado_palabra = ' '.join(letra if letra in letras_adivinadas else '_' for letra in palabra)
    texto = FUENTE_GRANDE.render(estado_palabra, True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2))

# Función para mostrar mensajes en una ventana verde agua translúcida
def mostrar_mensaje_nueva_ventana(mensaje):
    ventana_mensaje = pygame.Surface((500, 250), pygame.SRCALPHA)  # Aumentar el tamaño
    ventana_mensaje.fill(VERDE_AGUA_TRANSLUCIDO)
    texto = FUENTE_PEQUEÑA.render(mensaje, True, NEGRO)
    ventana_mensaje.blit(texto, (ventana_mensaje.get_width() // 2 - texto.get_width() // 2, ventana_mensaje.get_height() // 2 - texto.get_height() // 2))

    pantalla.blit(ventana_mensaje, (ANCHO // 2 - 250, ALTO // 2 - 125))  # Centrar la ventana en la pantalla
    pygame.display.update()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                esperando = False

# Juego del ahorcado
def juego_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos = 6

    corriendo = True
    while corriendo:
        pantalla.fill(BLANCO)
        pantalla.blit(imagenes_ahorcado[6 - intentos], (ANCHO // 4, ALTO // 5))  
        mostrar_palabra(pantalla, palabra_secreta, letras_adivinadas)

        letras_incorrectas = [letra for letra in letras_adivinadas if letra not in palabra_secreta]
        texto_incorrectas = FUENTE_MEDIA.render("Letras incorrectas: " + ', '.join(letras_incorrectas), True, NEGRO)
        pantalla.blit(texto_incorrectas, (20, 500))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                letra = chr(evento.key).lower()
                if letra.isalpha() and letra not in letras_adivinadas:
                    letras_adivinadas.append(letra)
                    if letra not in palabra_secreta:
                        intentos -= 1

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            mostrar_mensaje_nueva_ventana("¡Ganaste!")
            corriendo = False
        if intentos == 0:
            mostrar_mensaje_nueva_ventana(f"Perdiste. La palabra era: {palabra_secreta}")
            corriendo = False

        pygame.display.update()

# Menú Principal
def mostrar_menu():
    pantalla.fill(BLANCO)
    pantalla.blit(imagen_inicial, (ANCHO // 4, ALTO // 4))  # Mostrar la imagen inicial en el centro
    pygame.display.update()
    pygame.time.delay(1500)  # Esperar 1.5 segundos

    while True:
        pantalla.fill(BLANCO)
        pantalla.blit(fondo_menu, (ANCHO // 2 - fondo_menu.get_width() // 2, ALTO // 2 - fondo_menu.get_height() // 2))  # Centrar imagen

        texto_menu = FUENTE_GRANDE.render("Juego del Ahorcado", True, NEGRO)
        pantalla.blit(texto_menu, (ANCHO // 2 - texto_menu.get_width() // 2, 50))
        
        boton_jugar = pygame.Rect(50, ALTO - 100, 200, 50)
        pygame.draw.rect(pantalla, VERDE_AGUA, boton_jugar)  #  fondo a verde agua
        texto_jugar = FUENTE_MEDIA.render("JUGAR", True, NEGRO)   
        pantalla.blit(texto_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
        
        boton_salir = pygame.Rect(ANCHO - 250, ALTO - 100, 200, 50)
        pygame.draw.rect(pantalla, VERDE_AGUA, boton_salir)
        texto_salir = FUENTE_MEDIA.render("SALIR", True, NEGRO)
        pantalla.blit(texto_salir, (boton_salir.x + 50, boton_salir.y + 10))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    sonido_clic.play()
                    juego_ahorcado()
                elif boton_salir.collidepoint(evento.pos):
                    sonido_clic.play()
                    pygame.quit()
                    return

# Ejecutar el juego
mostrar_menu()

# Finalizar Pygame
pygame.quit()

