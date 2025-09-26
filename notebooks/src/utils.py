def calcular_puntaje(stats: dict) -> int:
    """Calcula el puntaje de un equipo en una ronda.
       :param stats: diccionario de estadisticas de un equipo.
       :return: puntaje total de la ronda.
    """
    return stats["innovacion"] * 3 + stats["presentacion"] - int(stats["errores"])


def procesar_ronda(ronda: dict, acumulados: dict) -> tuple:
    """
    Procesa una ronda de evaluación, actualiza los acumulados y devuelve los resultados.
    :param ronda: diccionario de estadisticas de un equipo.
    :param acumulados: diccionario de acumulado de estadisticas de un equipo.
    :return:  tupla-->(Nombre del mejor equipo x Ronda , Puntaje de ese equipo, diccionario de estadisticas de la ronda).
    """
    #map() para calcular los puntajes de la ronda en una sola línea.
    puntajes_ronda = dict(map(lambda item: (item[0], calcular_puntaje(item[1])), ronda.items()))
    
    stats_ronda = {}
    
    for equipo, stats in ronda.items():
        puntos = puntajes_ronda[equipo]
        
        # Inicializa acumulados si no existe el equipo
        if equipo not in acumulados:
            acumulados[equipo] = {
                "innovacion": 0,
                "presentacion": 0,
                "errores": 0,
                "mejores": 0,
                 "puntos": 0
            }
        
        # Actualizar stats para la tabla de la ronda
        stats_ronda[equipo] = {
            "innovacion": stats["innovacion"]*3,
            "presentacion": stats["presentacion"],
            "errores": int(stats["errores"]),
            "mejores": 0,
            "puntos": puntos
        }
        
        # Actualiza acumulados
        acumulados[equipo]["innovacion"] += (stats["innovacion"]*3)
        acumulados[equipo]["presentacion"] += stats["presentacion"]
        acumulados[equipo]["errores"] += int(stats["errores"])
        acumulados[equipo]["puntos"] += puntos

    # Determina el mejor equipo de la ronda
    mejor_equipo = max(puntajes_ronda, key=puntajes_ronda.get)
    stats_ronda[mejor_equipo]["mejores"] = 1
    acumulados[mejor_equipo]["mejores"] += 1
    
    return mejor_equipo, puntajes_ronda[mejor_equipo], stats_ronda


def mostrar_tabla(stats_dict: dict, titulo):
    """Muestra tabla con formato de acumulados, puede usarse para rondas o final.
       :param stats_dict: diccionario de estadisticas de la Ronda.
       :param titulo: Titulo de la tabla.
    """
    print(titulo)
    print(f"{'Equipo':<10} {'Inno':<5} {'Pres':<5} {'Err':<5} {'MER':<5} {'Total':<5}")
    print("-" * 40)

    #Lista de tuplas ordenadas equipo:dict de stats
    ordenados = sorted(stats_dict.items(), key=lambda x: x[1]["puntos"], reverse=True)
    for equipo, stats in ordenados:
        print(f"{equipo:<10} {stats.get('innovacion', 0):<5} "
              f"{stats.get('presentacion', 0):<5} {stats.get('errores', 0):<5} "
              f"{stats.get('mejores', 0):<5} {stats['puntos']:<5}")