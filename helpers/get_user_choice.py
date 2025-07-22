from .get_model_list import get_model_list

"""
model_type: Örnek: Supervised CNN Model 1
model_prefix: Örnek supervised_cnn_1
returns
1 -> Yeniden eğitim
No model found -> Model yok durumu
exit -> işlem iptali
dosya adı -> olan modeli yükleme
"""
def get_user_choice(model_type, model_prefix):
    print(f"\n**************** {model_type} ****************\n")
    while True:
        print("------------------------------------------------------")
        print("Modeli yeniden eğitmek için --> 1\nHazır modellerden seçmek için --> 2")
        choice = input("Seçiminiz (1 veya 2): ").strip()
        
        if choice == "1":
            return "1"
        elif choice == "2":
            print("\n------------------------------------------------------")
            supervised_models = get_model_list(prefix=model_prefix)
            if not supervised_models:
                return "No model found"
            
            while True:
                for idx, model_name in enumerate(supervised_models, start=1):
                    print(f"{idx}. {model_name}")
                choice = input("Yüklenecek modelin numarasını giriniz (iptal için q): ").strip()
                if choice.lower() == "q":
                    return "exit"
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(supervised_models):
                        return supervised_models[idx]
                    else:
                        print("\nGeçersiz numara. Tekrar deneyin.")
                else:
                    print("Lütfen sayı giriniz veya 'q' ile çıkış yapınız.")
        else:
            print("Geçersiz seçim! Lütfen 1 veya 2 giriniz.")