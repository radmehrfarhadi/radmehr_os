import tkinter as tk

def hello():
    name = entery.get()
    label.config(text=f"Hello {name}")
window = tk.Tk()
window.title("Radmehr Os")
frame1 = tk.LabelFrame(window, text="بخش ورود اطلاعات")
frame1.pack(padx=20, pady=10, fill="both", expand=True)
frame2 = tk.LabelFrame(window, text="بخش پیام")
frame2.pack(padx=20, pady=10, fill="both", expand=True)
entery = tk.Entry(frame1)
entery.pack()
button = tk.Button(frame1, text="Hello", command=hello)
label = tk.Label(frame2, text="Waiting...")
label.pack(padx=15, pady=15, fill="both", expand=True)
button.pack()
window.mainloop()