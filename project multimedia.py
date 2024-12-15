import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video(quality):
    url = url_entry.get()
    if not url:
        messagebox.showerror("خطأ", "الرجاء إدخال رابط الفيديو")
        return

    # تحديد خيارات التنزيل بناءً على الجودة
    if quality == "high":
        ydl_opts = {'format': 'bestvideo+bestaudio/best', 'outtmpl': '%(title)s.%(ext)s'}
    elif quality == "low":
        ydl_opts = {'format': 'worstvideo+worstaudio/worst', 'outtmpl': '%(title)s.%(ext)s'}
    elif quality == "audio":
        ydl_opts = {'format': 'bestaudio', 'outtmpl': '%(title)s.%(ext)s'}
    else:
        messagebox.showerror("خطأ", "جودة غير صحيحة")
        return

    try:
        # بدء عملية التحميل
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("نجاح", "تم تحميل الفيديو بنجاح!")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ: {e}")

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("برنامج تحميل الفيديو")
root.geometry("400x200")

# إدخال الرابط
url_label = tk.Label(root, text="post link here  :", fg="red")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# أزرار التحميل
btn_high = tk.Button(root, text="تحميل بجودة عالية", bg="green", fg="white", command=lambda: download_video("high"))
btn_high.pack(pady=5)

btn_low = tk.Button(root, text="تحميل بجودة منخفضة", bg="orange", fg="white", command=lambda: download_video("low"))
btn_low.pack(pady=5)

btn_audio = tk.Button(root, text="تحميل الصوت فقط", bg="blue", fg="white", command=lambda: download_video("audio"))
btn_audio.pack(pady=5)

# تشغيل واجهة المستخدم
root.mainloop()
