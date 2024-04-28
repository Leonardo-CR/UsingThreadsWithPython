import os
import urllib.request
import concurrent.futures
import time

# Lista de URLs de las imágenes que deseas descargar
urls = [
    'https://th.bing.com/th/id/R.6e8a0316a362a93d97a2065202d17768?rik=%2bwGx4Y1i8Lypig&riu=http%3a%2f%2fwww.pngall.com%2fwp-content%2fuploads%2f2%2f1-Number-PNG-Picture.png&ehk=nn6eAThb0kLLODJQl1Ve%2bbtbv5B4A3aU7%2faR55WIPK8%3d&risl=&pid=ImgRaw&r=0',
    'https://2.bp.blogspot.com/-5D1qp2sW73c/WaBjkQ1f6gI/AAAAAAAABT4/6yN-5Ft_3dU1mLlPGOXAmddqmJxgCfhTgCKgBGAs/s1600/sistemas%2Brelatividade%2Bsimples%2BP%2Bcoord.png',
    'https://i0.wp.com/www.cursosdenumerologia.es/wp-content/uploads/2017/02/n%C3%BAmero-3-azul.jpg?ssl=1',
    'https://th.bing.com/th/id/OIP.XZ93IYOenbSrbe-rTg0SEwAAAA?w=173&h=176&c=7&r=0&o=5&pid=1.7',
    'https://i1.wp.com/www.cursosdenumerologia.es/wp-content/uploads/2017/02/n%C3%BAmero-5-azul.jpg?ssl=1',
    'https://th.bing.com/th/id/OIP.3gwy_ir4QflWlUtrM6-nrwHaJl?rs=1&pid=ImgDetMain',
    'https://th.bing.com/th/id/R.46a0f095ea7e3c021faec7a1fccc6c81?rik=QJGZs8rE14Fzhw&riu=http%3a%2f%2f2.bp.blogspot.com%2f-qaS6LRE9pnI%2fSluC2I2ngZI%2fAAAAAAAAGd4%2fItW6HRvA2HE%2fw382-h595-no%2fDigitalizar0005.jpg&ehk=WDlm5o93TyC9uwvs%2f5Vboiqxm9ZKj6kt4wh%2bc8XhySQ%3d&risl=&pid=ImgRaw&r=0',
    'https://i0.wp.com/www.orientacionandujar.es/wp-content/uploads/2017/11/8F.png?resize=366%2C500&ssl=1',
    'https://freepngimg.com/thumb/software/26765-5-software-photos-thumb.png',
    'https://th.bing.com/th/id/R.518fd504ceaf59ace32d1aa861fc2826?rik=cRwC4ZXGPbSouQ&riu=http%3a%2f%2fwww.eoi.es%2fblogs%2fmintecon%2ffiles%2f2013%2f12%2fProyecto.jpg&ehk=pOXaSlhwQdidkI3972oVf71A2dnaDbnQ37LpS4vVa1c%3d&risl=&pid=ImgRaw&r=0',
    'https://th.bing.com/th/id/R.81f8134b86eab74ef3299db1089d508e?rik=qn5eN%2fvAf5714g&riu=http%3a%2f%2flignux.com%2fwp-content%2fuploads%2f2014%2f08%2fdistros_linux.jpg&ehk=siHR8zMfowrGpJ1W6e3LlwFGXb4Pi8yw5Vy64Xe8mwY%3d&risl=&pid=ImgRaw&r=0',
    'https://www.pngall.com/wp-content/uploads/2016/07/Networking-Free-Download-PNG.png',
    'https://upload.wikimedia.org/wikipedia/commons/8/83/Solar_system.jpg',
    'https://th.bing.com/th/id/R.09da41ee73a5df23ff3bd4cf218e00d2?rik=fw7WM7dfefhsXg&riu=http%3a%2f%2fjmoral.es%2fassets%2fimg%2fmarketing%2fmarketing.png&ehk=ab%2fw3%2fhii%2fVs5pxhmZZ55nKTYU5H66fb7WEJEcFEWHg%3d&risl=&pid=ImgRaw&r=0',
    'https://www.cde.ual.es/wp-content/uploads/2020/09/Clases-de-microprocesadores-Clasificaciones-y-concepto.jpg',
    'https://bibliotecadeinvestigaciones.files.wordpress.com/2011/02/sistemas-y-aparatos.jpg',
    'https://lh5.googleusercontent.com/proxy/UfSbcE5WMVGWJFeSzcAITkvlolaBmllnBbJXswebrLHIswbN2HAJWsWPmrOBJEF1mTMhZKHzag7zglAlTIGjjOBJSb7Z7hz4r7dVbDGVSw=w1200-h630-p-k-no-nu',
    'https://th.bing.com/th/id/OIP.Cia89nljwhrtA1gtgLWIEQAAAA?rs=1&pid=ImgDetMain',
    'https://pressbooks.online.ucf.edu/app/uploads/sites/372/2021/04/CNX_UPhysics_20_01_System.jpg',
    'https://dimpapp.gr/wp-content/uploads/2016/04/mac_linux_windows-768x404.jpg'
    # Añade más URLs si es necesario
]

# Ruta de la carpeta donde deseas guardar las imágenes
carpeta = 'Threads/imagenesHilos'  # Cambia '/ruta/a/la/carpeta' por la ruta real
tiempoInicial = time.time()
# Crea la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

def descargar_imagen(url, index):
    archivo = os.path.join(carpeta, f'imagen_descargada_{index}.jpg')  # Nombre de archivo con ruta completa
    try:
        urllib.request.urlretrieve(url, archivo)
        return f"La imagen {index} ha sido descargada con éxito."
    except Exception as e:
        return f"No se pudo descargar la imagen {index}: {e}"

# Descarga las imágenes en paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    resultados = [executor.submit(descargar_imagen, url, index + 1) for index, url in enumerate(urls)]

# Imprime los resultados
for resultado in concurrent.futures.as_completed(resultados):
    print(resultado.result())

tiempoFinal = time.time()
TT = tiempoFinal - tiempoInicial
print(TT)#Me dio 1.93 segundos