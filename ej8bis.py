import random
import sys  # para usar sys.exit

# Preguntas, respuestas y respuestas correctas
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1]

# Unimos todo en una sola lista de tuplas (pregunta, respuestas, índice correcto)
qa_list = list(zip(questions, answers, correct_answers_index))

# Seleccionamos 3 preguntas distintas al azar
questions_to_ask = random.sample(qa_list, k=3)

# Variable para puntaje
score = 0

# Recorremos las preguntas
for question, options, correct_answers_index in questions_to_ask:
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    # El usuario tiene 2 intentos
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print("Respuesta no válida")
            sys.exit(1)  # salir con código de error 1

        # Verificamos que esté en rango
        if user_answer < 0 or user_answer >= len(options):
            print("Respuesta no válida")
            sys.exit(1)

        # Verificamos si es correcta
        if user_answer == correct_answers_index:
            print("¡Correcto!")
            score += 1  # acierto suma 1
            break
        else:
            print("Incorrecto.")
            score -= 0.5  # fallo resta 0.5
            if intento == 1:  # si fue el último intento, mostrar respuesta
                print("La respuesta correcta es:", options[correct_answers_index])

    print()  # línea en blanco después de cada pregunta

# Mostrar puntaje final
print(f"Tu puntaje final es: {score}")
