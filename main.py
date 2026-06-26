import streamlit as st
from datetime import datetime, date, time, timedelta
import json

st.title("Castillo Enchantix")

user_name = st.text_input("Nombre")

eventos_disponibles = "Boda Real", "Coronacion", "Nombramiento de Caballeros"

evento_name = st.selectbox("Elija un evento", eventos_disponibles)

fecha = st.date_input("Elija la fecha", min_value = date.today(), max_value = date.today() + timedelta(days = 365))

hora_inicio = st.time_input("Elija la hora de inicio del evento", value = time(12, 0))

hora_fin = st.time_input("Elija la hora de fin del evento", value = time(12, 0))

if evento_name == "Boda Real":
    recursos_boda = "Sacerdote", "Musica", "Bardos", "Arco de flores", "Arco de laureles"
    recursos = st.multiselect("Elija los recursos", recursos_boda)
elif evento_name == "Coronacion":
    recursos_coronacion = "Corona", "Musica", "Bardos", "Palomas"
    recursos = st.multiselect("Elija los recursos", recursos_coronacion)
else:
    recursos_caballeros = "Espada", "Rey", "Reina", "Trompetas", "Palomas"
    recursos = st.multiselect("Elija los recursos", recursos_caballeros)

class Evento:
    def __init__(self, user_name, evento_name, fecha, hora_inicio, hora_fin, recursos):
        self.user_name = user_name
        self.evento_name = evento_name
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.recursos = recursos

    def restricciones(self):
        errores = False
        if not self.user_name:
            st.error("Inserte su nombre")
            errores = True
        elif not self.evento_name:
            st.error("Inserte un evento")
            errores = True
        elif not self.fecha:
            st.error("Inserte una fecha")
            errores = True
        elif not self.hora_inicio:
            st.error("Inserte una hora de inicio")
            errores = True
        elif not self.hora_fin:
            st.error("Inserte una hora de fin")
            errores = True
        hora_min = time(9, 0)
        hora_max = time(17, 0)
        if self.hora_inicio < hora_min or self.hora_inicio > hora_max:
            st.error("La hora de inicio debe estar entre 9:00 y 15:00")
            errores = True
        elif hora_fin < hora_min or hora_fin > hora_max:
            st.error("La hora de fin debe estar entre 11:00 y 17:00")
            errores = True
        elif self.hora_inicio >= self.hora_fin:
            st.error("La hora de inicio no puede ser despues de la hora de fin")
            errores = True
        inicio_dt = datetime.combine(self.fecha, self.hora_inicio)
        fin_dt = datetime.combine(self.fecha, self.hora_fin)
        duracion = fin_dt - inicio_dt
        if duracion < timedelta(hours = 2):
            st.error("El evento debe durar al menos dos horas")
            errores = True
        elif duracion > timedelta(hours = 8):
            st.error("El evento no puede durar mas de ocho horas")
            errores = True            
        elif "Boda Real" in self.evento_name:
            if "Sacerdote" not in self.recursos:
                st.error("No se puede realizar una boda sin un sacerdote")
                errores = True
            if "Musica" in self.recursos and "Bardos" not in self.recursos:
                st.error("No se puede tener musica sin los bardos")
                errores = True
            if "Arco de flores" in self.recursos and "Arco de laureles" in self.recursos:
                st.error("No se puede utilizar un arco de flores y un arco de laureles a la vez")
                errores = True
        elif "Coronacion" in self.evento_name:
            if "Corona" not in self.recursos:
                st.error("No se puede realizar una coronacion sin una corona")
                errores = True
            if "Musica" in self.recursos and "Bardos" not in self.recursos:
                st.error("No se puede tener musica sin los bardos")
                errores = True
            if "Musica" in self.recursos and "Palomas" in self.recursos:
                st.error("No se puede tener musica y palomas a la vez")
                errores = True
        elif "Nombramiento de caballeros" in self.evento_name:
            if "Espada" not in self.recursos:
                st.error("No se puede nombrar a un caballero sin una espada")
                errores = True
            if "Rey" in self.recursos and "Reina" not in self.recursos:
                st.error("El Rey no puede estar presente sin la Reina")
                errores = True
            if "Trompetas" in self.recursos and "Palomas" in self.recursos:
                st.error("No se pueden usar las trompetas y las palomas a la vez")
                errores = True
        return not errores 
        
    def guardar_evento(self):
        evento_dicc = {
            "nombre del usuario" : self.user_name,
            "nombre del evento" : self.evento_name,
            "fecha del evento" : str(self.fecha),
            "hora de inicio del evento" : str(self.hora_inicio),
            "hora de fin del evento" : str(self.hora_fin),
            "recursos del evento" : self.recursos
        }

        try:
            with open("eventos.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(evento_dicc)

        with open("eventos.json", "w") as f:
            json.dump(data, f, indent = 4)

        st.success("Evento guardado exitosamente")

if st.button("Guardar evento"):
    evento = Evento(user_name, evento_name, fecha, hora_inicio, hora_fin, recursos)
    if evento.restricciones():
        evento.guardar_evento()

def cargar_eventos():
    try:
        with open("eventos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_eventos(data):
    with open("eventos.json", "w") as f:
        json.dump(data, f, indent=4)

eventos_guardados = cargar_eventos()
if eventos_guardados:
    opciones = [f"{i+1}. {ev['nombre del evento']} - {ev['fecha del evento']} ({ev['nombre del usuario']})"
                for i, ev in enumerate(eventos_guardados)]
    seleccion = st.selectbox("Elija un evento", opciones)

    if st.button("Eliminar evento"):
        indice = opciones.index(seleccion)
        eliminado = eventos_guardados.pop(indice)
        guardar_eventos(eventos_guardados)
        st.success(f"Evento eliminado: {eliminado['nombre del evento']} del usuario {eliminado['nombre del usuario']}")
else:
    st.info("No hay eventos guardados")