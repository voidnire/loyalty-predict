import os
import shutil
import kagglehub

# 1. Definir o identificador do dataset e a pasta de destino
dataset_handle = "teocalvo/teomewhy-education-platform"
dest_folder = "/workspaces/loyalty-predict/data"

# Garantir que a pasta de destino existe
os.makedirs(dest_folder, exist_ok=True)

# 2. Descarregar o dataset através do kagglehub
print(f"A descarregar {dataset_handle}...")
downloaded_path = kagglehub.dataset_download(dataset_handle)
print(f"Descarregado temporariamente em: {downloaded_path}")

# 3. Copiar todos os ficheiros para a pasta de destino
for item in os.listdir(downloaded_path):
    source_item = os.path.join(downloaded_path, item)
    dest_item = os.path.join(dest_folder, item)
    
    if os.path.isdir(source_item):
        shutil.copytree(source_item, dest_item, dirs_exist_ok=True)
    else:
        shutil.copy2(source_item, dest_item)

print(f"\nFicheiros copiados com sucesso para: {dest_folder}")
print("Conteúdo da pasta:", os.listdir(dest_folder))