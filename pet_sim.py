import tkinter as tk
from tkinter import ttk

from pet import Pet


class VirtualPetGame:
    def __init__(self, window):
        self.pet = None
        self.game_running = False

        self.window = window
        self.window.title("Virtual Pet Simulator")
        self.window.geometry("500x700")
        self.window.resizable(False, False)
        self.window.configure(bg="#B8D9E0")
        self.show_start_screen()

    def show_start_screen(self):
        tk.Label(self.window, font=("Arial", 25), bg="#B8D9E0", text="Welcome!!!").pack(
            pady=15
        )
        tk.Label(
            self.window, font=("Arial", 20), bg="#B8D9E0", text="Let's Adopt a New Pet!"
        ).pack(pady=15)
        tk.Label(
            self.window, font=("Arial", 20), bg="#B8D9E0", text="Enter your pet's name:"
        ).pack()

        self.name_entry = tk.Entry(self.window, font=("Arial", 20), justify="center")
        self.name_entry.insert(0, "PET NAME")
        self.name_entry.pack(pady=15)

        tk.Label(
            self.window, font=("Arial", 20), bg="#B8D9E0", text="Choose your pet type: "
        ).pack()

        self.pet_type = ttk.Combobox(
            self.window,
            values=["Dog", "Cat"],
            font=("Arial", 20),
            state="readonly",
            justify="center",
        )
        self.pet_type.current(0)
        self.pet_type.pack(pady=15)

        tk.Button(
            self.window,
            text="Start Game",
            font=("Arial", 20, "bold"),
            width=20,
            height=2,
            command=self.start_game,
        ).pack(pady=15)

    def start_game(self):
        pet_name = self.name_entry.get()
        pet_type = self.pet_type.get()

        self.pet = Pet(pet_name, pet_type)
        self.game_running = True

        self.show_game_screen()
        self.schedule_timer()

    # showgamescreen
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def update_game_screen(self):
        mood, emoji = self.pet.get_mood()
        pet_emoji = {
            "Dog": "🐶",
            "Cat": "🐱",
        }
        p_emoji = pet_emoji.get(self.pet.pet_type)
        self.mood_label.config(text=p_emoji + " " + emoji + " " + mood)
        self.mood_label.pack()

    def show_game_screen(self):
        self.clear_screen()
        tk.Label(
            self.window,
            text=f"Hello, {self.pet.name}",
            font=("Arial", 20),
            bg="#B8D9E0",
        ).pack(pady=15)

        self.mood_label = tk.Label(
            self.window,
            text="? mood",
            font=("Arial", 20),
            bg="#B8D9E0",
        )
        mood, emoji = self.pet.get_mood()
        pet_emoji = {
            "Dog": "🐶",
            "Cat": "🐱",
        }
        p_emoji = pet_emoji.get(self.pet.pet_type)
        self.mood_label.config(text=p_emoji + " " + emoji + " " + mood)

        self.mood_label.pack()

        self.bars = {}
        status_frame = tk.Frame(self.window).pack()
        status_data = [
            ("Hunger", "hunger", "#E67E22"),
            ("Happiness", "happiness", "#E84393"),
            ("Energy", "energy", "#0984E3"),
        ]

        for title, key, color in status_data:
            row = tk.Frame(status_frame)
            row.pack()
            tk.Label(
                row,
                text=title,
                font=("Arial", 15),
            ).pack(side="left")

            pbar = ttk.Progressbar(
                row, length=200, maximum=100, mode="determinate"
            ).pack(side="left")

            value_label = tk.Label(
                row, text="", font=("Arial", 12), bg="#E87345"
            ).pack()

            self.bars[key] = (pbar, value_label)

        # button_frame=tk.Frame(
        #     self.window
        # ).pack()
        # actions = [
        #     ("🍖 Feed", self.feed_pet, "#FFB347"),
        #     ("🎾 Play", self.play_with_pet, "#F78FB3"),
        #     ("💤 Sleep", self.put_pet_to_sleep, "#74B9FF")
        # ]

        # for txt, cmd, clr in actions:
        #     button = tk.Button(
        #         button_frame,
        #         ext=txt,
        #         command=cmd,
        #     ).pack()

    def game_time(self):
        if not self.game_running:
            return
        print("gameticking")
        self.timer_id = None
        self.pet.pass_time()
        print(
            f"Current Status: Hunger: {self.pet.hunger} Energy: {self.pet.energy} Happiness: {self.pet.happiness}"
        )

        self.update_game_screen()
        self.check_game_status()
        self.schedule_timer()

    def schedule_timer(self):
        if self.game_running:
            self.timer_id = self.window.after(5000, self.game_time)

    def check_game_status(self):
        if not self.pet.is_alive():
            self.game_running = False
            self.mood_label.config(text="💔 GAME OVER 💔", font=("Arial", 30, "bold"))


# =============================
# runapp
# =============================
window = tk.Tk()  # SHELL
game = VirtualPetGame(window)
window.mainloop()  # RUN
