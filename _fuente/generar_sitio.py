# Genera el sitio estático "Grafito & Plata" del Dr. Luis Alonso Salja
import os, sys, html

OUT = sys.argv[1]
LOGO = "https://drluisalonsosalja.com/wp-content/uploads/2026/07/Logo_blanco-removebg-preview.png"
WA_MAIN = "https://wa.link/kxknj8"
PHONE = "+57 302 284 1740"
PHONE_RAW = "+573022841740"
EMAIL = "cipreecol@gmail.com"
ADDRESS = "Calle 85 #50-159, Edificio Quantum Tower, Consultorio 403"
FB = "https://www.facebook.com/profile.php?id=61586667602110"
IG = "https://www.instagram.com/drluisalonsosalja/"
TT = "https://vm.tiktok.com/ZS9FEAf14N6Ye-n8pZ0/"

# ---------- Iconos ----------
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
CAM = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="14" rx="2"/><circle cx="12" cy="13" r="3.5"/><path d="M8 6l1.5-2h5L16 6"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'
I_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8.5V6.8c0-.8.2-1.3 1.4-1.3H17V2.6c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.4-4 4.1v1.9H8v3.2h2.6V22H14V11.7h2.6l.4-3.2H14z"/></svg>'
I_IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM21.9 7.8a6.9 6.9 0 0 0-1.9-4.9A6.9 6.9 0 0 0 15.1 1C13.2.9 10.8.9 8.9 1A6.9 6.9 0 0 0 4 2.9 6.9 6.9 0 0 0 2.1 7.8c-.1 1.9-.1 6.5 0 8.4A6.9 6.9 0 0 0 4 21.1 6.9 6.9 0 0 0 8.9 23c1.9.1 4.3.1 6.2 0a6.9 6.9 0 0 0 4.9-1.9 6.9 6.9 0 0 0 1.9-4.9c.1-1.9.1-6.5 0-8.4zM19.6 18a3.2 3.2 0 0 1-1.8 1.8c-1.3.5-4.3.4-5.8.4s-4.5.1-5.8-.4A3.2 3.2 0 0 1 4.4 18c-.5-1.3-.4-4.3-.4-5.8s-.1-4.5.4-5.8A3.2 3.2 0 0 1 6.2 4.6c1.3-.5 4.3-.4 5.8-.4s4.5-.1 5.8.4a3.2 3.2 0 0 1 1.8 1.8c.5 1.3.4 4.3.4 5.8s.1 4.5-.4 5.8z"/></svg>'
I_TT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19.6 6.7a4.8 4.8 0 0 1-3.8-4.2V2h-3.4v13.6a2.9 2.9 0 1 1-2-2.7V9.4a6.3 6.3 0 1 0 5.4 6.2V8.7a8.2 8.2 0 0 0 3.8 1.2V6.7z"/></svg>'
I_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
I_MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
I_PLANE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>'
I_HAND = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V12M11 11.5v-2a1.5 1.5 0 0 1 3 0V12M14 10.5a1.5 1.5 0 0 1 3 0V12M17 11.5a1.5 1.5 0 0 1 3 0V16a6 6 0 0 1-6 6h-2a6 6 0 0 1-5-2.7L4.3 15a1.5 1.5 0 0 1 2.4-1.8L8 15"/></svg>'

SCRIBBLE = '<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 14 C 60 4, 120 6, 170 10 S 260 16, 297 6"/></svg>'

def esc(s): return html.escape(s, quote=True)

def ph(label, cls=""):
    return f'<div class="ph {cls}"><span>{CAM}{esc(label)}</span></div>'

