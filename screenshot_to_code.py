import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import requests
import base64
import openai




# Global variable to store the path of the uploaded image
uploaded_image_path = None
api_key_entry = None
upload_btn = None

def upload_image():
    global uploaded_image_path, status_label
    file_path = filedialog.askopenfilename()
    if file_path:
        uploaded_image_path = file_path
        status_label.config(text="Image uploaded successfully!")

def send_to_gpt4_vision_api(image_path, api_key):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    api_url = "https://api.openai.com/v1/images/edits"  # Replace with the actual API endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "image": encoded_string  # Adjust this as per the API's requirements
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()  # Adjust this based on the API's response format
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def apply_api_key():
    global upload_btn, status_label
    api_key = api_key_entry.get()

    if not api_key.strip():
        messagebox.showerror("Error", "API key is missing.")
        status_label.config(text="Error: API key is missing.")
        return

    openai.api_key = api_key

    try:
        # Use the correct endpoint for the version of the openai package
        response = openai.Engine.list()  # This is the new way to list models in openai>=1.0.0

        if response:
            upload_btn.config(state=tk.NORMAL)
            status_label.config(text="API key is valid. You can now upload an image.")
            messagebox.showinfo("Success", "API key is valid. You can now upload an image.")
        else:
            raise ValueError("The API key is not valid.")
            
    except Exception as e:
        messagebox.showerror("Error", f"Failed to verify API Key: {e}")
        status_label.config(text="Failed to verify API Key.")




def main():
    global api_key_entry, status_label, upload_btn
    app = tk.Tk()
    app.title("Screenshot to Code Converter")
    app.geometry("600x600")

    style = ttk.Style()
    style.theme_use('clam')

    upload_frame = ttk.Frame(app)
    upload_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    upload_btn = ttk.Button(upload_frame, text="Upload Screenshot", command=upload_image, state=tk.DISABLED)
    upload_btn.pack(pady=10)

    api_frame = ttk.Frame(app)
    api_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    api_key_label = ttk.Label(api_frame, text="Enter GPT-4 Vision API Key:")
    api_key_label.pack(side=tk.LEFT)

    api_key_entry = ttk.Entry(api_frame, width=30)
    api_key_entry.pack(side=tk.LEFT, padx=10)

    apply_button = ttk.Button(api_frame, text="Apply", command=apply_api_key)
    apply_button.pack(side=tk.LEFT)

    status_label = ttk.Label(app, text="Please enter your API key and click Apply.")
    status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()