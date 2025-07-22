import os
import librosa
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning) # FutureWarning: librosa.core.audio.__audioread_load Deprecated as of librosa version 0.10.0. It will be removed in librosa version 1.0.
warnings.filterwarnings("ignore", category=UserWarning) # PySoundFile failed. Trying audioread instead.

def load_wav_data(base_dir="Data/genres_original", sr=22050, duration=None):
    X = []
    y = []

    for genre in sorted(os.listdir(base_dir)):
        genre_path = os.path.join(base_dir, genre)
        if not os.path.isdir(genre_path):
            continue

        for file_name in os.listdir(genre_path):
            if file_name.endswith(".wav"):
                file_path = os.path.join(genre_path, file_name)
                try:
                    signal, _ = librosa.load(file_path, sr=sr, duration=duration)
                    if duration is not None:
                        expected_length = int(sr * duration)
                        if len(signal) < expected_length:
                            signal = np.pad(signal, (0, expected_length - len(signal)))
                        elif len(signal) > expected_length:
                            signal = signal[:expected_length]

                    X.append(signal)
                    y.append(genre)
                except Exception as e:
                    print(f"Dosya yüklenirken hata oluştu: {file_path}")
                    continue

    return X, y
