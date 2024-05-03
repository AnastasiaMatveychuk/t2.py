import tkinter as tk

def toggle_visibility():
    current_state = col_frame.winfo_ismapped()
    col_frame.grid_forget() if current_state else col_frame.grid(row=0, column=0, padx=10, pady=10)

def on_button_click():
    # Получаем текст из Entry и выводим его на консоль
    input_text = input_field.get()
    print(f"Text from Entry: {input_text}")

# Create the main window
window = tk.Tk()
window.title("Window Title")

# Create widgets
label = tk.Label(window, text="My Window")
input_field = tk.Entry(window)
button = tk.Button(window, text="My button", command=on_button_click)
invisible_button = tk.Button(window, text="Invisible", command=toggle_visibility)
visible_button = tk.Button(window, text="Visible", command=toggle_visibility)
exit_button = tk.Button(window, text="Exit", command=window.destroy)

# Create a frame for the column elements
col_frame = tk.Frame(window)

# Arrange widgets in the column frame
label.grid(row=0, column=0, sticky="w")
input_field.grid(row=0, column=1)
button.grid(row=0, column=2)
col_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")
col_frame.grid_propagate(False)  # Disable automatic resizing of the frame

# Add elements to the column frame
col_frame_label = tk.Label(col_frame, text="Additional Elements in Column")
col_frame_label.grid(row=0, column=0, columnspan=2, sticky="w")

# Create Canvas (not used in this example)
canvas = tk.Canvas(window, width=0, height=0)
canvas.grid(row=0, column=3, rowspan=2, padx=10, pady=10)

# Arrange buttons
invisible_button.grid(row=2, column=0, pady=5)
visible_button.grid(row=2, column=1, pady=5)
exit_button.grid(row=2, column=2, pady=5)

# Event Loop
window.mainloop()