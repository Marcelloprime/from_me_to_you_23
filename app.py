import streamlit as st
import base64
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import pandas as pd
import numpy as np
import plotly.express as px
import datetime

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64("data/fondo.jpg")

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        padding: 0;
    }}

    /* Capa blanca central */
    .central-box {{
        background-color: rgba(255, 255, 255, 0.94); /* Más opaca para mayor contraste */
        padding: 3rem;
        margin: 5vh auto;
        width: 85%;
        max-width: 1000px;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Feliz mesiversario mi amor💕")

st.subheader('Palabras para mi amada enamorada Angela')

st.write('''

Preparé este detalle porque quería que darte algo con mucha originalidad, algo que forma parte de mí, de mi profesión, 
lo que estudio y me gusta tanto, junto a mi persona favorita.
Por eso, este proyecto significa mucho más que cualquier proyecto que he realizado antes porque aquí estoy juntando a mis dos amores: 
la estadística y tú.
Me dio risa que lo haya estado haciendo hasta al frente tuyo pero no estoy seguro si te lo esperabas, si pensabas que era nuestro chat.

Espero que te guste mucho, este será un análisis de todos los mensajes que nos hemos enviado desde que me escribiste aquel día, 
el cual yo estaba perdido JAJAJA

Sé que realmente nos sentimos como novios hace meses, sé que te he tratado como mi novia pero he demorado en pedirte para estar
porque he deseado hacerlo de la mejor manera posible pero oficialmente, nos hemos unido como enamorados un 23 de mayo del 2025 y espero
no nos conformemos con celebrar meses ni año, sino aspirar a llegar a bodas de plata, de oro y lo que siga.

Jamás olvidaré el primer día que te vi, aquel año nuevo, 1 de enero del 2025, cuando yo estaba en una fiesta de gente desconcida
y sin ganas de hacer nada realmente, desanimado porque se venía nuevas cosas en mi vida, nuevos retos y, peor aun, no pude ir a la playa con mis
amigos que tanto quería por una oportunidad de practicante que al final no se dio pero ¿Por algo se dan las cosas, no?

Entonces llegaste tú, la chica que destacó por encima de todas, la que tenía una bonita vibra, con un cabello precioso, una personalidad muy llamativa
desde que entró, ahi yo dije "ESTA CHICA ES MUY BONITA PERO ¿ESTARÁ LOCA?". No importó, solo sé que yo en ese entonces pensaba que no te iba a volver
a ver, solo pude apreciar tu belleza y quedarme con eso. Volviendo a mi casa todo alcoholizado pensando en ti, diciendo "Que bonita chica, no creo que
la vuelva a ver, ella vive muy lejos, no hay manera de coincidir con ella"

La vida decidió finalmente que yo no entre a realizar mis prácticas, obviamente me dolió de corazón porque estaba muy entusiasmado pero a la vez
estaba convencido que la vida lo hizo por algo, quizá algo iba a pasar entrando a Majorel y no se equivocó, nunca juzgué al destino.
Sin darme cuenta, el trabajo me ayudó a reencontrarnos, a poder de nuevo apreciar tu belleza pero sin intenciones de nada, solo decidí apreciar
tu amistad, me parecías muy divertida cuando empezamos a hablar, muy preocupada por mi, apoyándome desde siempre en cada cosa, viendo cómo buscabas
cualquier excusa para acercarte a mi, yo siempre me sentí agradecido contigo por cómo me tratabas pero sentía que había algo más por tu parte, además
que, de manera natural, me nació ayudarte, querer cuidarte, invitarte mi agua y querer pasar más tiempo contigo.

Fue así como poco a poco, estaba claro nuestro futuro amor, aunque ambos con tantas dudas de si arriesgarnos o no, decidimos dar un paso, vencer nuestros
miedos, dejar de lado todo aquello que antes nos había pasado y darlo todo por el otro. Me acuerdo cuando salimos juntos y no pude evitar que estaba palteado
porque sabía a lo que iba, no sentí que fuese una cita fea ni nada, sentí que ya me estabas gustando más ese día, escucharte me hizo conocer más aspectos de tu vida
y darme cuenta que me gusta cómo piensas, cómo sientes y darme cuenta que tienes todo lo que me gusta.

Desde ahí, todo subió y nunca nos frenamos, nos arriesgamos como si nunca antes nos hubiesen hecho daño, como si el mundo se acabara mañana y solo tenemos un día
para conocernos, amarnos y admirarnos. 
Desde que empecé a salir contigo, me di cuenta que íbamos a estar juntos, sabía que ya no había paso atrás y que si o si tú ibas a estar conmigo por mucho tiempo, ahora
sabemos que será por toda la vida.

Conocerte ese día fue el instante más bonito de mi vida pero amarte fue, es y será lo más hermoso que he hecho y por eso lo sigo haciendo, por eso sigo amandote cada día más y más,
demostrandote mi amor todos los días, dandote razones para seguir conmigo todos los días. 
         
Así fue como un 23 de mayo, ya habiendo planificado la fecha para estar juntos, teniendo en cuenta muchos eventos y dandome cuenta que era
una fecha bonita declarar mi amor oficialmente, decidí preparar una sorpresa: darte los tulipanes que tanto anhelabas, que tantas veces me habías dado a entender que
te gustan las flores y que los tulipanes son tus favoritos, tomé en cuenta el estreno de tu película más esperada: Lilo y Stich, compré las entradas para ir juntos, lastimosamente no pude mentirte y no me dejaste continuar con la sorpresa,
preparé un bonito detalle para que puedas tener en tu cuarto y recordarte todos los días de mi. Asi fue como decidí ir manejando hasta tu casa en pleno tráfico de la Javier Prado y la Marina,
cosa que nunca me ha detenido para ir a verte porque el tráfico jamás me frenará para verte aunque sean 10 minutos. Llegué a tu casa y no pude evitar sentir cómo se me aceleraba el corazón,
con esa sensación de que estoy dando un gran paso en mi vida, yo sabía que la respuesta era SI pero aun asi, me tenía ansioso ver tu reacción, ver cómo esos ojos lloraban lágrimas de felicidad,
ojos que no lloraban de felicidad hace un buen tiempo probablemente, ver a través de tus ojos un niña de 5 años feliz y saltando de la emoción, sin saber qué hacer más que sonreir y sonreir.
Luego te agarré pero mis palabras practicadas en el carro y en la ducha desaparecieron en ese instante, el nudo en la garganta y la felicidad del momento hizo que mi mente caiga en un abismo para olvidarse todo lo practicado aunque
después de todo lo que te había demostrado antes, lo que había hecho por ti y que no haría por nadie más, las palabras que te había, ¿era realmente necesario decirte lo mucho que te amo?. Dejé
que mis acciones hablaran: la caja y las flores eran mis palabras y luego solo pude agarrarte firmemente de la cintura y preguntarte si desearías estar conmigo por el resto de la vida.
Asi fue cómo nos hicimos enamorados, despues estuvimos felices en el carro, sonriendo y disfrutando la película. Al llegar a tu casa y hablar, nos dimos cuenta de muchas cosas y definimos el rumbo de la relación,
dejamos claro que si queremos seguir juntos por toda nuestra vida, teníamos que equilibrar todo sin dejar de amarnos tan fuerte como lo hemos hecho desde que decidimos hacerlo de verdad
Volví a mi casa convencido de que ya estaba con la 10/10, la chica perfecta, la chica divertida, alocada, preciosa, amorosa, inteligente, audaz, ingenua, persistente, destinada y caprichosa que tanto necesitaba en mi vida.
Desde que apareciste en mi vida, no hiciste otra cosa que darme más razones para despertarme, para querer verte y querer salir adelante contigo.
    
Nena, tú siempre estarás bajo mis brazos, siempre te sentirás protegida, siempre te protegeré, te apoyaré y estaré para ti, en todos los momentos.
No somos cualquier tipo de pareja, nosotros tenemos potencial para mucho más, solo debemos seguir haciendo las cosas como las hacemos ahora para lograr construir una familia con más miembros
y seguir cumpliendo nuestras metas.
         
Continúo escribiendo estas palabras ya que no pude terminar el proyecto a tiempo, que la intención era mostrartelo a las 00:40 mientras teníamos PVD
pero no pude concluirlo, estuve contigo sábado y domingo y eso me retrasó un poco pero ¿aún todavía es 23, no?

Te amo demasiado Angela, ya me tienes, ya no puedo dejar de pensar en ti, no puedo evitar preocuparme por ti, no puedo evitar querer verte todos los dias,
no puedo evitar sentir tanto por ti, no puedo evitar querer verte sonreir siempre y hacerte sentir como lo más valioso que tengo.
         

Todo mi corazón es para ti, no dejaré de amarte por nada guapa💖

*Feliz 23 mi vida, te amo demasiado y que nunca dejemos de celebrar un 23 juntos*
''')

def get_video_base64(path):
    with open(path, "rb") as video_file:
        video_bytes = video_file.read()
        encoded = base64.b64encode(video_bytes).decode()
        return encoded

video_base64 = get_video_base64("data/video_amor.mp4")

# Mostrar con tamaño personalizado
st.markdown(f"""
    <video width="800" height="450" controls>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        Tu navegador no soporta el video HTML5.
    </video>
""", unsafe_allow_html=True)



row_data = pd.read_csv('data/chat_amor.csv')
cleaned_data = pd.read_csv('data/chat_limpio.csv')

# CONTADOR DE DÍAS DE CONOCIDO

dias_conocidos = (datetime.date.today() - datetime.date(2025,1,1)).days

# CONTADOR DE DÍAS ESCRITOS

dias_escritos = row_data['Fecha'].nunique()


# CONTADOR DE NUESTRA PRIMERA CITA

dias_cita = (datetime.date.today() - datetime.date(2025,2,21)).days


# CONTADOR DE DÍAS COMO NOVIOS
dias_novios = (datetime.date.today() - datetime.date(2025,5,23)).days


st.subheader('📅¿Cuántos días...?')

col1, col2= st.columns(2, vertical_alignment= 'center')
col3,col4= st.columns(2, vertical_alignment= 'center')

with col1:
    st.metric("¿Cuántos días han transcurrido desde que te vi?", dias_conocidos)

with col2:
    st.metric("¿Cuántos días llevamos hablando?", dias_escritos)

with col3:
    st.metric("¿Cuántos días han pasado desde nuestra primera cita?", dias_cita)

with col4:
    st.metric("¿Cuántos días llevamos siendo enamorados?", dias_novios)

# GRAFICO DE PIE POR REMITENTE

st.subheader('👺¿Quien envía más mensajes?')

remitente_counts = row_data['Remitente'].value_counts().reset_index()
remitente_counts.columns = ['Remitente', 'Cantidad']
colores = ['#5881d0','#f399b5']
fig1 = px.pie(remitente_counts, names='Remitente',
             values='Cantidad',
             color_discrete_sequence=colores)

fig1.update_traces(textinfo='label+value')
fig1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo general
    plot_bgcolor='rgba(0,0,0,0)',   # Fondo del área de gráfico
)
st.plotly_chart(fig1, use_container_width=True)


st.subheader('💕¿Cuando empezamos a conectar más?')

# GRAFICO DE NUMERO DE MENSAJES POR DÍA

# Asegúrate de que la columna 'Fecha' esté en formato de fecha
row_data['Fecha'] = pd.to_datetime(row_data['Fecha'])

# Contar mensajes por día
msg_per_day = row_data['Fecha'].value_counts().reset_index()
msg_per_day.columns = ['Fecha', 'Cantidad']
msg_per_day = msg_per_day.sort_values(by='Fecha')

# Crear gráfico de línea
fig2 = px.line(msg_per_day, x='Fecha', y='Cantidad',
               markers=True,
               line_shape='spline')  # spline para curvas suaves

# Personalización del gráfico
fig2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Fecha',
    yaxis_title='Número de mensajes',
    hovermode='x unified',
    width=1000,
    height=600
)

