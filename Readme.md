<div align="center">

# 🎯 Sticker Vault

**A complete pipeline to extract, organize, and deploy WhatsApp sticker packs.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Sticker%20Pack-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://whatsapp.com)

</div>

---

## 📖 Overview

**Sticker Vault** is an end-to-end automation suite that bridges the gap between WhatsApp Web and custom sticker apps. The workflow is simple:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  WhatsApp Web   │────▶│  Sticker Vault  │────▶│   WhatsApp App  │
│  (Tap Sticker)  │     │  (Pipeline)     │     │  (Import Pack)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Tap** any sticker in WhatsApp Web → it opens in your custom app
2. **Browse** the beautiful web gallery to preview all extracted stickers
3. **Import** sticker packs directly into WhatsApp with one click

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Extraction** | Browser-based scraper captures blob URLs from WhatsApp Web in real-time |
| 🛡️ **Deduplication** | SHA-256 hashing eliminates duplicate stickers automatically |
| 📦 **Auto-Packaging** | Chunks stickers into WhatsApp-compliant packs (max 30 per pack) |
| 🎨 **Tray Icons** | Generates 96×96 PNG tray icons optimized for WhatsApp |
| 🌐 **Web Gallery** | Dark-themed Flask app with lazy loading and staggered animations |
| ⬇️ **One-Click Download** | Download individual stickers directly from the gallery |
| 📋 **Manifest Generation** | Produces `contents.json` fully compliant with WhatsApp sticker schema |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
- **Image Processing:** Pillow (PIL)
- **Data:** JSON manifests with SHA-256 deduplication
- **Automation:** Browser console scripts for scraping

---

## 📁 Project Structure

```
wp_stickers/
│
├── 📄 app.py                    # Flask web server
├── 📄 build.py                  # Deduplication & build pipeline
├── 📄 generate_manifest.py      # WhatsApp contents.json generator
├── 📄 make_trays.py             # Tray icon generator (96x96 PNG)
│
├── 📄 contents.json             # WhatsApp sticker pack manifest
│
├── 🌐 sticker_finder.js         # Browser scraper (run in DevTools)
├── 🌐 sticker_downloader.js     # Batch downloader (run in DevTools)
│
├── 🎨 templates/
│   └── index.html               # Dark-themed sticker gallery
│
├── 🖼️ static/
│   └── dist/                    # Processed stickers output
│
├── 🗂️ stickers/                 # Raw extracted .webp files
│
├── 📂 1/                        # Sticker Pack 1 (30 stickers)
├── 📂 2/                        # Sticker Pack 2 (30 stickers)
├── 📂 3/                        # Sticker Pack 3 (19 stickers)
│
└── 🖼️ tray_1.png, tray_2.png, tray_3.png   # Pack tray icons
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Modern web browser (Chrome/Edge/Firefox)
- Pillow library

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sticker-vault.git
cd sticker-vault

# Install dependencies
pip install flask pillow
```

---

## 📋 Usage Guide

### Step 1: Extract Stickers from WhatsApp Web

1. Open **WhatsApp Web** in your browser
2. Open **Developer Tools** (`F12` or `Ctrl+Shift+I`)
3. Go to the **Console** tab
4. Paste and run `sticker_finder.js`:
   ```javascript
   // This will start scraping sticker blob URLs as you scroll
   ```
5. Scroll through chats to capture stickers
6. Run `sticker_downloader.js` to batch download all captured stickers:
   ```javascript
   // Downloads all scraped stickers as raw_sticker_X.webp
   ```
7. Move downloaded files to the `stickers/` folder

### Step 2: Build & Deduplicate

```bash
python build.py
```

- Removes duplicate stickers using SHA-256 hashing
- Renames files to sequential format (`sticker_001.webp`, etc.)
- Stages output to `static/dist/`
- Generates `stickers.json` manifest for the web gallery

### Step 3: Generate WhatsApp Manifest

```bash
python generate_manifest.py
```

- Creates `contents.json` compliant with WhatsApp sticker requirements
- Auto-chunks stickers into packs of 30
- Assigns tray icons and emoji metadata

### Step 4: Generate Tray Icons

```bash
python make_trays.py
```

- Generates 96×96 PNG tray icons from selected stickers
- Optimized file size (under 50KB limit)

### Step 5: Launch Web Gallery

```bash
python app.py
```

- Opens `http://localhost:5000`
- Browse all stickers with smooth animations
- Click any sticker to download it instantly

---

## 📱 WhatsApp Compliance

This project adheres to **WhatsApp Sticker Requirements**:

| Requirement | Status |
|-------------|--------|
| WebP format | ✅ |
| Max 30 stickers per pack | ✅ |
| 96×96 tray icon (PNG) | ✅ |
| Tray icon < 50KB | ✅ |
| At least 1 emoji per sticker | ✅ |
| `contents.json` schema | ✅ |

---

## 🎨 Gallery Preview

The web interface features:

- 🌙 **Dark theme** with slate color palette
- ✨ **Staggered fade-in animations**
- 🖼️ **Lazy loading** for performance
- 📱 **Fully responsive** grid layout
- ⚡ **Hover effects** with scale transitions

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) and [Tailwind CSS](https://tailwindcss.com/)
- Inspired by the WhatsApp Sticker Platform

---

<div align="center">

**Made with ❤️ by [Indiser](https://github.com/yourusername)**

⭐ Star this repo if you found it helpful!

</div>

