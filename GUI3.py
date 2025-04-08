import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
import os
from fpdf import FPDF

# Initialize Tkinter window
root = Tk()
root.title("Input Form")

# Load the icon (must be a .png file or supported format)
icon = tk.PhotoImage(file="./img/ProLadang-Logo.png")
# Set the icon using iconphoto
root.iconphoto(True, icon)

# Set the desired window size
window_width = 400
window_height = 300

# Get the screen's width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 2

# Set the geometry with the calculated size and position
#root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
root.geometry(f"+{x_offset}+{y_offset}")

# Dictionary to store inputs
inputs = {}

# Function to reset the window
"""def reset_window():
    for widget in root.winfo_children():
        widget.destroy()  # Remove all existing widgets"""
def delete_window():
    global root
    root.destroy()  # Destroy the current window

# Function to handle form and image submission
def submit_form_and_image():
    global inputs
    inputs['Name'] = name_entry.get()
    inputs['Date'] = date_entry.get()
    inputs['HLT'] = hlt_entry.get()
    inputs['Plot'] = plot_entry.get()
    inputs['ImagePath'] = image_entry.get()

    # Validate Image Path
    image_path = inputs['ImagePath']
    if image_path:
        # Remove quotes if present and replace backslashes with forward slashes
        image_path = image_path.strip('"').replace("\\", "/")

        # Check if the file exists
        if not os.path.isfile(image_path):
            messagebox.showerror("Error", "File not found")
            return

    # Reset window if validation succeeds
    inputs['ImagePath'] = image_path
    delete_window()