# ---------- Procedimientos (texto original del sitio) ----------
PROCS = [
 dict(slug="mamoplastia-de-aumento", cat="mamaria", name="Mamoplastia de aumento", wa="https://wa.link/vzzi6x",
  short="Aumenta el volumen y mejora la forma de los senos con resultados naturales, armónicos y adaptados a tu anatomía.",
  card="La mamoplastia de aumento permite aumentar el volumen de los senos y mejorar su forma mediante implantes de última generación, proporcionando resultados naturales, equilibrados y acordes con la anatomía de cada paciente.",
  intro=["La mamoplastia de aumento es un procedimiento diseñado para mejorar el volumen, la forma y la proyección de las mamas, logrando una silueta más armónica y proporcionada.",
         "Cada cirugía se planifica de forma personalizada, seleccionando el implante y la técnica más adecuados según la anatomía, las expectativas y el estilo de vida de cada paciente. Nuestro objetivo es obtener resultados naturales que respeten tu esencia, priorizando siempre la seguridad y el equilibrio estético."],
  faq=[("¿Quién es candidata para una mamoplastia de aumento?","Es un procedimiento indicado para mujeres que desean aumentar el volumen de sus mamas, corregir asimetrías o recuperar la pérdida de volumen ocasionada por el embarazo, la lactancia o cambios importantes de peso. La valoración médica permitirá determinar el plan quirúrgico ideal para cada caso."),
       ("¿Cómo se elige el tamaño del implante?","La elección del implante se realiza de manera personalizada, considerando tus proporciones corporales, la calidad de los tejidos y el resultado que deseas alcanzar. Nuestro objetivo es lograr un resultado armónico, natural y acorde con tu anatomía."),
       ("¿Dónde se colocan los implantes?","Dependiendo de las características de cada paciente, los implantes pueden colocarse por encima o por debajo del músculo pectoral. Durante la consulta se determinará cuál es la técnica más adecuada para ofrecer el mejor resultado."),
       ("¿Cómo es la recuperación?","La recuperación suele ser progresiva. Durante los primeros días pueden presentarse inflamación y molestias leves que mejoran gradualmente. El seguimiento médico y el cumplimiento de las recomendaciones postoperatorias son fundamentales para una recuperación segura."),
       ("¿Cuándo podré ver el resultado final?","Aunque el cambio es visible desde el inicio, el resultado definitivo se aprecia de forma gradual a medida que disminuye la inflamación y los tejidos se adaptan al implante, generalmente durante los siguientes meses."),
       ("¿Los implantes duran toda la vida?","Los implantes mamarios son dispositivos de larga duración, pero no tienen una fecha exacta de reemplazo. Se recomienda realizar controles periódicos y consultar con el cirujano ante cualquier cambio o molestia.")],
  approach_title="Resultados que priorizan tu <em>bienestar</em>",
  approach=[("Implante personalizado","Selección del tamaño, perfil y técnica de colocación según tu anatomía y objetivos estéticos."),
            ("Técnica quirúrgica precisa","Planificación detallada para lograr proyección y armonía respetando tus tejidos."),
            ("Resultados duraderos","Técnicas que aseguran una evolución estética estable y un impacto positivo en tu confianza a largo plazo.")]),
 dict(slug="transferencia-de-grasa-a-senos", cat="mamaria", name="Transferencia de grasa a senos", wa="https://wa.link/74zr82",
  short="Tejido de la propia paciente para aumentar el volumen y mejorar el contorno de forma natural.",
  card="La transferencia de grasa a senos utiliza tejido de la propia paciente para aumentar el volumen y mejorar el contorno de forma natural, proporcionando resultados armónicos, equilibrados y acordes con la anatomía de cada paciente.",
  intro=["La reconstrucción mamaria con transferencia de grasa utiliza tejido del propio paciente para restaurar el volumen y la forma del seno de manera natural. La grasa se obtiene mediante una liposucción cuidadosamente planificada, se procesa y posteriormente se injerta en la mama para mejorar su contorno y calidad de los tejidos.",
         "Al emplear tejido autólogo, se consigue un resultado de apariencia y tacto más naturales, evitando el uso de materiales sintéticos cuando está indicado."],
  faq=[("¿Cómo se realiza el procedimiento?","El procedimiento inicia con una liposucción de áreas previamente seleccionadas para obtener grasa de alta calidad. Posteriormente, esta se procesa cuidadosamente y se injerta en la mama de forma estratégica, buscando restaurar el volumen y mejorar el contorno con resultados armónicos y naturales."),
       ("¿Existen riesgos?","Como cualquier procedimiento quirúrgico, existen riesgos que serán explicados durante la consulta. Una adecuada selección del paciente, una técnica precisa y un seguimiento postoperatorio cercano son fundamentales para obtener una evolución segura y resultados satisfactorios."),
       ("¿Cómo es la recuperación?","La recuperación suele ser progresiva. Durante las primeras semanas es normal presentar inflamación tanto en la zona donante como en la zona tratada. El cumplimiento de las recomendaciones médicas y los controles postoperatorios favorecen una adecuada integración del injerto y una recuperación segura."),
       ("¿Cuándo se ven los resultados?","Los resultados evolucionan de forma gradual a medida que disminuye la inflamación y el injerto se estabiliza. El objetivo es ofrecer una reconstrucción que restablezca la armonía del seno, respetando la anatomía y proporcionando una apariencia natural.")],
  approach_title="Restaurar con tu propia <em>esencia</em>",
  approach=[("Tejido autólogo","Utiliza tu propia grasa para restaurar volumen y forma de manera natural."),
            ("Técnica precisa","Liposucción e injerto estratégico para un contorno armónico."),
            ("Resultado natural","Apariencia y tacto naturales sin materiales sintéticos.")]),
 dict(slug="reduccion-mamaria", cat="mamaria", name="Reducción mamaria", wa="https://wa.link/w4n8bk",
  short="Reduce el tamaño de los senos para aliviar molestias y lograr una figura más cómoda, equilibrada y natural.",
  card="La reducción mamaria permite disminuir el exceso de tejido mamario y remodelar los senos para conseguir una silueta más cómoda, aliviar las molestias ocasionadas por su exceso de volumen y mejorar la armonía corporal.",
  intro=["La mamoplastia de reducción es un procedimiento diseñado para disminuir el tamaño y el peso de las mamas, restaurando una proporción más armónica con el cuerpo. Además de mejorar el contorno, ayuda a aliviar las molestias físicas ocasionadas por un exceso de volumen mamario, favoreciendo una mejor calidad de vida.",
         "Cada cirugía se planifica de forma personalizada, respetando la anatomía, las necesidades funcionales y los objetivos estéticos de cada paciente."],
  faq=[("¿Por qué considerar una mamoplastia de reducción?","La reducción mamaria no solo transforma la apariencia del busto, sino que también puede mejorar significativamente el bienestar físico y emocional, aliviando molestias y mejorando la calidad de vida."),
       ("¿Quién es candidata para una mamoplastia de reducción?","Está indicada para mujeres con senos de gran tamaño que presentan molestias físicas, limitaciones en sus actividades diarias o desean una apariencia más proporcionada."),
       ("¿Cómo es la recuperación después de la cirugía?","La recuperación suele ser progresiva. La mayoría de las pacientes retoman actividades ligeras en pocos días y pueden reincorporarse a su rutina habitual siguiendo las indicaciones del cirujano."),
       ("¿Cuándo podré ver el resultado definitivo?","Los cambios son visibles desde el inicio, pero el resultado final se aprecia una vez disminuye la inflamación y los tejidos cicatrizan, generalmente entre tres y seis meses después de la cirugía.")],
  approach_title="Recuperar comodidad y <em>confianza</em>",
  approach=[("Alivio funcional","Reduce el dolor en cuello, espalda y hombros derivado del exceso de volumen mamario."),
            ("Proporción corporal","Restaura una silueta más equilibrada y armónica con tu cuerpo."),
            ("Seguridad quirúrgica","Planificación personalizada priorizando tu bienestar y tus objetivos.")]),
 dict(slug="explantacion-mamaria", cat="mamaria", name="Explantación mamaria", wa="https://wa.link/pa9s4s",
  short="Retira los implantes de forma segura y restaura una apariencia más natural.",
  card="La explantación mamaria permite retirar los implantes de forma segura y restaurar una apariencia más natural, respetando la anatomía de cada paciente y priorizando siempre su bienestar, comodidad y equilibrio estético.",
  intro=["La explantación mamaria es un procedimiento quirúrgico que consiste en retirar los implantes mamarios y, cuando está indicado, la cápsula que los rodea. Más que remover un implante, el objetivo es restaurar la anatomía de forma segura, respetando la naturalidad y el equilibrio estético de cada paciente.",
         "Cada cirugía se planifica de manera personalizada, buscando no solo un resultado armónico, sino también brindar tranquilidad y bienestar durante todo el proceso."],
  faq=[("¿Quién es candidata para una explantación mamaria?","La explantación está indicada para pacientes que desean retirar sus implantes por motivos médicos, estéticos o personales, buscando una solución adaptada a sus necesidades."),
       ("¿Cómo es la recuperación después de la explantación?","La recuperación varía según cada paciente y el procedimiento realizado. Siguiendo las indicaciones del cirujano, la mayoría puede retomar sus actividades de forma progresiva."),
       ("¿Será necesario realizar un procedimiento adicional?","En algunos casos, puede recomendarse una mastopexia o remodelación mamaria para mejorar la forma y el contorno del busto después del retiro de los implantes, dependiendo de las características de cada paciente.")],
  approach_title="Una nueva etapa con <em>seguridad</em>",
  approach=[("Retiro seguro del implante","Extracción cuidadosa del implante y, cuando corresponde, de la cápsula."),
            ("Respeto por tu anatomía","Restaura la naturalidad y el equilibrio estético de la mama."),
            ("Tranquilidad y bienestar","Un proceso transparente y acompañado para tu nueva etapa.")]),
 dict(slug="mastopexia-levantamiento-de-senos", cat="mamaria", name="Levantamiento de senos", wa="https://wa.link/782w52",
  short="Eleva y remodela los senos para recuperar su firmeza y posición.",
  card="La mastopexia permite elevar y remodelar los senos para recuperar su firmeza y posición, logrando una apariencia más armónica, juvenil y natural, respetando las proporciones de cada paciente.",
  intro=["La mastopexia, o levantamiento de senos, es un procedimiento quirúrgico diseñado para restaurar la posición, la firmeza y la forma de las mamas. Además de elevar el tejido mamario, permite reposicionar la areola y el pezón para lograr una apariencia más armónica y juvenil.",
         "Los cambios asociados al embarazo, la lactancia, las variaciones de peso y el paso del tiempo pueden modificar la forma del seno. La mastopexia busca devolver el equilibrio y la proporción, respetando la anatomía de cada paciente. Cuando es necesario, puede combinarse con implantes mamarios o una reducción mamaria para obtener el resultado deseado."],
  faq=[("¿Qué resultados puedo esperar?","La mastopexia ofrece una mama más firme, elevada y proporcionada, mejorando el contorno y la armonía corporal sin perder la naturalidad."),
       ("¿Es más que un cambio estético?","Además de mejorar la apariencia, la mastopexia puede aumentar la comodidad física al disminuir la flacidez y mejorar el soporte del tejido mamario. Muchas pacientes experimentan una mayor confianza, bienestar y satisfacción con su imagen corporal."),
       ("¿Cómo es la recuperación después de una mastopexia?","La recuperación es progresiva y varía en cada paciente. Siguiendo las recomendaciones del cirujano, la mayoría puede retomar sus actividades cotidianas de forma gradual, mientras el resultado continúa evolucionando durante los meses posteriores.")],
  approach_title="Devolver el equilibrio sin perder tu <em>esencia</em>",
  approach=[("Restauración de la firmeza","Reposiciona el tejido mamario para recuperar una apariencia juvenil y erguida."),
            ("Reposición armónica","Ubica la areola y el pezón en una posición natural y equilibrada."),
            ("Resultado natural y juvenil","Devuelve el equilibrio y la proporción respetando tu anatomía.")]),
 dict(slug="abdominoplastia", cat="corporal", name="Abdominoplastia", wa="https://wa.link/ark3ba",
  short="Elimina el exceso de piel y fortalece el abdomen para conseguir un contorno más firme, plano y definido.",
  card="La abdominoplastia es un procedimiento que elimina el exceso de piel y grasa del abdomen, fortalece la pared abdominal y redefine el contorno corporal para lograr una silueta más firme, armónica y natural.",
  intro=["La abdominoplastia es un procedimiento quirúrgico que elimina el exceso de piel y grasa del abdomen, al tiempo que fortalece la pared abdominal para conseguir un abdomen más firme, plano y una silueta mejor definida. La cirugía se realiza mediante una incisión ubicada por encima del vello púbico, cuya longitud dependerá de la cantidad de piel y tejido que sea necesario retirar.",
         "Durante el procedimiento, el ombligo se reubica para conservar una apariencia natural y los músculos abdominales pueden repararse cuando existe separación o debilidad, lo que contribuye a mejorar el contorno de la cintura. La cicatriz queda estratégicamente ubicada para que pueda ocultarse con la ropa interior o el traje de baño y, con el paso del tiempo, suele volverse menos visible como parte del proceso normal de cicatrización."],
  faq=[("¿Quién es candidato para una abdominoplastia?","Está indicada para pacientes con exceso de piel, flacidez abdominal o separación de los músculos (diástasis), generalmente después del embarazo o de una pérdida importante de peso. La valoración médica permitirá determinar si este procedimiento es el más adecuado para ti."),
       ("¿Cuáles son los riesgos del procedimiento?","Como toda cirugía, la abdominoplastia implica riesgos que son explicados detalladamente durante la consulta. Una adecuada selección del paciente, una técnica quirúrgica precisa y el cumplimiento de las recomendaciones postoperatorias contribuyen a minimizar estas complicaciones."),
       ("¿Cómo se realiza la cirugía?","La intervención se realiza bajo anestesia general y se adapta a las necesidades de cada paciente. Dependiendo del caso, puede incluir la reparación de la pared abdominal, la eliminación del exceso de piel y grasa, y el reposicionamiento del ombligo para conseguir un resultado armónico y natural."),
       ("¿Cómo es la recuperación?","La recuperación es progresiva y personalizada. Durante las primeras semanas se recomienda limitar los esfuerzos físicos y utilizar la faja postoperatoria según las indicaciones médicas. Nuestro equipo realizará un seguimiento cercano para acompañarte durante todo el proceso y favorecer una recuperación segura.")],
  approach_title="Un abdomen firme y <em>definido</em>",
  approach=[("Reparación muscular","Corrige la diástasis y restaura la firmeza de la pared abdominal."),
            ("Eliminación del exceso","Retira piel y grasa sobrante para un contorno más definido."),
            ("Contorno natural","Logra un abdomen más plano, natural y proporcionado a tu cuerpo.")]),
 dict(slug="liposuccion", cat="corporal", name="Liposucción", wa="https://wa.link/8g9kp1",
  short="Elimina depósitos de grasa localizada para remodelar el contorno y definir la silueta.",
  card="La liposucción elimina depósitos de grasa localizada para remodelar el contorno corporal y definir la silueta, logrando resultados naturales, equilibrados y acordes con la anatomía de cada paciente.",
  intro=["La liposucción es un procedimiento diseñado para eliminar depósitos de grasa localizada y mejorar el contorno corporal de forma armónica. No está orientada a la pérdida de peso, sino a redefinir la silueta en pacientes que mantienen un estilo de vida saludable y presentan zonas resistentes al ejercicio y la alimentación.",
         "Cada procedimiento se planifica de manera personalizada, respetando la anatomía de cada paciente y buscando resultados naturales, proporcionales y duraderos."],
  faq=[("¿En qué consiste la liposucción?","La liposucción utiliza cánulas especializadas para remover grasa localizada a través de pequeñas incisiones. Dependiendo de tus objetivos, puede realizarse como procedimiento único o combinarse con otras cirugías para optimizar el contorno corporal."),
       ("¿Quién es candidato para una liposucción?","Es ideal para pacientes con un peso estable, buen estado de salud y acumulaciones de grasa que no responden al ejercicio o la dieta. Durante la valoración médica determinamos si este procedimiento es el indicado para ti."),
       ("¿Cómo es la recuperación?","La recuperación es progresiva y personalizada. Es normal presentar inflamación y molestias leves durante los primeros días. El uso de prendas de compresión y el seguimiento médico favorecen una adecuada cicatrización y una recuperación segura."),
       ("¿Cuándo se observan los resultados?","Los cambios iniciales comienzan a apreciarse cuando disminuye la inflamación. El resultado continúa definiéndose de forma progresiva durante los siguientes meses, alcanzando un contorno corporal más armónico y natural.")],
  approach_title="Redefinir tu silueta con <em>precisión</em>",
  approach=[("Redefinición de la silueta","Elimina grasa localizada resistente al ejercicio y la dieta."),
            ("Respeto por la anatomía","Resultados proporcionales y naturales según tu cuerpo."),
            ("Resultados duraderos","Contorno estable manteniendo hábitos de vida saludables.")]),
 dict(slug="transferencia-de-grasa-a-gluteos", cat="corporal", name="Transferencia de grasa a glúteos", wa="https://wa.link/gmku1p",
  short="Aumenta el volumen y mejora la forma de los glúteos con tu propia grasa.",
  card="La transferencia de grasa a glúteos combina liposucción y remodelación corporal para aumentar el volumen y mejorar la forma de los glúteos utilizando la propia grasa del paciente.",
  intro=["La transferencia de grasa a glúteos, también conocida como lipotransferencia glútea, es un procedimiento que combina liposucción y remodelación corporal para aumentar el volumen y mejorar la forma de los glúteos utilizando la propia grasa del paciente.",
         "La grasa se obtiene de zonas con exceso de tejido adiposo, se procesa cuidadosamente y se injerta de manera estratégica para conseguir un resultado armónico, natural y proporcional. Nuestro objetivo es realzar el contorno corporal respetando la anatomía y priorizando siempre la seguridad del paciente."],
  faq=[("¿Quién es candidato para una transferencia de grasa a glúteos?","Este procedimiento está indicado para pacientes con depósitos de grasa suficientes para realizar la transferencia y que deseen mejorar el volumen, la proyección o la forma de los glúteos de manera natural. La valoración médica determinará si eres un candidato adecuado."),
       ("¿Qué ventajas tiene frente a los implantes glúteos?","Al utilizar la grasa del propio paciente, se obtiene un resultado de apariencia y tacto más natural, sin necesidad de implantes. Además, la liposucción permite definir otras áreas del cuerpo, mejorando el contorno corporal de forma integral."),
       ("¿Qué sucede con la grasa transferida?","Una parte de la grasa injertada se integra de manera permanente al tejido, mientras que otra puede reabsorberse durante los primeros meses. La técnica quirúrgica y el cumplimiento de las recomendaciones postoperatorias son fundamentales para optimizar la supervivencia del injerto."),
       ("¿Cómo es la recuperación?","Durante las primeras semanas se recomienda evitar la presión directa sobre los glúteos y seguir estrictamente las indicaciones médicas. El uso de prendas de compresión y los controles postoperatorios favorecen una recuperación adecuada y resultados óptimos."),
       ("¿Cuándo se observan los resultados?","El cambio es visible desde el postoperatorio inmediato; sin embargo, el resultado definitivo se aprecia progresivamente a medida que disminuye la inflamación y la grasa injertada se estabiliza, generalmente entre los 3 y 6 meses.")],
  approach_title="Esculpir tu cuerpo de forma <em>integral</em>",
  approach=[("Esculpido integral","Combina liposucción e injerto para realzar el contorno de forma armónica."),
            ("Proporciones armónicas","Resultados naturales que respetan tu anatomía y tus objetivos."),
            ("Seguridad quirúrgica","Planificación personalizada priorizando siempre tu bienestar.")]),
 dict(slug="retraccion-de-piel-y-contorno-corporal", cat="corporal", name="Retracción de piel y contorno corporal", wa="https://wa.link/j1d42x",
  short="Mejora la firmeza y definición del contorno corporal con tecnologías avanzadas.",
  card="La retracción de piel mejora la firmeza y definición del contorno corporal mediante tecnologías avanzadas, favoreciendo una piel más firme y resultados naturales, armónicos y duraderos.",
  intro=["La retracción de piel es un complemento de la liposucción que busca mejorar la firmeza y definición del contorno corporal. Mediante tecnologías de última generación, es posible estimular la contracción de los tejidos y favorecer la producción de colágeno, logrando una piel más firme y un resultado más armónico.",
         "Seleccionamos la tecnología más adecuada según la calidad de la piel, la anatomía y los objetivos de cada paciente, con un enfoque personalizado y orientado a resultados naturales."],
  faq=[("¿Quién es candidato para estas tecnologías?","Son ideales para pacientes que presentan grasa localizada y desean mejorar la firmeza de la piel o prevenir la flacidez después de una liposucción. La indicación dependerá de la calidad de la piel y de la evaluación médica."),
       ("¿Estas tecnologías reemplazan una cirugía para retirar piel?","No. Cuando existe un exceso importante de piel, procedimientos como la abdominoplastia o el lifting corporal siguen siendo la mejor alternativa. Estas tecnologías ofrecen excelentes resultados en casos de flacidez leve o moderada."),
       ("¿Se pueden combinar con una liposucción?","Sí. Con frecuencia se utilizan como complemento de la liposucción para mejorar la definición corporal y favorecer una mayor retracción de la piel."),
       ("¿Los resultados son inmediatos?","Algunos cambios pueden apreciarse desde las primeras semanas; sin embargo, la producción de colágeno continúa durante los siguientes meses, por lo que el resultado mejora de forma progresiva."),
       ("¿Cómo es la recuperación?","La recuperación dependerá del procedimiento realizado. En la mayoría de los casos, es similar a la de una liposucción convencional, siguiendo las indicaciones médicas, el uso de prendas de compresión y los controles postoperatorios.")],
  approach_title="Tecnología que reafirma tu <em>piel</em>",
  approach=[("Tecnología de vanguardia","Retraction®, VASER® y J-Plasma® seleccionadas según tu caso."),
            ("Retracción cutánea","Estimula la contracción de los tejidos y la producción de colágeno."),
            ("Resultados progresivos","Una piel más firme que mejora de forma gradual en los siguientes meses.")]),
]
CATS = {"mamaria": "Estética mamaria", "corporal": "Contorno corporal"}


