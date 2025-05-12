import subprocess
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

# Nomes dos serviços (confira no seu PC)
POSTGRES_SERVICE = "postgresql-x64-17"
MYSQL_SERVICE = "MySQL93"

# Criação de ícone básico (círculo preto)
def create_image():
    image = Image.new('RGB', (64, 64), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.ellipse((16, 16, 48, 48), fill=(0, 0, 0))
    return image

# Funções de controle
def start_service(service):
    subprocess.run(["sc", "start", service], shell=True)

def stop_service(service):
    subprocess.run(["sc", "stop", service], shell=True)

# Função principal
def setup_tray():
    icon = Icon("Service Manager")

    # Menu do ícone
    icon.menu = Menu(
        MenuItem("Iniciar PostgreSQL", lambda: threading.Thread(target=start_service, args=(POSTGRES_SERVICE,)).start()),
        MenuItem("Parar PostgreSQL", lambda: threading.Thread(target=stop_service, args=(POSTGRES_SERVICE,)).start()),
        MenuItem("Iniciar MySQL", lambda: threading.Thread(target=start_service, args=(MYSQL_SERVICE,)).start()),
        MenuItem("Parar MySQL", lambda: threading.Thread(target=stop_service, args=(MYSQL_SERVICE,)).start()),
        MenuItem("Sair", lambda icon: icon.stop())
    )

    icon.icon = create_image()
    icon.run()

# Rodar
setup_tray()
