import yt_dlp
import os

def download_video():
    url = input("Cole o link do vídeo: ")
    
    # Garantir que a pasta de downloads existe
    download_path = "downloads"
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print(f"Pasta '{download_path}' criada!")

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": f"{download_path}/%(title)s.%(ext)s",
        "merge_output_format": "mp4"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Iniciando download...")
            ydl.download([url])
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    download_video()
