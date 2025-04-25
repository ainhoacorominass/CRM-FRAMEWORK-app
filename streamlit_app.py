import streamlit as st

def main():
    st.set_page_config(page_title="Cuestionario de Madurez CRM", layout="centered")
    st.title("🧠 Cuestionario de Madurez Digital CRM - Sector Hotelero")

    if "fase" not in st.session_state:
        st.session_state.fase = "madurez"
        st.session_state.respuestas = {}
        st.session_state.prioridades = {}
        st.session_state.puntuacion_madurez = 0

    if st.session_state.fase == "madurez":
        st.markdown("Responde a las siguientes preguntas para evaluar el nivel de madurez digital de tu hotel:")

        respuestas_textos = [
            "¿Cuántas reservas mensuales gestiona el hotel?",
            "¿Dispone de más de un punto de venta en el hotel (restaurante, bar, spa)?",
            "¿Qué porcentaje de huéspedes tiene sus registros digitalizados?",
            "¿Cuál es el porcentaje de huéspedes recurrentes?",
            "¿Gestionas preferencias específicas de huéspedes (dietas, tipo de habitación)?",
            "¿Tienes implementado un procedimiento de protección de datos (RGPD)?",
            "¿Tienes definidos KPIs sobre la experiencia del cliente?",
            "¿Usas un PMS (Sistema de Gestión Hotelera)?",
            "¿Cuál es tu presupuesto anual para tecnología?"
        ]

        opciones_dict = {
            respuestas_textos[0]: ["Menos de 30 reservas", "Entre 30 y 100 reservas", "Más de 100 reservas"],
            respuestas_textos[1]: ["No dispone de puntos de venta adicionales", "Sí, algunos puntos adicionales", "Sí, con gestión separada o integrada"],
            respuestas_textos[2]: ["Menos del 70%", "Entre el 70% y 90%", "Más del 90%"],
            respuestas_textos[3]: ["Menos del 40%", "Entre 40% y 60%", "Más del 60%"],
            respuestas_textos[4]: ["No se gestionan preferencias", "Sí, datos básicos", "Sí, incluyendo hábitos y quejas"],
            respuestas_textos[5]: ["No existe protocolo", "Sí, básico", "Sí, con auditorías y revisión periódica"],
            respuestas_textos[6]: ["No se miden KPIs", "Sí, pero básicos", "Sí, con revisiones periódicas"],
            respuestas_textos[7]: ["No se utiliza PMS", "Sí, básico o limitado", "Sí, integrado con otros sistemas"],
            respuestas_textos[8]: ["Menos de 1.000 €", "Entre 1.000 € y 2.000 €", "Más de 2.000 €"]
        }

        for pregunta in respuestas_textos:
            st.session_state.respuestas[pregunta] = st.radio(f"**{pregunta}**", opciones_dict[pregunta], index=None)

        st.markdown("---")

        if st.button("📊 Evaluar nivel de madurez"):
            if None in st.session_state.respuestas.values():
                st.warning("❗ Por favor, responde a todas las preguntas antes de continuar.")
            else:
                puntuacion = 0
                for pregunta, respuesta in st.session_state.respuestas.items():
                    opciones = opciones_dict[pregunta]
                    puntuacion += opciones.index(respuesta) + 1

                st.session_state.puntuacion_madurez = puntuacion
                st.session_state.fase = "resultado_madurez"
                st.rerun()

    elif st.session_state.fase == "resultado_madurez":
        st.subheader("🔎 Resultado de madurez digital:")
        puntuacion = st.session_state.puntuacion_madurez

        if 9 <= puntuacion <= 15:
            st.markdown(f"### 🟠 **Madurez Baja** ({puntuacion} puntos)")
            st.info("""El hotel presenta un nivel de digitalización bajo o nulo.
Se recomienda comenzar con herramientas básicas de CRM para digitalizar reservas, contactos y comunicaciones.""")
        elif 16 <= puntuacion <= 22:
            st.markdown(f"### 🟡 **Madurez Media** ({puntuacion} puntos)")
            st.info("""El hotel tiene una base tecnológica en marcha, pero aún necesita optimizar procesos de fidelización, marketing y análisis de datos.""")
        elif 23 <= puntuacion <= 27:
            st.markdown(f"### 🟢 **Madurez Alta** ({puntuacion} puntos)")
            st.success("""El hotel dispone de una infraestructura digital sólida, orientada a maximizar la automatización, analítica predictiva e integración total de sistemas.""")
        else:
            st.error("Algo no cuadra con la puntuación. Por favor revisa las respuestas.")

        st.markdown("---")
        if st.button("➡️ Continuar priorización de áreas funcionales"):
            st.session_state.fase = "prioridades"
            st.success("✅ Ahora puedes priorizar las áreas funcionales más abajo ⬇️")

    if st.session_state.fase == "prioridades":
        st.header("🎯 Prioriza las áreas funcionales para tu futuro CRM")

        st.markdown("""
Selecciona para cada área qué prioridad tiene para ti:
- **1** ➔ Área prescindible  
- **2** ➔ Poca importancia  
- **3** ➔ Moderadamente importante  
- **4** ➔ Importante  
- **5** ➔ Área crítica e imprescindible  
""")

        areas_funcionales = [
            "Estructura Operativa",
            "Gestión de clientes",
            "Comunicación y marketing",
            "Automatización y tecnología",
            "Digitalización de datos",
            "Reporting y dashboards"
        ]

        for area in areas_funcionales:
            st.session_state.prioridades[area] = st.radio(
                f"Prioridad para **{area}**:",
                ["1", "2", "3", "4", "5"],
                index=None, horizontal=True
            )

        if st.button("✅ Finalizar encuesta"):
            if None in st.session_state.prioridades.values():
                st.warning("🚫 Por favor, prioriza todas las áreas funcionales antes de finalizar.")
            else:
                st.success("✅ ¡Encuesta completada correctamente!")
                st.write("### Resumen de prioridades seleccionadas:")
                for area, prioridad in st.session_state.prioridades.items():
                    st.write(f"**{area}** ➔ Prioridad {prioridad}/5")

if __name__ == "__main__":
    main()