# ---------- Resultados reales (fotos de la carpeta "img dr luis alonso/Procedimientos") ----------
RESULTS = {
 "abdominoplastia": [("corporal", 0), ("corporal", 4), ("corporal", 12), ("corporal", 19), ("corporal", 43), ("corporal", 45)],
 "liposuccion": [("corporal", 5), ("corporal", 10), ("corporal", 25), ("corporal", 35), ("corporal", 33), ("corporal", 38)],
 "retraccion-de-piel-y-contorno-corporal": [("corporal", 20), ("corporal", 27), ("corporal", 33), ("corporal", 38)],
 "transferencia-de-grasa-a-gluteos": [("gluteos", 0), ("gluteos", 2), ("gluteos", 3), ("gluteos", 4), ("gluteos", 8), ("corporal", 32), ("corporal", 34), ("corporal", 36)],
 "mamoplastia-de-aumento": [("mamaria", 3), ("mamaria", 4), ("mamaria", 5), ("mamaria", 6), ("mamaria", 11)],
 "reduccion-mamaria": [("mamaria", 2), ("mamaria", 14), ("mamaria", 16)],
 "mastopexia-levantamiento-de-senos": [("mamaria", 1), ("mamaria", 16), ("mamaria", 2)],
 "explantacion-mamaria": [("mamaria", 1), ("mamaria", 6)],
 "transferencia-de-grasa-a-senos": [("mamaria", 3), ("mamaria", 11)],
}
GROUP_LABEL = {"corporal": "Contorno corporal", "gluteos": "Glúteos", "mamaria": "Estética mamaria"}
CARD_IMG = {
 "abdominoplastia": "resultados/corporal-12-d.jpg", "liposuccion": "resultados/corporal-35-d.jpg",
 "transferencia-de-grasa-a-gluteos": "resultados/gluteos-2-d.jpg", "retraccion-de-piel-y-contorno-corporal": "resultados/corporal-27-d.jpg",
 "mamoplastia-de-aumento": "quirofano/q7.jpg", "reduccion-mamaria": "quirofano/q8.jpg",
 "explantacion-mamaria": "quirofano/q11.jpg", "mastopexia-levantamiento-de-senos": "quirofano/q6.jpg",
 "transferencia-de-grasa-a-senos": "quirofano/q-luz.jpg",
}
EYE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>'

def ba_real(group, idx, label, cat=None):
    sens = group == "mamaria"
    base = f"assets/img/resultados/{group}-{idx}"
    veil = f'<button class="veil" type="button">{EYE}<b>Contenido médico</b><small>Toca para ver el resultado</small></button>' if sens else ""
    return f"""<div class="ba-item rv" data-cat="{cat or group}">
  <div class="ba{' ba--sens' if sens else ''}">
    <img src="{base}-a.jpg" alt="Antes: {esc(label)}" loading="lazy" width="436" height="600">
    <img class="ba__after" src="{base}-d.jpg" alt="Después: {esc(label)}" loading="lazy" width="436" height="600">
    <span class="ba__tag ba__tag--l">Antes</span><span class="ba__tag ba__tag--r">Después</span>
    <span class="ba__bar" aria-hidden="true"></span>
    <input type="range" min="0" max="100" value="50" aria-label="Comparar antes y después: {esc(label)}">
    {veil}
  </div>
  <div class="ba-cap"><b>{esc(label)}</b><span class="muted">Desliza ↔</span></div>
</div>"""

def results_for(slug):
    items = RESULTS.get(slug, [])
    return "".join(ba_real(g, i, f"Caso real {n+1} · {GROUP_LABEL[g]}") for n, (g, i) in enumerate(items))

REELS = [("Mi verdadero trabajo empieza aquí", "Técnica, profesionalismo y resultados"), ("En quirófano", "Así cuidamos cada detalle"),
         ("¿Fibrosis?", "Qué es y cómo prevenirla"), ("Explantación mamaria", "Lo que debes saber"),
         ("Agenda tu valoración", "Así empieza tu proceso"), ("La Cherchita", "El lado más humano del doctor"),
         ("Fibrosis, en podcast", "Respuestas claras"), ("¿Por qué Colombia?", "Turismo médico seguro")]

def reels_block():
    cards = ""
    for i, (t, sub) in enumerate(REELS, 1):
        cards += f"""<a class="reel" href="{IG}" target="_blank" rel="noopener" aria-label="Ver video: {esc(t)}">
  <video muted loop playsinline preload="none" poster="assets/video/posters/reel-{i}.jpg" data-src="assets/video/reel-{i}.mp4"></video>
  <img class="reel__poster" src="assets/video/posters/reel-{i}.jpg" alt="" loading="lazy">
  <span class="reel__sound" aria-hidden="true">Toca para activar el sonido</span>
  <span class="reel__play">{PLAY}</span>
  <span class="reel__cap"><b>{esc(t)}</b>{esc(sub)}</span>
</a>"""
    return cards

def proc_scroller():
    cards = ""
    for p in sorted(PROCS, key=lambda x: x["slug"] not in CARD_IMG):
        img = CARD_IMG.get(p["slug"])
        media = f'<img src="assets/img/{img}" alt="Resultado de {esc(p["name"].lower())}" loading="lazy">' if img else ph("Foto: " + p["name"])
        cards += f"""<a class="pslide" href="{p["slug"]}.html">
  <div class="pslide__img">{media}<span class="pcard__tag">{CATS[p["cat"]]}</span></div>
  <div class="pslide__txt"><h3>{esc(p["name"])}</h3><span class="go">{ARROW}</span></div>
</a>"""
    return cards

