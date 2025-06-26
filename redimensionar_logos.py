from PIL import Image
import os

PASTA_ORIGEM = r"C:\Users\WMBSuporte\Pictures\Marcas"
PASTA_DESTINO = r"C:\Users\WMBSuporte\Pictures\Logos" 

for nome_arquivo in os.listdir(PASTA_ORIGEM):
    if nome_arquivo.endswith(".png"):
        caminho_arquivo = os.path.join(PASTA_ORIGEM, nome_arquivo)
        try:
            with Image.open(caminho_arquivo) as img:
                img_redimensionada = img.resize((100, 100), Image.LANCZOS)

                destino = os.path.join(PASTA_DESTINO, nome_arquivo)
                img_redimensionada.save(destino, format="PNG")
                print(f"[✔] Redimensionado: {nome_arquivo}")
        except Exception as e:
            print(f"[×] Erro com {nome_arquivo}: {e}")
