version = '0.1'
author = 'lukkshh'
import hashlib , customtkinter
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')
root = customtkinter.CTk()
root.title('Md5 Hash Generator')
root.geometry('450x500')
root.resizable(False , False)
def generate_hash():
    usr_inp = inp.get()
    if usr_inp == '':
        hash_label.configure(text='Please Input Text !')
    else:
        hashed = hashlib.md5(usr_inp.encode()).hexdigest()
        hash_label.configure(text=str(hashed))
        copybtn.configure(state='normal')
def clear_inp():
    inp.delete(0,'end')
    inp.insert(0,'')
def copy(): 
    root.clipboard_clear()
    usr_inp = inp.get()
    hashed = hashlib.md5(usr_inp.encode()).hexdigest()
    root.clipboard_append(hashed)
    hash_label.configure(text='Coppied To Clipboard')
    copybtn.configure(state='disabled')
buttons =("Arial",18)
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20 , padx=20 , fill='both', expand=True)
label = customtkinter.CTkLabel(master=frame, text='MD5 Hash Generator' )
label.configure(font=('Arial',25))
label.pack(pady=12,padx=12)
output_frame = customtkinter.CTkFrame(master=frame)
output_frame.pack(pady=12,padx=12 , fill='x')
hash_label = customtkinter.CTkLabel(master=output_frame, text='' , height=40)
hash_label.configure(font=('Arial', 13))
hash_label.pack(pady=2 , padx=2)
inp = customtkinter.CTkEntry(master=frame , placeholder_text='Input' , height=35)
inp.pack(pady=20, padx=12 , fill='x')
generate = customtkinter.CTkButton(master=frame , text_font=buttons , width=300 , height=40 , text='Generate' , command=generate_hash)
generate.pack(pady=5,padx=12)
clear = customtkinter.CTkButton(master=frame , text_font=buttons , width=300 , height=40 , text='Clear Input', command=clear_inp)
clear.pack(pady=8,padx=12)
copybtn = customtkinter.CTkButton(master=frame , text_font=buttons , width=300 , height=40 , state='disabled' , text='Copy Hash', command=copy)
copybtn.pack(pady=8,padx=12)
exitbtn = customtkinter.CTkButton(master=frame , text_font=buttons , width=300 , height=40 , text='Exit', command=root.destroy)
exitbtn.pack(pady=8,padx=12)
footer = customtkinter.CTkLabel(master=frame, text='lukkshh.ga')
footer.pack(padx = 0.0, pady = 1.0)
root.mainloop()
