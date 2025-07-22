import os
import numpy as np
import warnings
import matplotlib.pyplot as plt
from PIL import Image
import librosa, librosa.display
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn.functional as F

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def save_as_png_spectrogram(S, sr, hop_length, save_path):
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.close()

def prepare_data_from_pngs(target_dir, img_size=(128, 128), batch_size=32):
    X = []
    y = []
    for genre in sorted(os.listdir(target_dir)):
        genre_path = os.path.join(target_dir, genre)
        if not os.path.isdir(genre_path):
            continue
        for file_name in os.listdir(genre_path):
            if file_name.endswith(".png"):
                file_path = os.path.join(genre_path, file_name)
                try:
                    img = Image.open(file_path).convert("RGB")
                    img = img.resize(img_size)
                    img_array = np.array(img) / 255.0  # normalize 0-1
                    X.append(img_array.transpose((2, 0, 1)))  # PyTorch: C x H x W
                    y.append(genre)
                except Exception as e:
                    print(f"Hata: {file_path}")
                    print(e)
                    continue

    X = torch.tensor(X, dtype=torch.float32)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    y = torch.tensor(y_encoded, dtype=torch.long)

    dataset = TensorDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    return dataloader, label_encoder

def load_spectrogram(base_dir="Data/genres_original", target_dir="processed_data/spectrogram", img_size=(128, 128), batch_size=32):
    if os.path.exists(target_dir):
        return prepare_data_from_pngs(target_dir, img_size, batch_size)

    for genre in sorted(os.listdir(base_dir)):
        genre_path = os.path.join(base_dir, genre)
        if not os.path.isdir(genre_path):
            continue

        genre_output_dir = os.path.join(target_dir, genre)
        os.makedirs(genre_output_dir, exist_ok=True)

        for file_name in os.listdir(genre_path):
            if file_name.endswith(".wav"):
                file_path = os.path.join(genre_path, file_name)
                try:
                    x, sr = librosa.load(file_path, sr=None)
                    hop_length = 512
                    n_fft = 2048
                    X = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)
                    S = librosa.amplitude_to_db(np.abs(X))

                    save_path = os.path.join(genre_output_dir, file_name.replace('.wav', '.png'))
                    save_as_png_spectrogram(S, sr, hop_length, save_path)

                except Exception as e:
                    print(f"Hata: {file_path}")
                    print(e)
                    continue

    return prepare_data_from_pngs(target_dir, img_size, batch_size)
