usuario = {
    "nombre": "Ana",
    "edad": 17,
    "rol": "alumno",      # Puede ser: "alumno", "profesor", "invitado"
    "nota": 6.5,          # Número entre 0 y 10 (puede ser inválido). Indiferente para profesor.
    "activo": True        # Indica si el usuario está activo en el sistema
}

# Verificar si el usuario está activo
if usuario ["activo"]:
    match usuario["rol"]:
        # Evaluar el rol del usuario
        case "alumno":
            # Evaluar la nota del alumno
            if usuario["nota"] >= 0 and usuario["nota"] <= 10:
                if usuario["nota"] < 5:
                    print(f"Suspenso")
                elif usuario["nota"] >= 5 and usuario["nota"] < 7:
                    print(f"Aprobado")
                elif usuario["nota"] >= 7 and usuario["nota"] < 9:
                    print(f"Notable")
                else:
                    print(f"Excelente")
            else:
                print(f"Nota no valida")

            # Evaluar la edad del alumno
            if usuario["edad"] < 18:
                print(f"Alumno menor de edad")
            else:
                print(f"Alumno mayor de edad")

            # Evaluar el estado académico del alumno utilizando un operador ternario
            estado_academico = "Promociona" if usuario["nota"] >= 5 else "No promociona"
            print(f"Estado académico: {estado_academico}")
            
        # Evaluar otros roles
        case "profesor":
            print(f"Acceso como profesor. No se requiere evaluación.")
        case "invitado":
            print(f"Acceso limitado como invitado.")
        case _:
            print(f"Rol no reconocido.")
        