# ---------- Equipo (nombres y cargos por confirmar con el cliente) ----------
TEAM = [
 ("../doctor/retrato-sonrisa.jpg", "Dr. Luis Alonso", "Cirujano plástico", "Cirujano plástico, estético y reconstructivo",
  "Especialista de la Universidad Nacional de Colombia, docente de posgrado en la Universidad Simón Bolívar y miembro de la SCCP y la FILACP."),
 ("integrante-1.jpg", "Nombre", "Jefe de enfermería", "Jefe de enfermería",
  "Coordina el cuidado de cada paciente antes, durante y después de la cirugía, con protocolos hospitalarios rigurosos y trazabilidad completa."),
 ("integrante-2.jpg", "Nombre", "Anestesiología", "Médico anestesiólogo",
  "Parte del equipo de anestesia certificado que vela por tu seguridad durante todo el procedimiento quirúrgico."),
 ("integrante-3.jpg", "Nombre", "Médica asistente", "Médica asistente",
  "Acompaña la valoración, el plan quirúrgico y los controles postoperatorios, resolviendo tus dudas en cada paso."),
 ("integrante-4.jpg", "Nombre", "Instrumentación", "Instrumentadora quirúrgica",
  "Prepara el quirófano y el instrumental para que cada cirugía se realice con precisión y bajo los más altos estándares."),
 ("integrante-5.jpg", "Nombre", "Atención al paciente", "Coordinadora de pacientes y turismo médico",
  "Tu primer contacto: agenda tu valoración y coordina vuelos, hospedaje y traslados si vienes de otra ciudad o país."),
 ("integrante-6.jpg", "Nombre", "Cosmetología", "Cosmetóloga · post operatorio",
  "Acompaña tu recuperación con tratamientos post operatorios y aparatología para favorecer resultados óptimos."),
]

NAV = [("index.html", "Inicio"), ("sobre-mi.html", "Sobre mí"), ("procedimientos.html", "Procedimientos"),
       ("turismo-medico.html", "Turismo médico"), ("contacto.html", "Contacto")]

def header(active):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ''
        if href == "procedimientos.html":
            cols = ""
            for c, cl in CATS.items():
                items = "".join(f'<a href="{p["slug"]}.html">{esc(p["name"])}</a>' for p in PROCS if p["cat"] == c)
                cols += f'<div><h4>{cl}</h4>{items}</div>'
            links.append(f'<div class="nav__drop"><button type="button" aria-haspopup="true"{cur} onclick="location.href=\'procedimientos.html\'">Procedimientos {CHEV}</button><div class="mega">{cols}</div></div>')
        else:
            links.append(f'<a href="{href}"{cur}>{label}</a>')
    drawer_procs = "".join(f'<a href="{p["slug"]}.html">{esc(p["name"])}</a>' for p in PROCS)
    return f'''<a class="skip" href="#main">Saltar al contenido</a>
<header class="header">
  <div class="wrap header__in">
    <a class="brand" href="index.html" aria-label="Dr. Luis Alonso Salja — Inicio">
      <img src="{LOGO}" alt="Luis Alonso Salja — Cirugía plástica" width="200" height="60">
    </a>
    <nav class="nav" aria-label="Principal">{''.join(links)}</nav>
    <a class="btn btn--bronze header__cta" href="{WA_MAIN}" target="_blank" rel="noopener">Agendar mi cita</a>
    <button class="burger" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="drawer"><span></span></button>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <button class="drawer__close" type="button" aria-label="Cerrar menú">×</button>
  <nav aria-label="Menú móvil">
    <a href="index.html">Inicio</a>
    <a href="sobre-mi.html">Sobre <em>mí</em></a>
    <details><summary>Procedimientos</summary><a href="procedimientos.html">Ver todos</a>{drawer_procs}</details>
    <a href="turismo-medico.html">Turismo <em>médico</em></a>
    <a href="contacto.html">Contacto</a>
  </nav>
  <a class="btn btn--bronze" href="{WA_MAIN}" target="_blank" rel="noopener">Agendar mi cita {ARROW}</a>
  <div class="drawer__foot">{PHONE}<br>{ADDRESS}, Barranquilla</div>
</div>
'''

def footer():
    procs = "".join(f'<li><a href="{p["slug"]}.html">{esc(p["name"])}</a></li>' for p in PROCS[:6])
    return f'''<footer class="footer">
  <div class="wrap">
    <p class="footer__big">Comience su transformación con <em>confianza.</em></p>
    <div class="footer__grid">
      <div>
        <div class="footer__logo"><img src="{LOGO}" alt="Luis Alonso Salja — Cirugía plástica" width="84" height="64"></div>
        <p>Cada procedimiento es una oportunidad para resaltar tu belleza de forma natural, con seguridad, experiencia y un acompañamiento cercano.</p>
        <div class="social">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>
          <a href="{TT}" target="_blank" rel="noopener" aria-label="TikTok">{I_TT}</a>
        </div>
      </div>
      <div><h4>Navegación</h4><ul>{''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)}</ul></div>
      <div><h4>Procedimientos</h4><ul>{procs}<li><a href="procedimientos.html">Ver todos →</a></li></ul></div>
      <div><h4>Contacto</h4><ul>
        <li><a href="tel:{PHONE_RAW}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ADDRESS}<br>Barranquilla, Colombia</li>
      </ul></div>
    </div>
    <div class="footer__bottom"><span>© <span data-year>2026</span> drluisalonsosalja.com</span><a href="guia-de-marca.html">Guía de marca · propuesta</a></div>
  </div>
  <div class="footer__mark" aria-hidden="true">Luis Alonso</div>
</footer>
<a class="wa-float" href="{WA_MAIN}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><span>¿Hablamos?</span><i>{WA_ICON}</i></a>
<div class="cursor-preview" aria-hidden="true"><div></div></div>
<script src="js/main.js" defer></script>
'''

def page(fname, title, desc, body, active=None, body_class=""):
    doc = f'''<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#1B2026">
<link rel="icon" href="https://drluisalonsosalja.com/wp-content/uploads/2026/07/cropped-IMG_6256-32x32.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Instrument+Sans:wght@400;500;600&family=Mrs+Saint+Delafield&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body class="{body_class}">
{header(active)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(doc)
    print("ok", fname)

# ---------- Bloques reutilizables ----------
def team_block(dark=False, heading=True):
    cards = ""
    for i, (img, name, cap, role, bio) in enumerate(TEAM):
        is_dr = i == 0
        shown = name if is_dr else "Nombre"
        alt = f"{name} — {role}" if is_dr else f"{role} del equipo del Dr. Luis Alonso Salja"
        cards += f'''<article class="pola" tabindex="0" role="button" aria-expanded="false" aria-label="{esc(role)}: ver quién es" style="--d:-{i*0.9:.1f}s">
  <span class="pola__clip" aria-hidden="true"></span>
  <div class="pola__card">
    <div class="pola__photo"><img src="assets/img/equipo/{img}" alt="{esc(alt)}" loading="lazy" width="480" height="640">
      <div class="pola__bio"><b>{esc(role)}</b><p>{esc(bio)}</p></div>
    </div>
    <div class="pola__name">{esc(shown)}</div>
    <div class="pola__role">{esc(cap)}</div>
  </div>
</article>'''
    head = f'''<div class="team__head">
      <div>
        <span class="eyebrow">Nuestro equipo</span>
        <h2 class="rv">Las manos que te <em>acompañan</em></h2>
        <p class="lead rv rv-d1" style="margin-top:18px">Cada procedimiento es el resultado de un trabajo coordinado entre especialistas comprometidos con tu seguridad, tu bienestar y resultados que trascienden.</p>
      </div>
      <div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div>
    </div>''' if heading else f'<div class="team__head"><span></span><div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div></div>'
    return f'''<section class="section team{' dark' if dark else ''}" id="equipo" aria-label="Equipo médico">
  <div class="wrap">
    {head}
    <div class="rope">
      <svg class="cord" viewBox="0 0 1200 60" preserveAspectRatio="none" aria-hidden="true"><path d="M-10 6 Q 300 46 600 18 T 1210 10"/></svg>
      <div class="team__track">{cards}</div>
    </div>
    <p class="pola__hint">{I_HAND} Pasa el mouse o toca cada foto para conocer a quien te acompaña</p>
  </div>
</section>'''

def ba_block(items, dark=False):
    out = ""
    for label in items:
        out += f'''<div>
  <div class="ba">
    {ph("Foto antes")}
    {ph("Foto después", "ba__after")}
    <span class="ba__tag ba__tag--l">Antes</span><span class="ba__tag ba__tag--r">Después</span>
    <span class="ba__bar" aria-hidden="true"></span>
    <input type="range" min="0" max="100" value="50" aria-label="Comparar antes y después: {esc(label)}">
  </div>
  <div class="ba-cap"><b>{esc(label)}</b><span class="muted">Desliza ↔</span></div>
</div>'''
    return f'<div class="ba-grid">{out}</div>'

def cta_band(title, text, href=WA_MAIN, label="Agendar mi cita", checks=None, dark=True):
    ch = ""
    if checks:
        ch = '<ul class="checks">' + "".join(f"<li>{c}</li>" for c in checks) + "</ul>"
    return f'''<section class="section cta-band{' dark' if dark else ''}">
  <div class="wrap">
    <span class="eyebrow">Tu primera consulta</span>
    <h2 class="rv">{title}</h2>
    <p class="lead rv rv-d1">{text}</p>
    {ch}
    <div class="btn-row rv rv-d2"><a class="btn btn--bronze" href="{href}" target="_blank" rel="noopener">{label} {ARROW}</a><a class="btn btn--ghost" href="tel:{PHONE_RAW}">Llamar {PHONE}</a></div>
  </div>
