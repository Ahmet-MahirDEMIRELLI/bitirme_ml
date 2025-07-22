import os

"""
models_dir: Model dosyalarının bulunduğu klasör yolu
prefix: Listelenecek dosyaların başlangıç metni
"""
def get_model_list(prefix, models_dir="models"):

    if not os.path.exists(models_dir):
        return []

    files = os.listdir(models_dir)
    filtered_models = [f for f in files if f.startswith(prefix)]
    return filtered_models