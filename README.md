<<<<<<< HEAD
# 🌾 AgriAI CLI — Asisten Pertanian Cerdas

Aplikasi command-line berbasis AI untuk membantu petani Indonesia mendapatkan informasi pertanian yang akurat dan praktis. Ditenagai oleh Claude AI dari Anthropic.

## ✨ Fitur

- 💬 Chat interaktif tentang topik pertanian
- 🌱 Panduan budidaya tanaman pangan & hortikultura
- 🐛 Identifikasi dan penanganan hama & penyakit
- 💧 Manajemen irigasi dan kebutuhan air
- 🧪 Rekomendasi pemupukan
- ♻️ Pertanian organik dan berkelanjutan
- 📦 Tips pasca panen dan pemasaran
- 🔄 Multi-sesi percakapan

## 🚀 Cara Instalasi

### 1. Clone repository

```bash
git clone https://github.com/username/agri-ai-cli.git
cd agri-ai-cli
```

### 2. Buat virtual environment (disarankan)

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi API Key

```bash
cp .env.example .env
```

Edit file `.env` dan isi dengan API key kamu:
```
ANTHROPIC_API_KEY=your-api-key-here
```

> Dapatkan API key gratis di: https://console.anthropic.com

### 5. Jalankan aplikasi

```bash
python main.py
```

## 🖥️ Contoh Penggunaan

```
╔══════════════════════════════════════════╗
║         🌾  AgriAI CLI  🌾              ║
║   Asisten Pertanian Cerdas Indonesia    ║
╚══════════════════════════════════════════╝

🧑‍🌾 Kamu: Tanaman padi saya daunnya menguning, kenapa?

🌾 AgriAI: Daun padi menguning bisa disebabkan beberapa hal...
```

### Perintah Tersedia

| Perintah | Fungsi |
|----------|--------|
| `baru` / `new` | Reset percakapan baru |
| `bantuan` / `help` | Tampilkan menu bantuan |
| `keluar` / `exit` | Keluar dari program |

## 🛠️ Tech Stack

- **Python 3.8+**
- **Anthropic SDK** — koneksi ke Claude AI
- **Rich** — tampilan CLI yang cantik
- **python-dotenv** — manajemen environment variable

## 📁 Struktur Proyek

```
agri-ai-cli/
├── main.py           # Program utama
├── requirements.txt  # Dependencies
├── .env.example      # Contoh konfigurasi
├── .env              # API key (tidak di-commit)
├── .gitignore        # File yang diabaikan git
└── README.md         # Dokumentasi ini
```

## 🤝 Kontribusi

Pull request sangat diterima! Untuk perubahan besar, buka issue terlebih dahulu.

## 📄 Lisensi

MIT License — bebas digunakan dan dimodifikasi.
=======
# agri-ai
>>>>>>> b287de65d4d58d683ddd17e642d6a87a837ed7eb
