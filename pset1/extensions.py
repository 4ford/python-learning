file_name = input("File name: ")

dot_index = file_name.find('.')

f_d_e =file_name.strip().lower()
f_d_e = f_d_e[-4:].replace(".", "")

if f_d_e == "jpg":
    f_d_e = "jpeg"
#FDE is what I have the ending as
if f_d_e in ["jpeg", "gif", "png"]:
    print(f"image/{f_d_e}")
elif f_d_e in ["pdf", "zip"]:
    print(f"application/{f_d_e}")
elif f_d_e == "txt":
    print(f"text/plain")
else:
    print("application/octet-stream")
