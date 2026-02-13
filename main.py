import yt_dlp
import os

def download_video():
    url = input("Cole o link do vídeo: ").strip()
    if not url: return

    # Pasta de downloads
    path = "downloads"
    if not os.path.exists(path): os.makedirs(path)

    # Opções de download (MP4 alta qualidade)
    opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": f"{path}/%(title)s.%(ext)s",
        "merge_output_format": "mp4"
    }

    try:
        print("Baixando...")
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("✅ Concluído!")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    download_video()