# Mostrar gráfico en Streamlit
st.plotly_chart(fig2, use_container_width=False)

st.subheader('📉❤️¿En qué momento del día chateamos más?')

modo_grafico = st.radio(
    "Selecciona cómo deseas ver los mensajes por hora:",
    ("Detalle (hora y minuto)", "Resumen (solo horas)")
)

if modo_grafico == 'Detalle (hora y minuto)':

    # GRAFICO DE MENSAJES POR HORA

    # Convertir a datetime (si no está ya)
    row_data['Hora'] = pd.to_datetime(row_data['Hora'], format='%H:%M:%S')

    # Crear columna solo con hora y minuto
    row_data['Hora_minuto'] = row_data['Hora'].dt.strftime('%H:%M')

    # Contar mensajes por cada minuto exacto
    mensajes_por_minuto = row_data['Hora_minuto'].value_counts().reset_index()
    mensajes_por_minuto.columns = ['Hora_minuto', 'Cantidad']
    mensajes_por_minuto = mensajes_por_minuto.sort_values(by='Hora_minuto')

    fig3 = px.line(mensajes_por_minuto, x='Hora_minuto', y='Cantidad',
                  markers=False,
                  labels={'Hora_minuto': 'Hora (HH:MM)', 'Cantidad': 'Cantidad de mensajes'},
                  color_discrete_sequence=['#f399b5'])

