import streamlit as st

# ==============================================================================
# SOBERANÍA OS v2.6 - WEB INTERFACE (STREAMLIT)
# ==============================================================================

# Configuración de la página web
st.set_page_config(page_title="Sinergia 360 - Ingeniería de Orden", page_icon="📊", layout="centered")

st.title("📊 Ingeniería de Orden: El Mapa del Impuesto al Desorden")
st.markdown("### Sinergia 360 System")
st.write("Bienvenido al cuestionario de diagnóstico estructural. Por favor, complete los siguientes datos.")

st.divider()

# Formulario para evitar recargas parciales mientras el cliente escribe
with st.form("cuestionario_orden"):
    
    # ----------------------------------------------------------------------
    # MÓDULO 1: VARIABLES DE IMPACTO Y FUGA
    # ----------------------------------------------------------------------
    st.subheader("Módulo 1: Variables de Impacto y Fuga")
    
    nombre_caso = st.text_input("Nombre de la Empresa o Caso:", placeholder="Ej. Mi PyME S.A.")
    dep_input = st.selectbox("¿Se va de vacaciones y el negocio opera de manera idéntica?", ["SI", "NO"])
    hp = st.number_input("Horas perdidas a la semana en 'bomberazos' y emergencias [HP]:", min_value=0, max_value=168, value=6)
    vhe = st.number_input("Valor estimado de tu hora estratégica en el mercado ($ MXN):", min_value=0.0, value=700.0)
    drenaje = st.number_input("Pérdidas anuales por errores operativos, multas o demandas ($ MXN):", min_value=0.0, value=0.0)
    st.selectbox("¿La utilidad es proporcional o el dinero se evapora?", ["PROPORCIONAL", "EVAPORA"])

    st.divider()

    # ----------------------------------------------------------------------
    # MÓDULO 2: EVALUACIÓN DEL PENTÁGONO
    # ----------------------------------------------------------------------
    st.subheader("Módulo 2: Evaluación del Pentágono (Escala 1 al 10)")
    st.caption("Asigna una calificación del 1 (Nulo/Fuga) al 10 (Soberanía/Blindado) para cada pilar.")

    pilar_a = st.slider("Pilar A: Orden (Procesos y reloj operativo)", 1, 10, 8)
    pilar_b = st.slider("Pilar B: Integridad (Contratos de acero y materialidad)", 1, 10, 1)
    pilar_c = st.slider("Pilar C: Disciplina (Rigor presupuestal y control de fugas)", 1, 10, 6)
    pilar_d = st.slider("Pilar D: Resiliencia (Blindaje patrimonial y gestión de crisis)", 1, 10, 1)
    pilar_e = st.slider("Pilar E: Trascendencia (Inversión automática de excedentes)", 1, 10, 1)

    enviar = st.form_submit_button("PROCESAR DIAGNÓSTICO")

# ----------------------------------------------------------------------
# MÓDULO 3: PROCESAMIENTO Y DASHBOARD VISUAL
# ----------------------------------------------------------------------
if enviar:
    SEMANAS_ANUALES = 52
    TASA_RIESGO_MENSUAL = 0.00416
    MESES_PROYECCION = 12

    co = hp * SEMANAS_ANUALES
    id_anual = (co * vhe) + drenaje
    factor_compuesto = (((1 + TASA_RIESGO_MENSUAL) ** MESES_PROYECCION) - 1) / TASA_RIESGO_MENSUAL
    vf = id_anual * factor_compuesto
    score_pentagono = (pilar_a + pilar_b + pilar_c + pilar_d + pilar_e) / 5.0

    st.divider()
    st.header(f"📈 Dashboard de Resultados: {nombre_caso.upper()}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Caos Anual", f"{co} hrs")
    col2.metric("Impuesto al Desorden", f"${id_anual:,.2f} MXN")
    col3.metric("Valor Futuro (12M)", f"${vf:,.2f} MXN")

    st.subheader(f"Score Estructural: {score_pentagono:.1f} / 10.0")

    t_cima = "[X]" if pilar_e > 5 else "[ ]"
    m_izq = "[X]" if pilar_c > 5 else "[ ]"
    m_der = "[X]" if pilar_d > 5 else "[ ]"
    b_izq = "[X]" if pilar_a > 5 else "[ ]"
    b_der = "[X]" if pilar_b > 5 else "[ ]"

    grafico_web = f"""
    ```text
                   {t_cima} TRASCENDENCIA ({pilar_e})
                          /\\
                         /  \\
                        /    \\
 	DISCIPLINA ({pilar_c}) {m_izq}   /______\\   {m_der} RESILIENCIA ({pilar_d})
                      \\      /
                       \\    /
                        \\  /
           ORDEN ({pilar_a}) {b_izq}  \\/  {b_der} INTEGRIDAD ({pilar_b})
    ```
    """
    st.markdown("#### Geometría del Pentágono de la Economía")
    st.markdown(grafico_web)

    if score_pentagono < 5.0 or id_anual > 100000:
        st.error("🚨 **SEMÁFORO ROJO: ZONA DE DESASTRE ESTRUCTURAL**\n\n*Interfaz suspendida para la descarga de formatos genéricos. Redirección obligatoria a Diagnóstico General Profundo corporativo.*")

    if pilar_b <= 5 or pilar_d <= 5:
        st.warning("⚠️ **ALERTA: RIESGO DE OPERACIONES SIMULADAS Y VULNERABILIDAD PATRIMONIAL**\n\n*Se requiere la instrumentación inmediata de Contratos de Acero con Fecha Cierta (NOM-151), cláusulas estrictas de materialidad y bitácoras de Prueba de Vida.*")

    if pilar_a > 6 and pilar_b <= 4: st.info("🔮 **ALERTA: EL ESPEJISMO DEL ORDEN**\n\n*La operación fluye pero carece de chasis legal preventivo. Riesgo de erosión de confianza inminente.*")
