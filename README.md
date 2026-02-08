# 🚀 Video Downloader (Python + yt-dlp + FFmpeg)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-0078D4?style=for-the-badge&logo=ffmpeg&logoColor=white)

Um script poderoso e simples para baixar vídeos do YouTube (e outros sites) na qualidade máxima disponível, incluindo **4K**, utilizando o **yt-dlp** e o **FFmpeg** para processamento de mídia.

> [!IMPORTANT]
> Este projeto requer o **FFmpeg** instalado no sistema para unir os fluxos de áudio e vídeo em alta definição. Sem ele, o download será limitado a qualidades inferiores (360p/480p).

---

## 🛠️ Tecnologias Utilizadas

*   **[Python](https://www.python.org/)** - Linguagem de programação robusta e versátil.
*   **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Um fork do youtube-dl com novos recursos e correções.
*   **[FFmpeg](https://ffmpeg.org/)** - Solução completa para gravação, conversão e streaming de áudio e vídeo.

---

## 📦 Instalação e Configuração

### Pré-requisitos
*   [Python 3.x](https://www.python.org/downloads/)
*   [FFmpeg](https://ffmpeg.org/download.html) (Instalável via `winget install ffmpeg`)

### Passo a passo

1. **Clone este repositório (ou crie a pasta):**
   ```bash
   # Se estiver usando Git
   git clone <link-do-seu-repositorio>
   ```

2. **Crie e ative seu ambiente virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Rodar

Basta executar o arquivo principal e colar a URL do vídeo quando solicitado:

```powershell
python main.py
```

O vídeo será salvo automaticamente na pasta `downloads/` com a melhor qualidade disponível e áudio compatível com Windows (AAC/M4A).

---

## ✨ Funcionalidades

- ✅ **Qualidade Máxima**: Suporte total a vídeos em 1080p, 2K e 4K.
- ✅ **Auto-Pasta**: Cria automaticamente o diretório `downloads/` se ele não existir.
- ✅ **Tratamento de Erros**: Mensagens claras caso o link seja inválido ou ocorra erro de conexão.
- ✅ **Compatibilidade**: Áudio convertido automaticamente para formatos suportados pelo Windows.

---

## 👤 Autor

Desenvolvido por **[Thaiz](https://github.com/otavio-vinii)** (Baseado no template de Otávio Vinícius).
