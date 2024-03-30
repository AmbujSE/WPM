import tkinter as tk
import time


class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.words_per_minute = tk.StringVar()
        self.elapsed_time = tk.StringVar()

        self.typing_text = ""
        self.start_time = 0
        self.stop_time = 0

        self.create_widgets()

    def create_widgets(self):
        self.sample_label = tk.Label(self.master, text="Type the following text:")
        self.sample_label.pack()

        self.sample_textbox = tk.Text(self.master, height=5, width=50)
        self.sample_textbox.insert(tk.END, self.sample_text)
        self.sample_textbox.pack()

        self.typing_label = tk.Label(self.master, text="Start typing below:")
        self.typing_label.pack()

        self.typing_textbox = tk.Text(self.master, height=5, width=50)
        self.typing_textbox.pack()

        self.result_label = tk.Label(self.master, text="Your typing speed (words per minute): ")
        self.result_label.pack()

        self.wpm_display = tk.Label(self.master, textvariable=self.words_per_minute)
        self.wpm_display.pack()

        self.start_button = tk.Button(self.master, text="Start Test", command=self.start_test)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop Test", command=self.stop_test, state=tk.DISABLED)
        self.stop_button.pack()

    def start_test(self):
        self.typing_text = ""
        self.start_time = time.time()
        self.stop_time = 0
        self.typing_textbox.bind("<KeyRelease>", self.update_speed)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_test(self):
        self.stop_time = time.time()
        self.typing_textbox.unbind("<KeyRelease>")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_speed(self, event):
        self.typing_text = self.typing_textbox.get("1.0", tk.END)
        elapsed_time = self.stop_time - self.start_time if self.stop_time else time.time() - self.start_time
        typed_words = self.typing_text.split()
        words_per_minute = int(len(typed_words) / (elapsed_time / 60))
        self.words_per_minute.set(words_per_minute)


def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