else:


    # MENSAJES POR HORA

    row_data['Hora_num'] = pd.to_datetime(row_data['Hora'], format='%H:%M:%S').dt.hour
    mensajes_por_hora = row_data['Hora_num'].value_counts().reset_index()
    mensajes_por_hora.columns = ['Hora', 'Cantidad']
    mensajes_por_hora = mensajes_por_hora.sort_values(by='Hora')

    fig3 = px.line(mensajes_por_hora, x='Hora', y='Cantidad',
                   markers=True,
                   line_shape='spline',  # línea suavizada
                   labels={'Hora': 'Hora del día', 'Cantidad': 'Cantidad de mensajes'},
                   color_discrete_sequence=['#f399b5'])

fig3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        tickangle=90,  # ← Esto hace que el texto del eje X sea vertical
        tickmode='auto'
    ),
    hovermode='x unified'
)

st.plotly_chart(fig3, use_container_width=True)

# AMOR
# Asegúrate que la columna 'Fecha' sea tipo fecha
cleaned_data['Fecha'] = pd.to_datetime(cleaned_data['Fecha'], format='%Y-%m-%d')

# Buscar "te amo" o "t amo"
filtro_te_amo = cleaned_data['Mensaje'].str.contains(r'\b(te amo|t amo)\b', case=False, regex=True, na = False)
te_amo_count = filtro_te_amo.sum()
te_amo_fecha = cleaned_data.loc[filtro_te_amo, 'Fecha'].min()

