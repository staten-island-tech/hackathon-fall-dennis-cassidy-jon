import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Non-Editable Text Box Example")

# Create a Text widget that is non-editable
text_box = tk.Text(root, height=10, width=30, bd=3, relief="solid", wrap="word")
text_box.insert(tk.END, "This is some non-editable text.")
text_box.config(state=tk.DISABLED)  # Make the text box non-editable
text_box.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()