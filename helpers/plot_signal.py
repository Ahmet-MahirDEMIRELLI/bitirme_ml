import matplotlib.pyplot as plt
import librosa.display
import numpy as np

def plot_signal(signal, title):
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    librosa.display.waveshow(signal, sr=22050)
    plt.title(f"Waveform - {title}")

    plt.subplot(1, 2, 2)
    S = librosa.feature.melspectrogram(y=signal, sr=22050, n_mels=128)
    S_dB = librosa.power_to_db(S, ref=np.max)
    librosa.display.specshow(S_dB, sr=22050, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title("Mel Spectrogram")

    plt.tight_layout()
    plt.show()