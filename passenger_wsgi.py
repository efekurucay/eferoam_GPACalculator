import sys
import os

# Virtual environment'ı aktif et
INTERP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venv', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Uygulama dizinini Python path'ine ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Flask uygulamasını import et
from wsgi import application 