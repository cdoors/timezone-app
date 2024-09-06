import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

class TimezoneComparisonTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Timezone Comparison Tool")

        self.timezones = pytz.all_timezones
        self.selected_timezones = []

        # Create UI elements
        self.label = tk.Label(root, text="Select your local time zone:")
        self.label.pack(pady=10)

        self.local_timezone = ttk.Combobox(root, values=self.timezones)
        self.local_timezone.pack(pady=10)
        self.local_timezone.bind("<<ComboboxSelected>>", self.update_timezones)
        self.local_timezone.bind("<KeyRelease>", self.filter_timezones)  # Bind key release event

        self.add_button = tk.Button(root, text="Add Time Zone", command=self.add_timezone)
        self.add_button.pack(pady=10)

        self.timezone_list = tk.Listbox(root)
        self.timezone_list.pack(pady=10)

        self.timeline_frame = tk.Frame(root)
        self.timeline_frame.pack(pady=10, fill=tk.X, expand=True)

        self.update_button = tk.Button(root, text="Update Timeline", command=self.update_timeline)
        self.update_button.pack(pady=10)

        self.time_display = tk.Label(root, text="")
        self.time_display.pack(pady=10)

    def add_timezone(self):
        selected = self.local_timezone.get()
        if selected and selected not in self.selected_timezones:
            self.selected_timezones.append(selected)
            self.timezone_list.insert(tk.END, selected)
            self.update_timeline()

    def update_timezones(self, event):
        self.update_timeline()

    def filter_timezones(self, event):
        search_term = self.local_timezone.get().lower()
        filtered_timezones = [tz for tz in self.timezones if search_term in tz.lower()]
        self.local_timezone['values'] = filtered_timezones  # Update the dropdown options
        self.local_timezone.set(search_term)  # Set the current input

    def update_timeline(self):
        for widget in self.timeline_frame.winfo_children():
            widget.destroy()  # Clear previous timeline

        base_timezone = self.local_timezone.get()
        if base_timezone:
            base_time = datetime.now(pytz.timezone(base_timezone)).strftime('%H:%M')
            self.time_display.config(text=f"Current time in {base_timezone}: {base_time}")

        # Create a horizontal timeline
        timezones_to_display = [base_timezone] + self.selected_timezones
        for i, tz in enumerate(timezones_to_display):
            time = datetime.now(pytz.timezone(tz)).strftime('%H:%M')
            frame = tk.Frame(self.timeline_frame, borderwidth=1, relief="solid")
            frame.grid(row=0, column=i, padx=5, sticky="nsew")
            
            tk.Label(frame, text=tz, wraplength=100).pack(pady=5)
            tk.Label(frame, text=time, font=("Arial", 14, "bold")).pack(pady=5)

        # Configure grid to expand columns evenly
        for i in range(len(timezones_to_display)):
            self.timeline_frame.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimezoneComparisonTool(root)
    root.mainloop()