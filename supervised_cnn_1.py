from helpers.get_user_choice import get_user_choice
from helpers.load_wav_data import load_wav_data
from helpers.plot_signal import plot_signal

def train_model():
    model = None
    print(".wav verisi yükleniyor...")
    X, y = load_wav_data(sr=22050)
    print(f"{len(X)} adet ses dosyası okundu")
    
    for i in range(0,3):
        plot_signal(X[i], y[i])
    
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
    main()