</section>'''

def index_list(cat, hidden=False):
    rows = ""
    n = 0
    for p in PROCS:
        if p["cat"] != cat: continue
        n += 1
        rows += f'''<li><a href="{p["slug"]}.html" data-preview="" data-label="{esc(p["name"])}">
  <span class="n">0{n}</span><h3>{esc(p["name"])}</h3><p>{esc(p["short"])}</p><span class="go">{ARROW}</span></a></li>'''
    return f'<ul class="index-list" id="panel-{cat}" role="tabpanel" aria-labelledby="tab-{cat}"{" hidden" if hidden else ""}>{rows}</ul>'

# =========================================================
# INICIO
# =========================================================
home = f"""
<section class="hero-full" aria-label="Portada">
  <div class="hero-full__media">
    <picture>
      <source media="(max-width: 700px)" srcset="assets/img/quirofano/q-luz.jpg">
      <img src="assets/img/doctor/hero-quirofano.jpg" alt="El Dr. Luis Alonso Salja en quirófano" width="1920" height="1282" fetchpriority="high">
    </picture>
  </div>
  <div class="hero-full__shade" aria-hidden="true"></div>
  <div class="wrap hero-full__in">
    <span class="eyebrow">Cirujano plástico certificado · Barranquilla</span>
    <h1><span class="line"><span>Transformando belleza</span></span><span class="line"><span>con <em>precisión</em> y naturalidad.</span></span></h1>
    <p class="lead">Innovación, experiencia y procedimientos de última generación para resultados que inspiran confianza.</p>
    <div class="btn-row">
      <a class="btn btn--light" href="{WA_MAIN}" target="_blank" rel="noopener">Agenda tu cita {ARROW}</a>
      <a class="btn btn--ghost" href="#resultados">Ver resultados reales</a>
      <button class="play-btn" type="button" data-video="assets/video/hero.mp4" aria-label="Ver video del doctor en quirófano"><i>{PLAY}</i>Ver video</button>
    </div>
  </div>
  <div class="wrap hero-full__bar">
    <div class="stat"><b><span data-count="3500">0</span><sup>+</sup></b><span>Cirugías completadas</span></div>
    <div class="stat"><b><span data-count="15">0</span><sup>+</sup></b><span>Años de experiencia</span></div>
    <div class="stat"><b><span data-count="10">0</span><sup>+</sup></b><span>Procedimientos</span></div>
    <div class="stat"><b><span data-count="100">0</span><sup>%</sup></b><span>Satisfacción</span></div>
  </div>
</section>

<dialog class="vmodal" aria-label="Video">
  <button class="vmodal__close" type="button" aria-label="Cerrar video">×</button>
  <video controls playsinline preload="none"></video>
</dialog>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{"".join("<span>Transforma tu imagen</span><span>Fortalece tu confianza</span>" for _ in range(4))}</div></div>

<section class="section scroller" id="resultados" data-scroller data-auto>
  <div class="wrap">
    <div class="proc-head">
      <div><span class="eyebrow">Resultados reales</span><h2 class="rv">Tú también puedes <em>verte así</em></h2></div>
      <div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div>
    </div>
    <div class="hs-track ba-track">
      {ba_real("corporal", 12, "Contorno corporal")}
      {ba_real("gluteos", 2, "Glúteos")}
      {ba_real("corporal", 0, "Abdomen")}
      {ba_real("mamaria", 4, "Estética mamaria")}
      {ba_real("gluteos", 4, "Glúteos")}
      {ba_real("corporal", 35, "Abdomen y cintura")}
      {ba_real("corporal", 43, "Contorno corporal")}
      {ba_real("mamaria", 5, "Estética mamaria")}
    </div>
    <div class="results-cta rv">
      <p>¿Quieres un resultado así? Envíanos tu caso y te orientamos.</p>
      <a class="btn btn--bronze" href="{WA_MAIN}" target="_blank" rel="noopener">Quiero mi valoración {ARROW}</a>
    </div>
    <p class="fine">Pacientes reales del Dr. Luis Alonso Salja. Los resultados varían en cada paciente; las fotografías se publican con autorización y tienen fines informativos.</p>
  </div>
</section>

<section class="section stone scroller" data-scroller>
  <div class="wrap">
    <div class="proc-head">
      <div><span class="eyebrow">Procedimientos</span><h2 class="rv">¿Qué deseas <em>transformar?</em></h2></div>
      <div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div>
    </div>
    <div class="hs-track">{proc_scroller()}</div>
    <p style="margin-top:8px"><a class="link-arrow" href="procedimientos.html">Ver todos los procedimientos {ARROW}</a></p>
  </div>
</section>

<section class="section dark scroller" data-scroller>
  <div class="wrap">
    <div class="proc-head">
      <div><span class="eyebrow">En video</span><h2 class="rv">El doctor te lo <em>explica</em></h2></div>
      <div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div>
    </div>
    <div class="hs-track reels">{reels_block()}</div>
    <p style="margin-top:8px"><a class="link-arrow" href="{IG}" target="_blank" rel="noopener">47,9 mil personas lo siguen en Instagram {ARROW}</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="hero__media rv" style="justify-self:center"><div class="arch"><img src="assets/img/doctor/scrubs-sonrisa.jpg" alt="Dr. Luis Alonso Salja sonriendo con su uniforme quirúrgico" loading="lazy" width="1000" height="1497"></div><div class="note"><span class="hand">Te esperamos</span>Consultorio 403 · Quantum Tower, Barranquilla</div></div>
    <div>
      <span class="eyebrow">Excelencia médica</span>
      <h2 class="rv">Experiencia que marca la <em>diferencia</em></h2>
      <p class="lead rv rv-d1" style="margin-top:22px">Médico egresado de la Universidad de Cartagena y Cirujano Plástico, Estético y Reconstructivo de la Universidad Nacional de Colombia.</p>
      <ul class="badges rv rv-d2">
        <li><b>+15</b> años de experiencia</li>
        <li><b>Docente</b> de posgrado · U. Simón Bolívar</li>
        <li><b>Miembro</b> SCCP · FILACP</li>
      </ul>
      <div class="sign rv rv-d3"><span class="hand">Luis Alonso</span><a class="link-arrow" href="sobre-mi.html">Acerca de mí {ARROW}</a></div>
    </div>
  </div>
</section>

{team_block(dark=True)}

<section class="section stone">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Turismo médico</span>
      <h2 class="rv">Tu transformación, en un destino que te <em>cuida</em></h2>
      <p class="lead rv rv-d1" style="margin:22px 0 30px">Vuelos, hospedaje, traslados y recuperación: nosotros lo coordinamos.</p>
      <a class="btn btn--ghost rv rv-d2" href="turismo-medico.html">Planear mi viaje {ARROW}</a>
    </div>
    <div class="pass rv" aria-label="Pase de abordar ilustrativo hacia Barranquilla">
      <div class="pass__main">
        <div class="pass__top"><span>Pase de transformación</span><span>LAS · 403</span></div>
        <div class="pass__route"><div><b>TU</b><small>Tu ciudad</small></div><div class="pass__plane">{I_PLANE}</div><div style="text-align:right"><b>BAQ</b><small>Barranquilla</small></div></div>
        <div class="pass__meta"><div><span>Pasajero</span><b>Tú</b></div><div><span>Destino</span><b>Quantum Tower</b></div><div><span>Clase</span><b>Bienestar</b></div></div>
      </div>
      <div class="pass__stub"><div><span>Puerta</span><b>Consultorio 403</b></div><div><span>Abordaje</span><b>Tu valoración</b></div><div class="barcode" aria-hidden="true"></div></div>
    </div>
  </div>
</section>

{cta_band("Todo comienza con una <em>valoración</em>", "Diseñamos un plan a tu medida. Escríbenos y resolvemos tus dudas por WhatsApp.", checks=["Diagnóstico profesional", "Plan personalizado", "Resultados naturales", "Atención individual"])}
"""
page("index.html", "Dr. Luis Alonso Salja | Cirujano Plástico en Barranquilla",
     "Cirujano plástico certificado en Barranquilla. Mamoplastia, abdominoplastia, liposucción y más, con resultados naturales y seguridad. Agenda tu valoración.", home, "index.html", "has-hero")

# =========================================================
# SOBRE MÍ
# =========================================================
about = f'''
<section class="page-hero">
  <div class="wrap split split--wide">
    <div>
      <span class="eyebrow">Dr. Luis Alonso Salja</span>
      <h1 class="rv">Conoce al Dr. Luis <em>Alonso Salja</em></h1>
      <p class="lead rv rv-d1" style="margin-top:28px">Médico graduado de la Universidad de Cartagena y especialista en Cirugía Plástica, Estética y Reconstructiva de la Universidad Nacional de Colombia, con una trayectoria enfocada en la seguridad del paciente, la precisión quirúrgica y los resultados naturales.</p>
      <p class="rv rv-d2">Mantiene una actualización constante en técnicas y avances científicos para ofrecer procedimientos respaldados por los más altos estándares de calidad.</p>
      <p class="rv rv-d2">Actualmente es docente de posgrado en la Especialización en Cirugía Plástica de la Universidad Simón Bolívar, donde contribuye a la formación de nuevos especialistas.</p>
      <p class="rv rv-d3" style="margin:26px 0 0;font-weight:600">Miembro de sociedades científicas de cirugía plástica:</p>
      <ul class="socs rv rv-d3"><li>Sociedad Colombiana de Cirugía Plástica, Estética y Reconstructiva (SCCP)</li><li>Federación Ibero Latinoamericana de Cirugía Plástica (FILACP)</li></ul>
    </div>
    <div class="hero__media" style="justify-self:center">
      <div class="arch"><img src="assets/img/doctor/arco.jpg" alt="Dr. Luis Alonso Salja" width="1200" height="1797"></div>
      <div class="note"><span class="hand">Luis Alonso</span>Cirujano plástico, estético y reconstructivo</div>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Mis valores como médico</span>
      <p class="quote rv">Mi práctica se fundamenta en principios que guían cada decisión clínica y cada procedimiento.</p>
    </div>
    <div>
      <p class="lead rv rv-d1">La confianza que depositas en mí la respondo con ética, dedicación y un compromiso genuino con tu bienestar integral.</p>
      <div class="sign rv rv-d2"><span class="hand">Luis Alonso</span><small>Dr. Luis Alonso Salja</small></div>
    </div>
  </div>
  <div class="wrap">
    <div class="values" style="color:var(--ink)">
      <div class="value rv"><i><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg></i><h3>Seguridad ante todo</h3><p>Protocolos rigurosos y tecnología de vanguardia para garantizar tu bienestar en cada etapa.</p></div>
      <div class="value rv rv-d1"><i><svg viewBox="0 0 24 24"><path d="M12 21c-4-3-8-6.5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 4.5-4 8-8 11z"/></svg></i><h3>Resultados naturales</h3><p>Realzamos tu belleza sin perder tu esencia, con armonía y proporción.</p></div>
      <div class="value rv rv-d2"><i><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg></i><h3>Atención personalizada</h3><p>Acompañamiento cercano, escuchando tus necesidades y expectativas reales.</p></div>
      <div class="value rv rv-d3"><i><svg viewBox="0 0 24 24"><path d="M12 2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17l-6.1 3.4 1.5-6.8L2.2 9l6.9-.7L12 2z"/></svg></i><h3>Excelencia</h3><p>Formación continua y técnica precisa en cada procedimiento que realizamos.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split split--wide">
    <div>
      <span class="eyebrow">Nuestro equipo médico</span>
      <h2 class="rv">La excelencia comienza con nuestro <em>equipo</em></h2>
      <p class="lead rv rv-d1" style="margin-top:22px">Cada procedimiento es el resultado de un trabajo coordinado entre especialistas comprometidos con tu seguridad, tu bienestar y resultados que trascienden.</p>
      <div class="btn-row rv rv-d2"><a class="btn btn--bronze" href="{WA_MAIN}" target="_blank" rel="noopener">Contáctanos {ARROW}</a><a class="btn btn--ghost" href="contacto.html#equipo">Conocer al equipo</a></div>
    </div>
    <figure class="photo-frame rv" style="margin:0;aspect-ratio:4/5"><img src="assets/img/consultorio/equipo-logo.jpg" alt="El Dr. Luis Alonso Salja con parte de su equipo médico" loading="lazy" width="819" height="1024"></figure>
  </div>
