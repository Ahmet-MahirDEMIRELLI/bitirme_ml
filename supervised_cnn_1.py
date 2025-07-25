from helpers.get_user_choice import get_user_choice
from helpers.load_wav_data_as_png import load_spectrogram, load_mel_spectrogram
from helpers.plot_signal import plot_signal
import torch

def train_model():
    model = None
    print(".wav verisi png olarak yükleniyor...")
    # dataloader, label_encoder = load_spectrogram()
    dataloader, label_encoder = load_mel_spectrogram()
    
    # Kodunu buraya ekle
    print("Model eğitiliyor...")
    
    return model

def load_model(model_name):
    model = None
    print(f"{model_name} modeli yükleniyor.")
    
    # Kodunu buraya ekle
    
    return model

def main():
    user_choice = get_user_choice("Supervised CNN Model 1", "supervised_cnn_1")
    if user_choice == "1":
        print("\n------------------------------------------------------")
        model = train_model()
    elif user_choice == "exit":
        return
    elif user_choice == "No model found":
        print("Yüklenecek model bulunamadı")
        return
    else:
        print("\n------------------------------------------------------")
        model = load_model(user_choice)
        

if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"device: {device}")
    main()
