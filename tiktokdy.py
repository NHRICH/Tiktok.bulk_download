import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import yt_dlp
import os

def download_videos(username, output_dir):
    url = f'https://www.tiktok.com/@{username}'
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title).80s.%(ext)s'),
        'quiet': False,
        'noplaylist': True,
        'format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"\nDownloading videos from: {url}")
            ydl.download([url])
            messagebox.showinfo("Download Complete", f"All videos from @{username} have been downloaded.")
        except Exception as e:
            print(f"❌ Failed to download videos from {url} - {str(e)}")
            messagebox.showerror("Download Failed", f"An error occurred: {str(e)}")

def start_download():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Input Error", "Please enter a TikTok username.")
        return

    output_dir = filedialog.askdirectory(title="Choose Download Folder")
    if not output_dir:
        return

    threading.Thread(target=download_videos, args=(username, output_dir)).start()

# UI Setup
root = tk.Tk()
root.title("TikTok Account Video Downloader")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Enter TikTok Username:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

download_button = tk.Button(root, text="Download All Videos", command=start_download, bg="green", fg="white", font=("Arial", 12))
download_button.pack(pady=20)

root.mainloop()
