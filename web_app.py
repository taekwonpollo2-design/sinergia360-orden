import streamlit as st

# ==============================================================================
# SOBERANÍA OS v2.6 (REV. LABORATORY 2026) - WEB INTERFACE
# DESIGNED FOR: SINERGIA 360 SYSTEM
# DEVELOPER: LUIS ALBERTO RETANA HERNÁNDEZ (EL ARQUITECTO DE LA CERTEZA)
# ==============================================================================

# Configuración de la página web e identidad visual
st.set_page_config(
    page_title="Sinergia 360 - Ingeniería de Orden", 
    page_icon="📊", 
    layout="centered"
)

st.title("📊 Ingeniería de Orden: El Mapa del Impuesto al Desorden")
st.markdown("### Sinergia 360 System | Sostenibilidad Empresarial")
st.write("Bienvenido al cuestionario de diagnóstico estructural. Por favor, complete los siguientes datos para calcular el impacto financiero y legal del desorden operativo en su organización.")

st.divider()

# Formulario unificado para control de envío de datos del cliente
with st.form("cuestionario_orden"):
    
    # ----------------------------------------------------------------------
    # MÓDULO 1: VARIABLES DE IMPACTO Y FUGA (INPUTS)
    # ----------------------------------------------------------------------
    st.subheader("Módulo 1: Variables de Impacto y Fuga")
    
    nombre_caso = st.text_input("Nombre de la Empresa o Caso:", placeholder="Ej. Mi PyME S.A.")
    
    dep_input = st.selectbox("¿Se va de vacaciones y el negocio opera de manera idéntica sin usted?", ["SI", "NO"])
    
    hp = st.number_input("Horas perdidas a la semana en 'bomberazos' y emergencias [HP]:", min_value=0, max_value=168, value=6)
    vhe = st.number_input("Valor estimado de tu hora estratégica en el mercado ($ MXN):", min_value=0.0, value=700.0)
    drenaje = st.number_input("Pérdidas anuales por errores operativos, multas, recargos o demandas [Drenaje] ($ MXN):", min_value=0.0, value=0.0)
    
    st.selectbox("¿La utilidad es proporcional al esfuerzo o el dinero se evapora?", ["PROPORCIONAL", "EVAPORA"])

    st.divider()

    # ----------------------------------------------------------------------
    # MÓDULO 2: EVALUACIÓN DEL PENTÁGONO (PREGUNTAS PRECISAS)
    # ----------------------------------------------------------------------
    st.subheader("Módulo 2: Evaluación Estructural (Escala 1 al 10)")
    st.caption("Asigne una calificación del 1 (Nulo / Riesgo Total) al 10 (Soberanía / Blindado absoluto) para cada pilar rector.")

    pilar_a = st.slider("Pilar A. Orden. ¿Sus procesos están tan claros que el negocio funciona como un reloj sin que usted dé una sola instrucción diaria?", 1, 10, 5)
    pilar_b = st.slider("Pilar B. Integridad. ¿Su materialidad jurídica (contratos, evidencias, reportes) es tan sólida que podría pasar una auditoría sin avisar mañana?", 1, 10, 5)
    pilar_c = st.slider("Pilar C. Disciplina. ¿Tiene el rigor de seguir su presupuesto y sus procesos al 100%, sin permitir 'fugas' de efectivo por impulsos o descontrol?", 1, 10, 5)
    pilar_d = st.slider("Pilar D. Resiliencia. ¿Su patrimonio está blindado legal y financieramente contra crisis externas, demandas o su propia ausencia prolongada?", 1, 10, 5)
    pilar_e = st.slider("Pilar E. Trascendencia. ¿Tiene hoy un sistema donde el dinero rescatado se invierte automáticamente para crear su legado y libertad futura?", 1, 10, 5)

    enviar = st.form_submit_button("PROCESAR DIAGNÓSTICO ESTRATÉGICO")