# Buscar "amor"
filtro_amor = cleaned_data['Mensaje'].str.contains(r'\bamor\b', case=False, regex=True, na = False)
amor_count = filtro_amor.sum()
amor_fecha = cleaned_data.loc[filtro_amor, 'Fecha'].sort_values(ascending=True)
amor_fecha = amor_fecha.iloc[4]


# Buscar "te quiero"
filtro_tequiero = cleaned_data['Mensaje'].str.contains(r'\bte quiero\b', case=False, regex=True, na = False)
tequiero_count = filtro_tequiero.sum()
tequiero_fecha = cleaned_data.loc[filtro_tequiero, 'Fecha'].sort_values(ascending=True)
tequiero_fecha = tequiero_fecha.iloc[2]

st.subheader("💖 Palabras de cariño")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Veces que dijeron 'Te amo'", te_amo_count)
    st.caption(f"Primera vez: {te_amo_fecha.strftime('%d/%m/%Y')}")

with col2:
    st.metric("Veces que dijeron 'Amor'", amor_count)
    st.caption(f"Primera vez: {amor_fecha.strftime('%d/%m/%Y')}")

with col3:
    st.metric("Veces que dijeron 'Te quiero'", tequiero_count)
    st.caption(f"Primera vez: {tequiero_fecha.strftime('%d/%m/%Y')}")


st.image('data/im1.JPEG')

st.write('''
¿Tantas veces nos hemos dicho palabras amorosas? Realmente es que ya no existe día o momento del día en el cual no nos digamos lo mucho que nos amamos.
Aún no podemos olvidar las veces que se nos escapó un "Te amo" o un "Te quiero" porque nuestras almas estaban hambrientas de darnos amor aunque fuese pronto, hambrientas de demostrar todo nuestro cariño
con unas simples pero poderosas palabras.
Jamás olvidaremos esos bonitos recuerdos ni las veces en las cuales nos íbamos a nuestro querido parque a hablar y conocernos cada día más y más.

''')

