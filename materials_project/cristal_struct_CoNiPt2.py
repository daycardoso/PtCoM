import os
import json
from ase.io import write
from dotenv import load_dotenv
from mp_api.client import MPRester

load_dotenv()

# Sua chave de API do Materials Project
API_KEY = os.getenv('MP_KEY')
# ID do material que você quer baixar
MATERIAL_ID = "mp-1226004"

# Conecta à API e busca os dados do material
with MPRester(api_key=API_KEY) as mpr:
    # mpr.materials.search retorna uma lista de documentos do material
    data = mpr.materials.search(material_ids=[MATERIAL_ID])

# --- Salvando em .traj (para uso em simulações) ---
# Extrai o objeto de estrutura do primeiro resultado
structure_object = data[0].structure
# # Salva a estrutura no formato .traj
# write(f'{MATERIAL_ID}.traj', structure_object)
# print(f"Estrutura salva com sucesso como '{MATERIAL_ID}.traj'!")


# # --- Salvando em .json (para visualização dos dados) ---
# # Pega o documento completo do material (que contém a estrutura e todas as outras propriedades)
# material_doc = data[0]

# # O objeto 'material_doc' tem um método para exportar para JSON diretamente.
# # Usamos indent=4 para formatar o arquivo de forma legível.
# json_output = material_doc.model_dump_json(indent=4)

# # Salva a string JSON em um arquivo de texto
# with open(f'{MATERIAL_ID}.json', 'w', encoding='utf-8') as f:
#     f.write(json_output)

# print(f"Todos os dados foram salvos com sucesso como '{MATERIAL_ID}.json'!")

# from mp_api.client import MPRester
# from ase.io import write

# # Sua chave de API do Materials Project
# API_KEY = MP_KEY 
# # ID do material que você quer baixar
# MATERIAL_ID = "mp-1226004"

# # Conecta à API e busca os dados do material
# with MPRester(api_key=API_KEY) as mpr:
#     # mpr.materials.search retorna uma lista de documentos do material
#     data = mpr.materials.search(material_ids=[MATERIAL_ID])

# # 1. Extrai o objeto de estrutura do primeiro resultado da busca
# #    O objeto é do tipo Pymatgen Structure
# structure_object = data[0].structure

# # 2. Usa a função 'write' do ASE para salvar o objeto
# #    A função detecta o formato pelo nome do arquivo (.traj)
# #    e converte o objeto Pymatgen para um objeto ASE Atoms automaticamente.
# write(f'{MATERIAL_ID}.traj', structure_object)

# print(f"Estrutura do material {MATERIAL_ID} salva com sucesso como '{MATERIAL_ID}.traj'!")