# Create form labels and entries
Label(root, text="Please insert name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Insert Date (Eg: YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
date_entry = Entry(root, width=30)
date_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Insert HLT:").grid(row=2, column=0, padx=10, pady=5)
hlt_entry = Entry(root, width=30)
hlt_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Insert Plot No (Eg: A(1234)):").grid(row=3, column=0, padx=10, pady=5)
plot_entry = Entry(root, width=30)
plot_entry.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Enter the path to your image:").grid(row=4, column=0, padx=10, pady=5)
image_entry = Entry(root, width=30)
image_entry.grid(row=4, column=1, padx=10, pady=5)

Button(root, text="Submit", command=submit_form_and_image).grid(row=7, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

# Create PDF
pdf = FPDF()
HEIGHT = 297
WIDTH = 210

pdf.set_top_margin(margin=5)
pdf.add_page()
pdf.image("./img/ProLadangHeader.png", x=0, y=0, w=210, h=297)
pdf.set_font("helvetica", size=14)
pdf.cell(190, 10, text="LAPORAN POTENSI SERANGAN PEROSAK & PENYAKIT", border=0, new_x="LMARGIN", new_y="NEXT", align='C', fill=False)
pdf.ln(5)

# Add collected inputs to the PDF
Name1 = "Nama: " + inputs['Name']
Date1 = "Tarikh: " + inputs['Date']
HLT1 = "HLT: " + inputs['HLT']
Plot1 = "Plot: " + inputs['Plot']

column_width = 190 / 2  # Adjust width dynamically for page size
row_height = 10  # Height of each row

pdf.set_font("helvetica", size=14)
pdf.cell(column_width, row_height, text=Name1, border=0, align='L', new_x="RIGHT", new_y="TOP")
pdf.cell(column_width, row_height, text=Date1, border=0, align='L', new_x="LMARGIN", new_y="NEXT")
pdf.cell(column_width, row_height, text=HLT1, border=0, align='L', new_x="RIGHT", new_y="TOP")
pdf.cell(column_width, row_height, text=Plot1, border=0, align='L', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.set_font("helvetica", size=14)
pdf.set_text_color(255,255,255)
pdf.set_fill_color(1,50,32)
pdf.cell(190, 10, text="Kawasan Terlibat", border=1, new_x="LMARGIN", new_y="NEXT", align = 'C', fill=True)
pdf.ln(5)

pdf.image(inputs["ImagePath"], w= 85, h=85)

pdf.set_fill_color(255,0,0)
pdf.ellipse(x=105, y=75, w=10, h=10, style='F')
pdf.set_fill_color(0,0,255)
pdf.ellipse(x=105, y=95, w=10, h=10, style='F')

pdf.set_xy(120, 70)
pdf.set_font("helvetica",style='B', size=16)
pdf.set_text_color(0,0,0)
pdf.cell(80, 20, text="Kawasan potensi risiko", border=0, new_x="LEFT", new_y="NEXT", align = 'L', fill=False)
pdf.cell(80, 20, text="Kawasan pengesahan risiko", border=0, new_x="LMARGIN", new_y="NEXT", align = 'L', fill=False)

pdf.set_xy(105,115)
pdf.set_font("helvetica", size=14)
pdf.multi_cell(w=95, h=10, text="Pergi ke kawasan yang di warnakan biru untuk pengesahan potensi serangan", border=1, align='L', fill=False)

pdf.set_xy(10,150)
pdf.set_text_color(255,255,255)
pdf.set_fill_color(1,50,32)
pdf.cell(190, 10, text="Jenis Serangan & tindakan yang perlu dilakukan", border=1, new_x="LMARGIN", new_y="NEXT", align = 'C', fill=True)
pdf.set_text_color(0,0,0)
pdf.ln(5)


def option1():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Ulat Gulung Daun", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Amalkan kebersihan sawah dan sembur racun serangga.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Cartap Hydrochloride, Chlorantraniliprole, Etofenprox", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Patuhi arahan pada label racun.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="  - Pastikan kawasan sawah bebas daripada sisa tanaman untuk mencegah peringkat larva bersembunyi", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option2():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Kesing", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Kawal serangan menggunakan racun serangga dan perbaiki pengurusan air.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Imidacloprid, Thiamethoxam, Dinotefuran", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Elakkan penanaman serentak di kawasan besar untuk memutuskan kitaran perosak.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="  - Pantau paras air di sawah untuk mengelakkan kelembapan berlebihan yang menarik perosak.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option3():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Tikus", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Pasang perangkap tikus, jaga kebersihan sawah, dan sembur racun jika perlu.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Bromadiolone, Warfarin, Zinc Phosphide", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Letakkan perangkap di laluan tikus utama.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="  - Lakukan kawalan serentak di kawasan sekitar untuk hasil yang lebih berkesan.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option4():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Ulat Batang", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Sembur racun sistemik pada pangkal batang padi.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Agrimec (Abamectin), Chlorantraniliprole, Diafenthiuron", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Potong dan buang batang padi yang dijangkiti larva.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="  - Kawal peringkat telur dengan mengelakkan genangan air berlebihan.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option5():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Karah Daun", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Sembur racun kulat sistemik.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Tricyclazole, Isoprothiolane, Azoxystrobin", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Pemantauan diperlukan pada peringkat awal serangan, terutama dalam keadaan cuaca lembap.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="  - Gunakan varieti padi tahan karah sebagai langkah pencegahan pada musim akan datang.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option6():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Bintik Daun (Bintik Perang)", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Sembur racun kulat.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Iprodione, Propiconazole, Carbendazim", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Sembur pada waktu pagi untuk memastikan penyerapan maksimum.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="  - Elakkan penggunaan racun berulang untuk mengelakkan rintangan.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option7():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Bintik Daun (Bintik Perang Tirus)", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Sembur racun kulat yang sesuai.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Propiconazole, Difenoconazole", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Kawalan awal penting untuk mencegah penyebaran ke kawasan lain.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option8():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Bintik Daun (Bintik Seludang)", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Sembur racun kulat pada tangkai dan seludang padi.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Difenoconazole, Mancozeb", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Kawalan rumpai juga penting untuk mengurangkan kelembapan yang mendorong penyakit.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

def option9():
    pdf.set_font("helvetica",style='B', size=14)
    pdf.cell(w=190, h=5.5, text="Nama perosak/penyakit: Kutu Thrip", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="1. Cara Kawalan: Mudah dikawal dengan menenggelamkan sawah secara berperingkat selama 1-2 hari.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.cell(w=190, h=5.5, text="2. Jenis Racun: Tidak perlu membuat semburan racun", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='B', size=11)
    pdf.cell(w=190, h=5.5, text="  Nota Penting:", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.set_font("helvetica",style='', size=11)
    pdf.cell(w=190, h=5.5, text="  - Menggunakan serangga pemangsa semulajadi seperti kumbang kura-kura, kumbang lanun, kumbang tanah.", border=0, new_x="LEFT", new_y="NEXT", align='L', fill=False)
    pdf.ln(4)

n=0
FileName = inputs['Name'] + "-" + inputs['Plot'] + "-" + inputs['Date'] + ".pdf"

def submit_choice():
    global inputs
    global n

    inputs['choice'] = choice_entry.get()
    if inputs['choice']=="1":
        option1()
        n += 1
    elif inputs['choice']=="2":
        option2()
        n += 1
    elif inputs['choice']=="3":
        option3()
        n += 1
    elif inputs['choice']=="4":
        option4()
        n += 1
    elif inputs['choice']=="5":
        option5()
        n += 1
    elif inputs['choice']=="6":
        option6()
        n += 1
    elif inputs['choice']=="7":
        option7()
        n += 1
    elif inputs['choice']=="8":
        option8()
        n += 1
    elif inputs['choice']=="9":
        option9()
        n += 1
    elif inputs['choice']=="0":
        messagebox.showinfo("PDF", f"PDF created successfully as {FileName}")
        delete_window()
        return
    else:
        messagebox.showerror("Error", "Invalid INPUT!!")

    choice_entry.delete(0, tk.END)

    if n==3:
        messagebox.showinfo("PDF", f"PDF created successfully as {FileName}")
        delete_window()

    
#New window for choice/option
root = Tk()
root.title("Option Form")

# Set the desired window size
window_width = 400
window_height = 300

# Get the screen's width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 2

# Set the geometry with the calculated size and position
#root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
root.geometry(f"+{x_offset}+{y_offset}")

Label(root, text="Choose type of disease (Max 3):\n1. Ulat Gulung Daun\n2. Kesing\n3. Tikus\n4. Ulat Batang\n5. Karah Daun\n6. Bintik Perang\n7. Bintik Perang Tirus\n8. Bintik Seludang\n9. Kutu Thrip\n0.Exit").grid(row=0, column=1, padx=10, pady=5)
choice_entry = Entry(root, width=30)
choice_entry.grid(row=1, column=1, padx=10, pady=5)
Button(root, text="Submit", command=submit_choice).grid(row=2, column=1, columnspan=2, pady=10)

root.mainloop()
pdf.output(FileName)