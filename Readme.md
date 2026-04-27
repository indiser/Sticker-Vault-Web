<div align="center">

# 🎯 Sticker Vault

### *Your Personal WhatsApp Sticker Arsenal*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
</p>

<p align="center">
  <strong>Extract • Organize • Deploy</strong>
</p>

<p align="center">
  A complete automation suite that transforms WhatsApp Web stickers into organized, importable packs with a stunning web gallery.
</p>

</div>

---

## 🌟 What is Sticker Vault?

Sticker Vault bridges the gap between **WhatsApp Web** and **custom sticker apps** with a seamless three-step workflow:

<div align="center">

```mermaid
graph LR
    A[🌐 WhatsApp Web] -->|Extract| B[⚙️ Sticker Vault]
    B -->|Process| C[📦 Organized Packs]
    C -->|Import| D[📱 WhatsApp App]
    
    style A fill:#25D366,stroke:#128C7E,color:#fff
    style B fill:#3776AB,stroke:#2C5F8D,color:#fff
    style C fill:#F7DF1E,stroke:#F0DB4F,color:#000
    style D fill:#25D366,stroke:#128C7E,color:#fff
```

</div>

<table align="center">
<tr>
<td align="center">🔍<br/><b>Extract</b><br/>Scrape stickers from WhatsApp Web</td>
<td align="center">⚡<br/><b>Process</b><br/>Deduplicate & organize automatically</td>
<td align="center">🎨<br/><b>Browse</b><br/>Beautiful web gallery with previews</td>
<td align="center">📲<br/><b>Import</b><br/>One-click WhatsApp integration</td>
</tr>
</table>

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔍 **Smart Extraction**
Browser-based scraper captures blob URLs from WhatsApp Web in real-time as you scroll through chats.

### 🛡️ **Auto Deduplication**
SHA-256 hashing eliminates duplicate stickers automatically—no manual cleanup needed.

### 📦 **WhatsApp Compliant**
Auto-chunks stickers into packs of 30 with proper manifest generation and tray icons.

</td>
<td width="50%">

### 🎨 **Beautiful Gallery**
Dark-themed Flask web app with lazy loading, smooth animations, and responsive design.

### ⬇️ **Instant Downloads**
Click any sticker to download it directly—no complicated export process.

