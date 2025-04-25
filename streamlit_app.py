# streamlit_app.py
import streamlit as st

def main():
    st.set_page_config(page_title="Cuestionario de Madurez CRM", layout="centered")
    st.title("🧠 Cuestionario de Madurez Digital CRM - Sector Hotelero")

    st.markdown("Responde a las siguientes preguntas para evaluar el nivel de madurez digital de tu hotel:")

    resultados = []

    # Pregunta 1
    r1 = st.radio(
        "¿El hotel gestiona más de 30 reservas mensuales?",
        ["-30", "30-100", "+100"],
        index=1
    )
    resultados.append(("Reservas mensuales", r1))

    # Pregunta 2
    r2 = st.radio(
        "¿Tienes más de un punto de venta en el hotel (restaurante, bar, spa)?",
        ["No", "Sí", "Sí y gestión separada o integrada"],
        index=0
    )
    resultados.append(("Puntos de venta", r2))

    # Pregunta 3
    r3 = st.radio(
        "¿Tienes registros digitalizados de al menos el 70% de tus huéspedes?",
        ["-70%", "70-90%", "90%"],
        index=1
    )
    resultados.append(("Digitalización huéspedes", r3))

    # Pregunta 4
    r4 = st.radio(
        "¿Más del 40% de tus huéspedes son recurrentes?",
        ["No", "Sí (-60%)", "Sí (+60%)"],
        index=0
    )
    resultados.append(("Huéspedes recurrentes", r4))

    # Pregunta 5
    r5 = st.radio(
        "¿Tienes un procedimiento de protección de datos (RGPD)?",
        ["No", "Sí (básico)", "Sí (auditorias)"],
        index=1
    )
    resultados.append(("Protección de datos", r5))

    # Pregunta 6
    r6 = st.radio(
        "¿Tienes KPIs definidos sobre experiencia del cliente (NPS, tasa de repetición, etc.)?",
        ["No", "Sí (básicos)", "Sí (revisiones periódicas)"],
        index=1
    )
    resultados.append(("KPIs de cliente", r6))

    st.markdown("---")
    if st.button("📊 Evaluar madurez"):
        st.subheader("Tus respuestas:")
        for pregunta, respuesta in resultados:
            st.write(f"**{pregunta}**: {respuesta}")
        st.success("¡Evaluación completada! Puedes seguir añadiendo más lógica para puntuar las respuestas.")

if __name__ == "__main__":
    main()