</section>
<section class="section scroller" data-scroller>
  <div class="wrap">
    <div class="proc-head">
      <div><span class="eyebrow">En quirófano</span><h2 class="rv">Precisión en cada <em>detalle</em></h2></div>
      <div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div>
    </div>
    <div class="hs-track">{"".join(f'<figure class="qshot"><img src="assets/img/quirofano/{q}.jpg" alt="El Dr. Luis Alonso Salja durante una cirugía" loading="lazy"></figure>' for q in ["q5", "q-luz", "q2", "q7", "q10", "q8", "q12", "q11"])}</div>
  </div>
</section>
<section class="section dark">
  <div class="wrap">
    <span class="eyebrow">Filosofía</span>
    <h2 class="rv">Tu seguridad es nuestra <em>prioridad</em></h2>
    <div class="pillars">
      <div class="pillar rv"><span class="num">01</span><h3>Seguridad</h3><p>Prácticas hospitalarias rigurosas, equipo de anestesia certificado y trazabilidad completa de cada procedimiento quirúrgico.</p></div>
      <div class="pillar rv rv-d1"><span class="num">02</span><h3>Precisión</h3><p>Planeación milimétrica de cada procedimiento. La belleza es consecuencia de la exactitud, no del exceso.</p></div>
      <div class="pillar rv rv-d2"><span class="num">03</span><h3>Resultados naturales</h3><p>El objetivo nunca es cambiar su esencia. Es realzar su belleza con equilibrio, naturalidad y precisión.</p></div>
    </div>
  </div>
</section>
{team_block(dark=False)}
'''
page("sobre-mi.html", "Sobre mí | Dr. Luis Alonso Salja, Cirujano Plástico",
     "Conoce al Dr. Luis Alonso Salja: cirujano plástico de la Universidad Nacional de Colombia, docente de posgrado y miembro de la SCCP y la FILACP.", about, "sobre-mi.html")

# =========================================================
# PROCEDIMIENTOS
# =========================================================
cards = ""
for p in PROCS:
    cards += f'''<a class="pcard rv" href="{p["slug"]}.html" data-cat="{p["cat"]}">
  <div class="pcard__img">{('<img src="assets/img/' + CARD_IMG[p["slug"]] + '" alt="Resultado de ' + esc(p["name"].lower()) + '" loading="lazy">') if p["slug"] in CARD_IMG else ph("Foto: " + p["name"])}<span class="pcard__tag">{CATS[p["cat"]]}</span></div>
  <h3>{esc(p["name"])}</h3>
  <p>{esc(p["card"])}</p>
  <span class="link-arrow">Ver procedimiento {ARROW}</span>
</a>'''
procs_page = f'''
<section class="page-hero">
  <div class="wrap split split--wide">
    <div>
      <span class="eyebrow">Dr. Luis Alonso Salja</span>
      <h1 class="rv">Encuentra el tratamiento ideal <em>para ti.</em></h1>
      <p class="lead rv rv-d1" style="margin:26px 0 34px">Cada transformación comienza con una valoración personalizada y un plan diseñado exclusivamente para ti.</p>
      <a class="btn btn--bronze rv rv-d2" href="{WA_MAIN}" target="_blank" rel="noopener">Agenda tu cita {ARROW}</a>
    </div>
    <div class="hero__media" style="justify-self:center"><div class="arch"><img src="assets/img/doctor/scrubs-brazos.jpg" alt="Dr. Luis Alonso Salja con uniforme quirúrgico" width="1000" height="1497"></div></div>
  </div>
</section>
<section class="section" style="padding-top:20px">
  <div class="wrap">
    <span class="eyebrow">Nuestros procedimientos</span>
    <h2 class="rv">Transforma tu imagen con <em>confianza</em></h2>
    <p class="lead rv rv-d1" style="margin-top:20px">Procedimientos personalizados con tecnología avanzada y resultados que realzan tu mejor versión. Cada detalle pensado para ti.</p>
    <div class="chips" role="group" aria-label="Filtrar procedimientos">
      <button class="chip" type="button" data-filter="todos" aria-pressed="true">Todos</button>
      <button class="chip" type="button" data-filter="mamaria" aria-pressed="false">Estética mamaria</button>
      <button class="chip" type="button" data-filter="corporal" aria-pressed="false">Contorno corporal</button>
    </div>
    <div class="pgrid">{cards}</div>
  </div>
</section>
<section class="section dark">
  <div class="wrap split">
    <div style="align-self:start;position:sticky;top:120px">
      <span class="eyebrow">Post operatorio</span>
      <h2 class="rv">Recuperación</h2>
      <p class="lead rv rv-d1" style="margin-top:20px">Un plan personalizado y seguimiento cercano en cada etapa.</p>
    </div>
    <div class="timeline">
      <span class="timeline__fill" aria-hidden="true"></span>
      <div class="tl rv"><i>1</i><div><h3>Primeras 48 horas</h3><p>Las primeras horas estarán orientadas a controlar la inflamación, favorecer el descanso y comenzar con una recuperación segura. Nuestro equipo estará disponible para resolver tus dudas en cada paso.</p></div></div>
      <div class="tl rv"><i>2</i><div><h3>Primera y segunda semana</h3><p>Es normal presentar inflamación y molestias leves. Poco a poco podrás retomar actividades cotidianas siguiendo las indicaciones médicas, respetando siempre los tiempos de cicatrización de tu cuerpo.</p><p>Actividades físicas restringidas 4–6 semanas, individualizadas por caso.</p></div></div>
      <div class="tl rv"><i>3</i><div><h3>Seguimiento personalizado</h3><p>La cirugía es solo el comienzo. Te acompañamos durante todo el proceso con seguimiento médico cercano, indicaciones precisas y el respaldo de un equipo comprometido con tu bienestar y resultados óptimos.</p></div></div>
    </div>
  </div>
</section>
{cta_band("¿No sabes cuál es el procedimiento <em>ideal para ti?</em>", "Cada transformación comienza con una valoración personalizada y un plan diseñado exclusivamente para ti.", label="Agenda tu cita", dark=False)}
'''
page("procedimientos.html", "Procedimientos | Dr. Luis Alonso Salja, Cirugía Plástica",
     "Mamoplastia de aumento, reducción mamaria, mastopexia, explantación, abdominoplastia, liposucción, transferencia de grasa y retracción de piel en Barranquilla.", procs_page, "procedimientos.html")

# =========================================================
# DETALLE DE CADA PROCEDIMIENTO
# =========================================================
for i, p in enumerate(PROCS):
    faq = "".join(f'<details class="rv"><summary>{esc(q)}<i aria-hidden="true"></i></summary><p>{esc(a)}</p></details>' for q, a in p["faq"])
    ap = "".join(f'<div class="ap rv rv-d{k}"><span class="num">0{k+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for k, (t, d) in enumerate(p["approach"]))
    others = [o for o in PROCS if o["cat"] == p["cat"] and o is not p][:3]
    if len(others) < 3: others += [o for o in PROCS if o["cat"] != p["cat"]][:3 - len(others)]
    rel = "".join(f'<a href="{o["slug"]}.html">{esc(o["name"])} {ARROW}</a>' for o in others)
    intro = "".join(f'<p class="{"lead" if k == 0 else "muted"} rv rv-d{k+1}">{esc(t)}</p>' for k, t in enumerate(p["intro"]))
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><a href="procedimientos.html">Procedimientos</a><span>/</span><span>{esc(p["name"])}</span></nav>
    <div class="detail-hero">
      <div>
        <span class="eyebrow">{CATS[p["cat"]]} · Dr. Luis Alonso Salja</span>
        <h1 class="rv" style="font-size:clamp(44px,6vw,88px);margin-bottom:28px">{esc(p["name"])}</h1>
        {intro}
        <div class="btn-row rv rv-d3" style="margin-top:30px"><a class="btn btn--bronze" href="{p["wa"]}" target="_blank" rel="noopener">Agenda valoración {ARROW}</a><a class="btn btn--ghost" href="#faq">Preguntas frecuentes</a></div>
      </div>
      <div class="hero__media" style="justify-self:center"><div class="arch">{('<img src="assets/img/' + CARD_IMG[p["slug"]] + '" alt="Resultado de ' + esc(p["name"].lower()) + '">') if p["slug"] in CARD_IMG else ph("Foto: " + p["name"])}</div></div>
    </div>
  </div>
</section>
<section class="section stone{' scroller' if len(RESULTS.get(p['slug'], [])) >= 4 else ''}" id="resultados"{' data-scroller data-auto' if len(RESULTS.get(p['slug'], [])) >= 4 else ''}>
  <div class="wrap">
    <div class="proc-head"><div><span class="eyebrow">Resultados reales</span><h2 class="rv">Casos de nuestros <em>pacientes</em></h2></div><a class="btn btn--bronze" href="{p["wa"]}" target="_blank" rel="noopener">Quiero un resultado así {ARROW}</a></div>
    <div class="{'hs-track ba-track' if len(RESULTS.get(p['slug'], [])) >= 4 else 'ba-grid ba-grid--4'}">{results_for(p["slug"]) or ba_block(["Caso 1", "Caso 2", "Caso 3"])}</div>
    <p class="fine">Pacientes reales del Dr. Luis Alonso Salja. Los resultados varían en cada paciente; las fotografías se publican con autorización y tienen fines informativos.</p>
  </div>
</section>
<section class="section dark">
  <div class="wrap">
    <span class="eyebrow">Mi enfoque quirúrgico</span>
    <h2 class="rv">{p["approach_title"]}</h2>
    <div class="approach">{ap}</div>
  </div>
</section>
<section class="section" id="faq">
  <div class="wrap split" style="align-items:start">
    <div style="position:sticky;top:120px">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2 class="rv">Resolvemos tus <em>dudas</em></h2>
      <p class="lead rv rv-d1" style="margin:22px 0 30px">¿Tienes otra pregunta? Escríbenos y te respondemos personalmente.</p>
      <a class="btn btn--ghost" href="{p["wa"]}" target="_blank" rel="noopener">Preguntar por WhatsApp {ARROW}</a>
    </div>
    <div class="faq" style="margin-top:0">{faq}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <span class="eyebrow">También te puede interesar</span>
    <div class="related">{rel}</div>
  </div>
</section>
{cta_band("Agenda tu valoración de <em>" + esc(p["name"].lower()) + "</em>", "Conoceremos tus objetivos, resolveremos tus inquietudes y diseñaremos un plan que priorice tu seguridad y respete tu anatomía.", href=p["wa"], label="Agenda valoración")}
'''
    page(f'{p["slug"]}.html', f'{p["name"]} en Barranquilla | Dr. Luis Alonso Salja',
         p["card"][:155], body, "procedimientos.html")