### 🖼️ **Tray Icon Generation**
Automatically creates optimized 96×96 PNG tray icons for each pack.

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technologies |
|:-----:|:-------------|
| **Backend** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/-Tailwind-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| **Processing** | ![Pillow](https://img.shields.io/badge/-Pillow-3776AB?style=flat-square) SHA-256 Hashing |
| **Data** | ![JSON](https://img.shields.io/badge/-JSON-000000?style=flat-square&logo=json&logoColor=white) WebP Format |

</div>

---

## 📁 Project Structure

```
wp_stickers/
│
├── 🐍 Python Scripts
│   ├── app.py                    # Flask web server
│   ├── build.py                  # Deduplication & build pipeline
│   ├── generate_manifest.py      # WhatsApp manifest generator
│   └── make_trays.py             # Tray icon generator (96x96)
│
├── 🌐 Browser Scripts
│   ├── sticker_finder.js         # Scraper (run in DevTools)
│   └── sticker_downloader.js     # Batch downloader
│
├── 📄 Data Files
│   ├── contents.json             # WhatsApp sticker manifest
│   └── stickers.json             # Gallery metadata
│
├── 🎨 Web Interface
│   ├── templates/
│   │   └── index.html            # Dark-themed gallery
│   └── static/
│       └── dist/                 # Processed stickers
│
├── 📦 Sticker Packs
│   ├── 1/                        # Pack 1 (30 stickers)
│   ├── 2/                        # Pack 2 (30 stickers)
│   ├── 3/                        # Pack 3 (remaining)
│   └── tray_*.png                # Pack tray icons
│
└── 🗂️ stickers/                  # Raw extracted files
```

---

## 🚀 Quick Start

### 📋 Prerequisites

<table>
<tr>
<td>✅ Python 3.8+</td>
<td>✅ pip package manager</td>
<td>✅ Modern browser (Chrome/Edge/Firefox)</td>
</tr>
</table>

### ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/indiser/Sticker-Vault-Web.git
cd sticker-vault

# Install dependencies
pip install flask pillow
```

---

## 📖 Complete Workflow

### **Step 1️⃣: Extract Stickers from WhatsApp Web**

<table>
<tr>
<td width="30px">1.</td>
<td>Open <b>WhatsApp Web</b> in your browser</td>
</tr>
<tr>
<td>2.</td>
<td>Press <code>F12</code> to open <b>Developer Tools</b></td>
</tr>
<tr>
<td>3.</td>
<td>Navigate to the <b>Console</b> tab</td>
</tr>
<tr>
<td>4.</td>
<td>Paste and run <code>sticker_finder.js</code></td>
</tr>
<tr>
<td>5.</td>
<td>Scroll through chats to capture sticker URLs</td>
</tr>
<tr>
<td>6.</td>
<td>Run <code>sticker_downloader.js</code> to download all stickers</td>
</tr>
<tr>
<td>7.</td>
<td>Move downloaded files to the <code>stickers/</code> folder</td>
</tr>
</table>

---

### **Step 2️⃣: Build & Deduplicate**

```bash
python build.py
```

<details>
<summary>🔍 What this does</summary>

- ✅ Removes duplicate stickers using SHA-256 hashing
- ✅ Renames files to sequential format (`sticker_001.webp`)
- ✅ Stages output to `static/dist/`
- ✅ Generates `stickers.json` for the web gallery

</details>

---

### **Step 3️⃣: Generate WhatsApp Manifest**

```bash
python generate_manifest.py
```

<details>
<summary>🔍 What this does</summary>

- ✅ Creates WhatsApp-compliant `contents.json`
- ✅ Auto-chunks stickers into packs of 30
- ✅ Assigns tray icons and emoji metadata

</details>

---

### **Step 4️⃣: Generate Tray Icons**

```bash
python make_trays.py
```

<details>
<summary>🔍 What this does</summary>

- ✅ Generates 96×96 PNG tray icons
- ✅ Optimizes file size (under 50KB limit)
- ✅ Creates one icon per sticker pack

</details>

---

### **Step 5️⃣: Launch Web Gallery**

```bash
python app.py
```

<details>
<summary>🔍 What this does</summary>

- ✅ Starts Flask server at `http://localhost:5000`
- ✅ Displays all stickers with smooth animations
- ✅ Enables one-click downloads

</details>

<div align="center">

**🎉 Your sticker gallery is now live!**

</div>

---

## 📱 WhatsApp Compliance Checklist

<div align="center">

| Requirement | Status | Details |
|:------------|:------:|:--------|
| **WebP Format** | ✅ | All stickers in `.webp` format |
| **Pack Size** | ✅ | Maximum 30 stickers per pack |
| **Tray Icon** | ✅ | 96×96 PNG format |
| **Icon Size** | ✅ | Under 50KB per icon |
| **Emoji Metadata** | ✅ | At least 1 emoji per sticker |
| **Manifest Schema** | ✅ | Valid `contents.json` |

</div>

---

## 🎨 Gallery Features

<div align="center">

<table>
<tr>
<td align="center">🌙<br/><b>Dark Theme</b><br/>Slate color palette</td>
<td align="center">✨<br/><b>Animations</b><br/>Staggered fade-ins</td>
<td align="center">🖼️<br/><b>Lazy Loading</b><br/>Optimized performance</td>
<td align="center">📱<br/><b>Responsive</b><br/>Mobile-friendly grid</td>
</tr>
</table>

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

<table>
<tr>
<td>

**🐛 Found a bug?**  
Open an issue with details

</td>
<td>

**💡 Have an idea?**  
Submit a feature request

</td>
<td>

**🔧 Want to code?**  
Fork and create a PR

</td>
</tr>
</table>

### Contribution Steps

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m 'Add amazing feature'

# 4. Push to the branch
git push origin feature/amazing-feature

# 5. Open a Pull Request
```

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License**

See the [LICENSE](LICENSE) file for details

</div>

---

## 🙏 Acknowledgments

<div align="center">

Built with ❤️ using:

[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

Inspired by the **WhatsApp Sticker Platform**

</div>

---

<div align="center">

### 💫 Made with passion by [Indiser](https://github.com/indiser)

<p>
  <a href="#-sticker-vault">Back to Top ⬆️</a>
</p>

<p>
  <sub>⭐ Star this repo if you found it helpful!</sub>
</p>

<p>
  <img src="https://img.shields.io/github/stars/yourusername/sticker-vault?style=social" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/yourusername/sticker-vault?style=social" alt="GitHub forks"/>
</p>

</div>