st.subheader('🎧¿Qué podemos decir de la músca?')

st.write('''
Desde que empezamos a escuchar música juntos, nos dimos cuenta que teníamos gustos similares, que podíamos compartir música, cosa que
para mi siempre fue difícil porque se me hacía complicado coincidir con alguien en gusto musical pero en ti encontré mucho de lo mío y tú encontraste mucho de lo tuyo en mi.
Para mi, la música es el alma y cuando escuchamos música y la disfrutas, siento que estoy tocando tu alma, que te tengo cerca a mi y no quiero soltarte.

De paso contaremos las veces en las que hemos escuchado música juntos gracias a la Jam de Spotify.
         
''')

# Filtrar los mensajes que contienen exactamente esa frase (ignora mayúsculas)
filtro_musica = cleaned_data['Mensaje'].str.contains(
    r'elijamos y escuchemos música en conjunto en tiempo real\.',
    case=False,
    regex=True,
    na=False
)

# Contar coincidencias
musica_count = filtro_musica.sum()

# Mostrar en Streamlit
st.metric("¿Cuántas veces nos hemos tocado las almas con los oidos?", musica_count)

st.write('Voy a recordarte algunas canciones que impactaron en nosotros❤️')

col4, col5 = st.columns(2)

with col4:

    st.markdown(f"""
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/7D0RhFcb3CrfPuTJ0obrod?utm_source=generator" width="100%" height="100" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/0T5iIrXA4p5GsubkhuBIKV?utm_source=generator" width="100%" height="100" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

with col5:

    st.markdown(f"""
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3NTaEHQg5iVrRRNWlnK4RY?utm_source=generator" width="100%" height="100" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

    """, unsafe_allow_html=True)

    st.markdown(f"""
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/2eAvDnpXP5W0cVtiI0PUxV?utm_source=generator&theme=0" width="100%" height="100" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

st.write('Quizá la canción que más me pueda recordar a ti es esta porque me acuerdo la primera vez que coincidimos en escuchar Manuel Medrano, yo te había pedido "Si Pudiera" y la pusiste, luego tú pusiste "Una y Otra Vez" sin darte cuenta que sería nuestra canción.')

st.markdown("""
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/0bK3jxkbq5cDKWr68KtO8G?utm_source=generator" width="100%" height="200" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""", unsafe_allow_html=True)

st.write('Aun asi, voy a recordar la playlist que tiene un sin fin de canciones que son solamente para ti, que solo puedo acordarme de ti cada vez que lo escucho porque eres la definición del amor más bonito que existe')

st.markdown("""
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3vfx5B6pExeEgtrGvARfjy?utm_source=generator" width="100%" height="200" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""", unsafe_allow_html=True)




# WORDCLOUD

st.subheader('🤔¿Cuáles son nuestras palabras más utilizadas?')


spanish_stopwords = set([
    "de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las", "por", "un", "para", "con",
    "no", "una", "su", "al", "lo", "como", "más", "pero", "sus", "le", "ya", "o", "este", "sí",
    "porque", "esta", "entre", "cuando", "muy", "sin", "sobre", "también", "me", "hasta", "hay",
    "donde", "quien", "desde", "todo", "nos", "durante", "todos", "uno", "les", "ni", "contra",
    "otros", "ese", "eso", "ante", "ellos", "e", "esto", "mí", "antes", "algunos", "qué", "unos",
    "yo", "otro", "otras", "otra", "él", "tanto", "esa", "estos", "mucho", "quienes", "nada",
    "muchos", "cual", "poco", "ella", "estar", "estas", "algunas", "algo", "nosotros", "mi", "mis",
    "tú", "te", "ti", "tu", "tus", "ellas", "nosotras", "vosotros", "vosotras", "os", "mío", "mía",
    "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas", "suyo", "suya", "suyos", "suyas", "nuestro",
    "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras", "esos",
    "esas", "estoy", "estás", "está", "estamos", "estáis", "están", "esté", "estés", "estemos",
    "estéis", "estén", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán","xd",
    "jiji","es","si","uu ","t ","uwu"
])

# Cargar imagen de máscara (forma de corazón)
mask_image = np.array(Image.open("data/corazon.jpg"))

# Unir todos los mensajes en un solo texto
texto_todos_los_mensajes = " ".join(cleaned_data['Mensaje'].dropna().astype(str))

mask = np.array(Image.open("data/corazon.jpg").convert("L"))

# Crear WordCloud con fondo transparente y máscara
wc = WordCloud(
    background_color=None,
    mode="RGBA",
    stopwords=spanish_stopwords,
    mask=mask,
    width=800,
    height=800,
    colormap='Reds'
)

wc.generate(texto_todos_los_mensajes)

# Guardar la imagen resultante con transparencia
wc.to_file("data/wordcloud_corazon_transparente.png")

st.image("data/wordcloud_corazon_transparente.png")

st.write('''
Este corazón representa las palabras que más utilizamos al momento de charlar según el tamaño de la misma y
como vemos, si o si nos referimos a nosotros como "Amor" y nos decimos muchas veces te "amo". Tambien hay algunas palabras
como "encanta", "dormir" o "contigo". Creo que analizando este wordcloud, nos damos cuenta que somos
muy cariñosos al momento de textearnos🥰
''')




st.subheader("🥸¿Qué expresamos al hablarnoss?")

# Cargar el archivo CSV
df = pd.read_csv("data/chat_limpio_con_emociones.csv")
# Traducir sentimientos
traduccion_sentimientos = {
    "others": "otros",
    "joy": "alegría",
    "sadness": "tristeza",
    "anger": "enojo",
    "surprise": "sorpresa",
    "fear": "miedo",
    "disgust": "disgusto"
}
df["Sentimiento_es"] = df["Sentimiento"].map(traduccion_sentimientos)

# Contar frecuencias
conteo = df["Sentimiento_es"].value_counts().reset_index()
conteo.columns = ["Sentimiento", "Frecuencia"]

# Crear gráfico tipo donut con fondo transparente
fig = px.pie(
    conteo,
    names="Sentimiento",
    values="Frecuencia",
    hole=0.3,
    color_discrete_sequence=px.colors.qualitative.Set3
)

# Hacer el fondo transparente
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image('data/im2.JPEG')

with col2:
    st.subheader('¿Cómo olvidar la primera vez que salimos y le mostratamos nuestro amor a todos?')
    st.subheader('¿Cómo olvidar que volví a casa tan feliz después de haber pasado la madrugada contigo?')

# DISTANCIA

st.subheader('🗺️¿Qué tan lejos nos encontramos?')

import streamlit as st
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# Entradas de usuario para dos ubicaciones

lat1 = -12.065777
lon1 = -77.123590


lat2 = -12.064371
lon2 = -76.946829

# Calcular distancia
distancia = geodesic((lat1, lon1), (lat2, lon2)).kilometers
st.success(f"Distancia entre los puntos: {distancia:.2f} km")

# Crear mapa con folium
m = folium.Map(location=[(lat1 + lat2) / 2, (lon1 + lon2) / 2], zoom_start=6)
m.fit_bounds([[lat1, lon1], [lat2, lon2]])
# Marcadores
folium.Marker([lat1, lon1], tooltip="Ubicación 1", icon=folium.Icon(color="blue")).add_to(m)
folium.Marker([lat2, lon2], tooltip="Ubicación 2", icon=folium.Icon(color="green")).add_to(m)

# Línea entre los puntos
folium.PolyLine(locations=[[lat1, lon1], [lat2, lon2]], color="red").add_to(m)

# Mostrar mapa en Streamlit
st_folium(m, width=700, height=500)


st.subheader('Último video antes de que termines mi niña')

video_base64 = get_video_base64("data/video_2.mp4")

# Mostrar con tamaño personalizado
st.markdown(f"""
    <video width="800" height="450" controls>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        Tu navegador no soporta el video HTML5.
    </video>
""", unsafe_allow_html=True)

st.header('''
TE AMO DEMASIADO MI NIÑA PRECIOSA
       
Atte. Tu enamorado Marcello❤️
''')

st.image('data/tulipanes.png')
