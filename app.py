import os
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog, messagebox

# Set up the visual theme of the app
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

class ImageToPdfApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Free Image to PDF Converter")
        self.geometry("500x450")
        self.resizable(False, False)

        # Track selected images in a list
        self.selected_images = []

        # --- UI ELEMENTS ---
        
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Image to PDF Converter", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(padx=20, pady=20)

        # Button to select images
        self.select_btn = ctk.CTkButton(self, text="Select Images", command=self.select_images_action)
        self.select_btn.pack(padx=20, pady=10)

        # Text box to show selected files
        self.file_list_box = ctk.CTkTextbox(self, width=400, height=180)
        self.file_list_box.pack(padx=20, pady=10)
        self.file_list_box.insert("0.0", "No images selected yet...\n\n(Tip: Hold Ctrl or Cmd to select multiple files at once!)")
        self.file_list_box.configure(state="disabled") # Prevent user typing inside it

        # Button to convert
        self.convert_btn = ctk.CTkButton(self, text="Convert to PDF", command=self.convert_to_pdf_action, fg_color="green", hover_color="darkgreen")
        self.convert_btn.pack(padx=20, pady=20)

    # --- ACTIONS ---

    def select_images_action(self):
        # Allow user to select multiple images (PNG, JPG, JPEG)
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        
        if files:
            # .extend() adds the new selections to your existing list
            self.selected_images.extend(list(files))
            
            # Update the text box to show all selected files
            self.file_list_box.configure(state="normal")
            self.file_list_box.delete("0.0", "end")
            for file in self.selected_images:
                self.file_list_box.insert("end", f"📄 {os.path.basename(file)}\n")
            self.file_list_box.configure(state="disabled")

    def convert_to_pdf_action(self):
        if not self.selected_images:
            messagebox.showwarning("Error", "Please select at least one image first!")
            return

        # Ask the user where to save the output PDF
        output_pdf_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save PDF As"
        )

        if output_pdf_path:
            try:
                image_list = []
                
                # Open the first image and convert it to RGB mode (PDFs require RGB)
                first_image = Image.open(self.selected_images[0]).convert("RGB")
                
                # Open all subsequent images and convert them to RGB
                for img_path in self.selected_images[1:]:
                    image_list.append(Image.open(img_path).convert("RGB"))
                
                # Save as PDF (this compiles them all into one file!)
                first_image.save(output_pdf_path, save_all=True, append_images=image_list)
                
                messagebox.showinfo("Success", f"PDF successfully created at:\n{output_pdf_path}")
                
                # Reset the app state so it's clean for the next conversion
                self.selected_images = []
                self.file_list_box.configure(state="normal")
                self.file_list_box.delete("0.0", "end")
                self.file_list_box.insert("0.0", "No images selected yet...\n\n(Tip: Hold Ctrl or Cmd to select multiple files at once!)")
                self.file_list_box.configure(state="disabled")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Run the application
if __name__ == "__main__":
    app = ImageToPdfApp()
    app.mainloop()