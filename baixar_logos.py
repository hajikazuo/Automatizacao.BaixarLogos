import requests
import re

brands_resp = requests.get("https://fipe.parallelum.com.br/api/v2/trucks/brands")
brands_resp.raise_for_status()
brands = brands_resp.json()  

def normalizar_nome(nome):
    nome = nome.lower()
    nome = re.sub(r"[àáâãäå]", "a", nome)
    nome = re.sub(r"[èéêë]", "e", nome)
    nome = re.sub(r"[ìíîï]", "i", nome)
    nome = re.sub(r"[òóôõö]", "o", nome)
    nome = re.sub(r"[ùúûü]", "u", nome)
    nome = re.sub(r"[ç]", "c", nome)
    nome = re.sub(r"[^a-z0-9]", "", nome)
    return nome

base_url = "https://api.puxaplaca.app/logo/{}.png"

for marca in brands:
    nome_normalizado = normalizar_nome(marca["name"])
    url = base_url.format(nome_normalizado)

    try:
        r = requests.get(url, verify=False)
        if r.status_code == 200 and r.headers.get('Content-Type', '').startswith('image'):
            with open(f"{nome_normalizado}.png", "wb") as f:
                f.write(r.content)
            print(f"[✔] {marca['name']} → {nome_normalizado}.png")
        else:
            print(f"[×] {marca['name']} — logo não encontrada ({r.status_code})")
    except Exception as e:
        print(f"[ERRO] {marca['name']} — {e}")