# ----------------------------------------------------------------------
# MÓDULO 3: MOTOR ALGORÍTMICO Y CUANTIFICACIÓN MODULAR
# ----------------------------------------------------------------------
if enviar:
    # Constantes matemáticas de la Economía del Orden
    SEMANAS_ANUALES = 52
    TASA_RIESGO_MENSUAL = 0.00416
    MESES_PROYECCION = 12

    # Ecuaciones financieras
    co = hp * SEMANAS_ANUALES
    id_anual = (co * vhe) + drenaje
    factor_compuesto = (((1 + TASA_RIESGO_MENSUAL) ** MESES_PROYECCION) - 1) / TASA_RIESGO_MENSUAL
    vf = id_anual * factor_compuesto
    score_pentagono = (pilar_a + pilar_b + pilar_c + pilar_d + pilar_e) / 5.0

    st.divider()
    st.header(f"📈 Dashboard de Resultados: {nombre_caso.upper()}")
    
    # Despliegue de métricas financieras de alto impacto
    col1, col2, col3 = st.columns(3)
    col1.metric("Caos Anual Destructivo", f"{co} hrs")
    col2.metric("Impuesto al Desorden (ID)", f"${id_anual:,.2f} MXN")
    col3.metric("Impacto al Patrimonio (CPE 12M)", f"${vf:,.2f} MXN")

    st.subheader(f"Score Estructural Promedio: {score_pentagono:.1f} / 10.0")
    st.divider()
    st.markdown("#### 🚨 Diagnóstico de Incidencia Estructural e Inmunidad")

    # CONDICIONAL 1: Semáforo Crítico de Colapso (Filtro por Promedio Estructural)
    if score_pentagono < 5.0:
        st.error("🚨 **SEMÁFORO ROJO: ZONA DE DESASTRE ESTRUCTURAL**\n\n*La viabilidad del negocio a mediano plazo está comprometida por debilidad sistémica. Queda suspendida la entrega de cualquier formato o acción aislada. Se requiere transicionar de inmediato a un Diagnóstico General Profundo corporativo para detener la erosión de valor.*")
    elif score_pentagono >= 5.0 and score_pentagono < 7.5:
        st.warning("⚠️ **SEMÁFORO AMARILLO: OPERACIÓN EN RIESGO DE FATIGA**\n\n*El negocio genera utilidades pero el chasis operativo presenta fricciones constantes. Existen vulnerabilidades que pueden activarse ante auditorías o imprevistos macroeconómicos.*")
    else:
        st.success("🟢 **SEMÁFORO VERDE: RUTA HACIA LA SOBERANÍA SISTÉMICA**\n\n*La estructura demuestra madurez institucional. El enfoque actual debe ser de optimización continua, blindaje avanzado e inversión estratégica.*")

    # CONDICIONAL 2: Fallo de Integridad y Resiliencia (Materialidad y Fiscalidad Art. 69-B CFF)
    if pilar_b <= 5 or pilar_d <= 5:
        st.warning("⚖️ **ALERTA DE SEGURIDAD LEGAL: AUSENCIA DE MATERIALIDAD Y RIESGO PATRIMONIAL**\n\n*Puntuación crítica en blindaje. Existe un riesgo severo ante presunciones de operaciones simuladas (Art. 69-B CFF) o contingencias laborales/civiles. Requerimiento: Instrumentar de forma prioritaria Contratos de Acero con Fecha Cierta (NOM-151), cláusulas rigurosas de entregables y bitácoras técnicas como Prueba de Vida del negocio.*")

    # CONDICIONAL 3: El Espejismo del Orden (Falso control)
    if pilar_a > 6 and pilar_b <= 5:
        st.info("🔮 **ALERTA DEFENSIVA: EL ESPEJISMO DEL ORDEN**\n\n*Sus procesos internos pueden percibirse ordenados en el día a día, pero carecen de una estructura jurídica que los respalde hacia el exterior. Fluye la operación pero no hay sustancia legal protectora: una sola demanda o multa agresiva podría romper el chasis operativo.*")

    # CONDICIONAL 4: Fuga de Caja o Descontrol Presupuestal
    if pilar_c <= 5:
        st.error("💸 **ALERTA FINANCIERA: FUGA PASIVA DE UTILIDADES**\n\n*La falta de rigor presupuestal y control contable está evaporando la rentabilidad operativa. El desorden en este pilar neutraliza los esfuerzos comerciales de la organización.*")

    # CONDICIONAL 5: Techo de Crecimiento y Legado
    if pilar_e <= 5 and score_pentagono > 6.0:
        st.info("🏛️ **ALERTA DE TRASCENDENCIA: EL SÍNDROME DEL AUTOEMPLEO AVANZADO**\n\n*A pesar de contar con un negocio estable y ordenado, la ausencia de un sistema de inversión automática y Gobierno Corporativo impide la consolidación de un legado real. Está atrapado en la gestión, no en la expansión.*")

    st.caption("🔒 *Análisis procesado bajo las reglas matrices del sistema de institucionalización de Sinergia 360.*")