# =========================================================
# TURISMO MÉDICO
# =========================================================
proc_opts = "".join(f"<option>{esc(p['name'])}</option>" for p in PROCS)
tour = f'''
<section class="page-hero">
  <div class="wrap split split--wide">
    <div>
      <span class="eyebrow">Turismo médico</span>
      <h1 class="rv">Tu transformación, en un destino que te <span class="scribble">cuida{SCRIBBLE}</span></h1>
      <p class="lead rv rv-d1" style="margin:28px 0 34px">Viaja con confianza para recibir atención quirúrgica de excelencia, combinando seguridad, resultados naturales y una experiencia diseñada para tu bienestar.</p>
      <a class="btn btn--bronze rv rv-d2" href="#agenda">Agenda tu cita {ARROW}</a>
    </div>
    <div class="pass rv rv-d2" aria-label="Pase de abordar ilustrativo hacia Barranquilla">
      <div class="pass__main">
        <div class="pass__top"><span>Pase de transformación</span><span>LAS · 403</span></div>
        <div class="pass__route"><div><b>TU</b><small>Tu ciudad</small></div><div class="pass__plane">{I_PLANE}</div><div style="text-align:right"><b>BAQ</b><small>Barranquilla</small></div></div>
        <div class="pass__meta"><div><span>Pasajero</span><b>Tú</b></div><div><span>Destino</span><b>Quantum Tower</b></div><div><span>Clase</span><b>Bienestar</b></div></div>
      </div>
      <div class="pass__stub"><div><span>Puerta</span><b>Consultorio 403</b></div><div><span>Abordaje</span><b>Tu valoración</b></div><div class="barcode" aria-hidden="true"></div></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:20px">
  <div class="wrap">
    <div class="mosaic rv">
      <figure class="photo-frame" style="margin:0"><img src="assets/img/barranquilla/noria.jpg" alt="Rueda de la fortuna Luna del Río en el Gran Malecón de Barranquilla" loading="lazy" width="960" height="1280"><figcaption>Rueda de la fortuna · Gran Malecón</figcaption></figure>
      <figure class="photo-frame" style="margin:0"><img src="assets/img/barranquilla/muelle.jpg" alt="Atardecer en el Muelle 1888 de Puerto Colombia" loading="lazy" width="960" height="1280" style="object-position:50% 62%"><figcaption>Muelle 1888 · Puerto Colombia</figcaption></figure>
      <figure class="photo-frame" style="margin:0"><img src="assets/img/barranquilla/arepa.jpg" alt="Arepas de huevo, plato típico de la costa Caribe" loading="lazy" width="1200" height="900"><figcaption>Arepa de huevo</figcaption></figure>
      <figure class="photo-frame" style="margin:0"><img src="assets/img/consultorio/equipo-trio.jpg" alt="El Dr. Luis Alonso Salja con parte de su equipo en el consultorio" loading="lazy" width="1024" height="819" style="object-position:50% 30%"><figcaption>Te recibimos en Quantum Tower</figcaption></figure>
    </div>
  </div>
</section>
<section class="section stone">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Barranquilla, Colombia</span>
      <h2 class="rv">Un destino que te recibe como en <em>casa</em></h2>
      <p class="lead rv rv-d1" style="margin-top:22px">Barranquilla es una ciudad vibrante, cálida y llena de vida. Su gente, su cultura y su clima te harán sentir acompañado durante toda tu experiencia.</p>
    </div>
    <div>
      <span class="eyebrow">Tu viaje, nuestra ciudad</span>
      <h3 class="rv" style="font-size:clamp(30px,3.4vw,44px)">Descubre Colombia mientras te <em>transformas</em></h3>
      <p class="rv rv-d1" style="margin-top:18px">Desde el mar Caribe hasta su gastronomía y cultura, Barranquilla ofrece todo lo que necesitas para una recuperación tranquila y una experiencia inolvidable.</p>
    </div>
  </div>
</section>
<section class="section scroller" data-scroller>
  <div class="wrap">
    <div class="proc-head">
      <div><span class="eyebrow">Sabores del Caribe</span><h2 class="rv">Tu recuperación también <em>sabe a Barranquilla</em></h2></div>
      <div class="team__ctrl"><button class="circle-btn" type="button" data-prev aria-label="Anterior">{ARROW_L}</button><button class="circle-btn" type="button" data-next aria-label="Siguiente">{ARROW}</button></div>
    </div>
    <div class="hs-track"><figure class="food"><img src="assets/img/barranquilla/arepa.jpg" alt="Arepa de huevo" loading="lazy"><figcaption><b>Arepa de huevo</b>El desayuno costeño por excelencia.</figcaption></figure><figure class="food"><img src="assets/img/barranquilla/butifarra.jpg" alt="Butifarra soledeña" loading="lazy"><figcaption><b>Butifarra soledeña</b>Con limón y bollo de yuca, como en Soledad.</figcaption></figure><figure class="food"><img src="assets/img/barranquilla/carimanolas.jpg" alt="Carimañolas y empanadas" loading="lazy"><figcaption><b>Carimañolas y empanadas</b>Fritos crujientes para la tarde.</figcaption></figure><figure class="food"><img src="assets/img/barranquilla/mote.jpg" alt="Mote de queso" loading="lazy"><figcaption><b>Mote de queso</b>Sopa de ñame con queso costeño.</figcaption></figure><figure class="food"><img src="assets/img/barranquilla/sancocho.jpg" alt="Sancocho de guandú" loading="lazy"><figcaption><b>Sancocho de guandú</b>El almuerzo de domingo en familia.</figcaption></figure></div>
    <p class="fine">Siempre siguiendo las indicaciones médicas de tu dieta post operatoria.</p>
    <p class="fine credits">Fotos de Barranquilla: Wikimedia Commons — «Noria Luna del Río» y comidas típicas por Jdvillalobos (CC BY-SA 4.0 / CC BY 3.0); «Atardecer en Muelle 1888» por Project5443 (CC0); «Mote de queso con chicharrón» por Futbolero (CC BY-SA 4.0).</p>
  </div>
</section>
<section class="section dark">
  <div class="wrap">
    <span class="eyebrow">El proceso</span>
    <h2 class="rv">De la idea a la realidad, <em>paso a paso</em></h2>
    <div class="route">
      <div class="route__step rv"><span class="route__dot">01</span><h3>Primera valoración</h3><p>Conversamos sobre tus objetivos y definimos el plan ideal.</p></div>
      <div class="route__step rv rv-d1"><span class="route__dot">02</span><h3>Coordinación de viaje</h3><p>Gestionamos vuelos, hospedaje y traslados.</p></div>
      <div class="route__step rv rv-d2"><span class="route__dot">03</span><h3>Día de tu cirugía</h3><p>Clínica certificada con equipo quirúrgico especializado.</p></div>
      <div class="route__step rv rv-d3"><span class="route__dot">04</span><h3>Recuperación</h3><p>Atención 24/7 y tiempo para descansar.</p></div>
    </div>
  </div>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee__track">{"".join("<span>Transforma tu imagen</span><span>Fortalece tu confianza</span>" for _ in range(4))}</div></div>
<section class="section" id="agenda">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow">Agenda tu viaje</span>
      <h2 class="rv">Tu transformación en Colombia te <em>espera</em></h2>
      <p class="lead rv rv-d1" style="margin-top:22px">Las citas para cirugía son limitadas. Cuéntanos sobre ti y te contactaremos para diseñar tu plan quirúrgico personalizado, incluyendo viaje, estadía y recuperación.</p>
      <ul class="checks"><li>Valoración virtual antes de viajar</li><li>Coordinación de vuelos, hospedaje y traslados</li><li>Acompañamiento durante toda tu recuperación</li></ul>
    </div>
    <div class="form-card rv rv-d1">
      <form class="form" data-wa="Hola, quiero planear mi viaje para cirugía con el Dr. Luis Alonso Salja." novalidate>
        <div class="field"><label for="t-nombre">Nombre *</label><input id="t-nombre" name="nombre" autocomplete="name" required><span class="err">Escribe tu nombre.</span></div>
        <div class="field"><label for="t-pais">País y ciudad *</label><input id="t-pais" name="pais" autocomplete="country-name" required><span class="err">Cuéntanos desde dónde viajas.</span></div>
        <div class="field"><label for="t-proc">Procedimiento de interés</label><select id="t-proc" name="procedimiento"><option value="">Aún no lo sé</option>{proc_opts}</select></div>
        <div class="field"><label for="t-fecha">Fecha tentativa de viaje</label><input id="t-fecha" name="fecha" type="month"></div>
        <div class="field field--full"><label for="t-msg">Mensaje</label><textarea id="t-msg" name="mensaje" placeholder="Cuéntanos tus objetivos o dudas"></textarea></div>
        <div class="field field--full"><button class="btn btn--bronze" type="submit">Enviar por WhatsApp {ARROW}</button><p class="form-note">Se abrirá WhatsApp con tu mensaje listo para enviar.</p></div>
      </form>
    </div>
  </div>
</section>
<section class="section stone">
  <div class="wrap">
    <div class="proc-head">
      <div><span class="eyebrow">Pacientes que viajaron</span><h2 class="rv">Mira lo que hemos <em>logrado</em></h2></div>
      <div class="social" style="margin:0"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram" style="border-color:var(--line)">{I_IG.replace('aria-hidden="true"', 'aria-hidden="true" style="fill:var(--ink)"')}</a><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook" style="border-color:var(--line)">{I_FB.replace('aria-hidden="true"', 'aria-hidden="true" style="fill:var(--ink)"')}</a><a href="{TT}" target="_blank" rel="noopener" aria-label="TikTok" style="border-color:var(--line)">{I_TT.replace('aria-hidden="true"', 'aria-hidden="true" style="fill:var(--ink)"')}</a></div>
    </div>
    <div class="pgrid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
      <div style="aspect-ratio:4/5;border-radius:var(--r);overflow:hidden">{ph("Video / testimonio 1")}</div>
      <div style="aspect-ratio:4/5;border-radius:var(--r);overflow:hidden">{ph("Video / testimonio 2")}</div>
      <div style="aspect-ratio:4/5;border-radius:var(--r);overflow:hidden">{ph("Video / testimonio 3")}</div>
      <div style="aspect-ratio:4/5;border-radius:var(--r);overflow:hidden">{ph("Video / testimonio 4")}</div>
    </div>
  </div>
</section>
'''
page("turismo-medico.html", "Turismo Médico en Barranquilla | Dr. Luis Alonso Salja",
     "Viaja a Barranquilla para tu cirugía plástica: valoración, coordinación de viaje, cirugía en clínica certificada y recuperación con atención 24/7.", tour, "turismo-medico.html")

