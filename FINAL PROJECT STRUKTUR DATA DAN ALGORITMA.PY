class TreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, prediction=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.prediction = prediction

    def is_leaf(self):
        return self.prediction is not None

def build_manual_tree():
    cerah = TreeNode(prediction="Cerah")
    cerah_berawan = TreeNode(prediction="Cerah Berawan")
    berawan = TreeNode(prediction="Berawan")
    hujan = TreeNode(prediction="Hujan")

    root = TreeNode(
        feature="Suhu", threshold=24,
        left=hujan,
        right=TreeNode(
            feature="Suhu", threshold=26,
            left=TreeNode(
                feature="Kelembaban", threshold=75,
                left=TreeNode(
                    feature="Kecepatan Angin", threshold=21.6,
                    left=berawan,
                    right=hujan
                ),
                right=hujan
            ),
            right=TreeNode(  # Suhu > 26
                feature="Suhu", threshold=28,
                left=TreeNode(
                    feature="Kelembaban", threshold=75,
                    left=TreeNode(
                        feature="Kecepatan Angin", threshold=10.8,
                        left=cerah_berawan,
                        right=hujan
                    ),
                    right=hujan
                ),
                right=TreeNode(  # Suhu ≥ 28
                    feature="Kelembaban", threshold=65,
                    left=TreeNode(
                        feature="Kecepatan Angin", threshold=5.4,
                        left=cerah,
                        right=cerah_berawan
                    ),
                    right=cerah_berawan
                )
            )
        )
    )
    return root

def prediksi_tree(node, suhu, kelembaban, angin):
    while not node.is_leaf():
        value = {
            "Suhu": suhu,
            "Kelembaban": kelembaban,
            "Kecepatan Angin": angin
        }[node.feature]
        node = node.left if value <= node.threshold else node.right
    return node.prediction

def saran_payung(cuaca):
    if cuaca == "Hujan":
        return "☔ WAJIB membawa payung"
    elif cuaca == "Cerah":
        return "🌤️ Disarankan membawa payung"
    elif cuaca == "Berawan":
        return "☁️ Disarankan membawa payung"
    else:
        return "☁️ Boleh tidak membawa payung"

try:
    suhu = float(input("Masukkan suhu (°C): "))
    kelembaban = float(input("Masukkan kelembaban (%): "))
    angin = float(input("Masukkan kecepatan angin (km/jam): "))

    root = build_manual_tree()
    prediksi = prediksi_tree(root, suhu, kelembaban, angin)
    rekomendasi = saran_payung(prediksi)

    print("\n📊 HASIL PREDIKSI CUACA")
    print(f"• Suhu: {suhu}°C")
    print(f"• Kelembaban: {kelembaban}%")
    print(f"• Kecepatan Angin: {angin} km/jam")
    print(f"• Prediksi Cuaca: {prediksi}")
    print(f"• Rekomendasi: {rekomendasi}")

except ValueError:
    print("❌ Masukan tidak valid. Harap masukkan angka.")