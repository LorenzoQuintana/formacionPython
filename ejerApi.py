import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def check_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"La página {url} se ha encontrado.")
        else:
            print(f"La página {url} No se ha encontrado.")
    except requests.RequestException as e:
        print(f"Error: {e}")

def get_robots(domain):
    url = f"{domain}/robots.txt"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            with open("robots.txt", "w", encoding="utf-8") as file:
                file.write(response.text)
            print("El archivo robots.txt se ha guardado.")
        else:
            print(f"El archivo robots.txt no se ha podido guardar.")
    except requests.RequestException as e:
        print(f"Error: {e}")

def extract_h1_tag(url):
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        h1_tag = soup.find('h1')
        if h1_tag:
            print(h1_tag.text.strip())
        else:
            print("No se encontró etiqueta h1.")
    except requests.RequestException as e:
        print(f"Error: {e}")

def extract_headers(url):
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = {}
        for i in range(1, 7):
            headers[f'h{i}'] = [tag.text.strip() for tag in soup.find_all(f'h{i}')]
        
        for header, values in headers.items():
            for value in values:
                print(f"{header}: {value}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def extract_images(url):
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_links = [img['src'] for img in soup.find_all('img', src=True)]

        for idx, link in enumerate(image_links, start=1):
            print(f"{idx}. {link}")
    except requests.RequestException as e:
        print(f"Error: {e}")



def main():
    print("\n")
    print("=" * 50)
    print("1. Comprobar si una página esta en el servidor")
    print("=" * 50)
    check_page("https://example.com")

    print("\n" + "=" * 50)
    print("2. Descargar el contenido de robots.txt")
    print("=" * 50)
    get_robots("https://en.wikipedia.org")

    print("\n" + "=" * 50)
    print("3. Extraer la etiqueta h1")
    print("=" * 50)
    extract_h1_tag("https://example.com")

    print("\n" + "=" * 50)
    print("4. Extraer todas las etiquetas de encabezado")
    print("=" * 50)
    extract_headers("https://en.wikipedia.org/wiki/Main_Page")

    print("\n" + "=" * 50)
    print("5. Extraer todos los enlaces de imágenes")
    print("=" * 50)
    extract_images("https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)")
    print("\n")

if __name__ == "__main__":
    main()