# =========================================================
# CONTACTO
# =========================================================
contact = f'''
<section class="page-hero">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow">Contacto</span>
      <h1 class="rv" style="font-size:clamp(48px,6.4vw,92px)">¿Tienes <em>preguntas?</em></h1>
      <p class="lead rv rv-d1" style="margin-top:24px">Nuestro equipo está listo para ayudarte. Diligencia el formulario y uno de nuestros asesores te contactará.</p>
      <div class="cinfo">
        <a href="tel:{PHONE_RAW}"><i>{I_PHONE}</i><span><small>Teléfono / Celular</small><b>{PHONE}</b></span></a>
        <a href="mailto:{EMAIL}"><i>{I_MAIL}</i><span><small>Correo electrónico</small><b>{EMAIL}</b></span></a>
        <a href="https://www.google.com/maps/search/?api=1&query=Quantum+Tower+Calle+85+50-159+Barranquilla" target="_blank" rel="noopener"><i>{I_PIN}</i><span><small>Ubicación</small><b>{ADDRESS}, Barranquilla</b></span></a>
      </div>
    </div>
    <div class="form-card rv rv-d1">
      <h2 style="font-size:clamp(32px,3.6vw,46px);margin-bottom:8px">Agenda tu <em>valoración</em></h2>
      <p class="muted" style="margin-bottom:26px">Comience su transformación con confianza.</p>
      <form class="form" data-wa="Hola, quiero agendar una valoración con el Dr. Luis Alonso Salja." novalidate>
        <div class="field"><label for="c-nombre">Nombre *</label><input id="c-nombre" name="nombre" autocomplete="name" required><span class="err">Escribe tu nombre.</span></div>
        <div class="field"><label for="c-tel">Celular *</label><input id="c-tel" name="celular" type="tel" autocomplete="tel" inputmode="tel" required><span class="err">Escribe un número de contacto.</span></div>
        <div class="field"><label for="c-ciudad">Ciudad / país</label><input id="c-ciudad" name="ciudad" autocomplete="address-level2"></div>
        <div class="field"><label for="c-proc">Procedimiento de interés</label><select id="c-proc" name="procedimiento"><option value="">Aún no lo sé</option>{proc_opts}</select></div>
        <div class="field field--full"><label for="c-msg">Mensaje</label><textarea id="c-msg" name="mensaje" placeholder="Cuéntanos qué te gustaría lograr"></textarea></div>
        <div class="field field--full"><button class="btn btn--bronze" type="submit">Enviar por WhatsApp {ARROW}</button><p class="form-note">Se abrirá WhatsApp con tu mensaje listo para enviar.</p></div>
      </form>
    </div>
  </div>
</section>
{team_block(dark=True)}
<section class="section section--tight">
  <div class="wrap">
    <div class="map"><iframe title="Mapa: Quantum Tower, Barranquilla" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Quantum+Tower+Calle+85+%2350-159+Barranquilla&output=embed"></iframe></div>
  </div>
</section>
'''
page("contacto.html", "Contacto | Dr. Luis Alonso Salja, Cirujano Plástico",
     "Agenda tu valoración con el Dr. Luis Alonso Salja. Calle 85 #50-159, Quantum Tower, consultorio 403, Barranquilla. Tel. +57 302 284 1740.", contact, "contacto.html")

# =========================================================
# GUÍA DE MARCA (para presentar al cliente)
# =========================================================
def sw(hexv, name, pms, role):
    return f'<div class="sw"><div style="background:{hexv}"></div><p><b>{name}</b><code>{hexv}</code><br>{pms}<br><span class="muted">{role}</span></p></div>'
brand = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Propuesta de identidad web</span>
    <h1 class="rv">Grafito &amp; <em>Plata</em></h1>
    <p class="lead rv rv-d1" style="margin-top:24px">La paleta del doctor son los grises: el logo plateado, la pared de estuco gris del consultorio y los grises que ya usa el sitio. La propuesta los conserva y los ordena en un sistema más sobrio y elegante. El calor humano lo ponen las fotografías del equipo, no el color.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">Paleta actual del sitio</span>
    <h2 class="rv">Lo que hay hoy</h2>
    <p class="muted" style="margin-top:14px">Extraída de las hojas de estilo de drluisalonsosalja.com. Las equivalencias Pantone son aproximadas y deben confirmarse con una guía física Pantone.</p>
    <div class="swatches">
      {sw("#000000", "Negro", "≈ PANTONE Black 6 C", "Textos y botones")}
      {sw("#1B2026", "Grafito", "≈ PANTONE 433 C", "Fondos oscuros")}
      {sw("#8E939A", "Gris frío", "≈ PANTONE Cool Gray 8 C", "Textos secundarios")}
      {sw("#DAD6D3", "Gris cálido", "≈ PANTONE Warm Gray 1 C", "Bordes y fondos")}
      {sw("#EAE9E7", "Niebla", "≈ PANTONE Cool Gray 1 C (más claro)", "Fondos de sección")}
      {sw("#FFFFFF", "Blanco", "PANTONE White", "Fondo base")}
    </div>
    <p class="muted" style="margin-top:22px"><b>Tipografías actuales:</b> Cormorant Garamond (títulos), Manrope (menú) y Nunito Sans (botones). La plantilla además carga Roboto y Roboto Slab, que no se usan.</p>
  </div>
</section>
<section class="section dark">
  <div class="wrap">
    <span class="eyebrow">Manual de identidad corporativa oficial</span>
    <h2 class="rv">Lo que dice el <em>manual</em></h2>
    <p style="margin-top:14px">El manual de marca del doctor define el logo en <b>Trajan Pro</b>, una caligrafía de apoyo (<b>Halimun</b>) y esta gama cromática. Los grises aparecen como versión en escala de grises del logo. La propuesta web usa los grises como base, como pidió el cliente; el dorado del manual queda disponible como acento si se quiere.</p>
    <div class="swatches" style="color:var(--ink)">
      {sw("#010002", "Negro", "CMYK 84 · 83 · 73 · 80", "Manual oficial")}
      {sw("#704415", "Bronce", "CMYK 0 · 67 · 91 · 59", "Manual oficial")}
      {sw("#5B2616", "Caoba", "CMYK 49 · 95 · 100 · 36", "Manual oficial")}
      {sw("#9E7B2C", "Dorado", "CMYK 19 · 44 · 92 · 25", "Manual oficial")}
    </div>
    <p style="margin-top:22px">Equivalentes web: Trajan Pro → <b>Cinzel</b> (Google Fonts) · Halimun → <b>Mrs Saint Delafield</b>.</p>
  </div>
</section>
<section class="section stone">
  <div class="wrap">
    <span class="eyebrow">Paleta propuesta</span>
    <h2 class="rv">Grafito &amp; Plata</h2>
    <p class="muted" style="margin-top:14px">Cuatro de los seis colores son los mismos del sitio actual; se suman un gris acero para los botones y un blanco nube más cálido para el fondo.</p>
    <div class="swatches">
      {sw("#1B2026", "Grafito", "≈ PANTONE 433 C", "Textos y secciones oscuras · se conserva")}
      {sw("#4F5660", "Acero", "≈ PANTONE 431 C", "Botones y llamados a la acción · nuevo")}
      {sw("#8E939A", "Gris frío", "≈ PANTONE Cool Gray 8 C", "Detalles y líneas · se conserva")}
      {sw("#B9BDC2", "Plata", "≈ PANTONE 428 C", "Acentos sobre grafito, como el logo · nuevo")}
      {sw("#DAD6D3", "Estuco", "≈ PANTONE Warm Gray 1 C", "Fondos de imágenes · se conserva")}
      {sw("#EAE9E7", "Niebla", "≈ PANTONE Cool Gray 1 C (más claro)", "Fondos alternos · se conserva")}
      {sw("#F0EEE9", "Blanco nube", "≈ PANTONE 11-4201 TCX Cloud Dancer", "Fondo principal · nuevo")}
    </div>
    <p class="muted" style="margin-top:22px">Contrastes verificados para accesibilidad (WCAG AA): Grafito sobre Blanco nube 14:1 · Acero sobre Blanco nube 6,4:1 · Blanco sobre Acero 7,4:1 · Plata sobre Grafito 8,7:1.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <span class="eyebrow">Tipografía</span>
    <h2 class="rv" style="margin-bottom:34px">Tres voces</h2>
    <div class="specimen"><span class="eyebrow">Títulos · Cormorant Garamond</span><p class="big" style="font-family:var(--serif)">Belleza con <em style="color:var(--bronze)">precisión</em></p><p class="muted">Se conserva del sitio actual: es la misma familia del logo y da continuidad a la marca.</p></div>
    <div class="specimen"><span class="eyebrow">Textos · Instrument Sans</span><p class="big" style="font-family:var(--sans);font-size:clamp(32px,4vw,52px)">Seguridad, experiencia y acompañamiento</p><p class="muted">Reemplaza a Manrope y Nunito Sans: más legible y menos vista en plantillas.</p></div>
    <div class="specimen"><span class="eyebrow">Firma · Mrs Saint Delafield</span><p class="big hand" style="font-size:clamp(60px,8vw,110px)">Luis Alonso</p><p class="muted">Un trazo a mano, usado con moderación, para que el sitio se sienta humano y firmado por el doctor.</p></div>
  </div>
</section>
'''
page("guia-de-marca.html", "Guía de marca · Propuesta Grafito & Plata | Dr. Luis Alonso Salja",
     "Paleta, equivalencias Pantone y tipografías de la propuesta web para el Dr. Luis Alonso Salja.", brand)
