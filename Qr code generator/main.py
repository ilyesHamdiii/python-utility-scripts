#pip install qrcode Image

def generator(text):
    qr=qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,

    )
    qr.add_data(text)
    img=qr.make_image(fill_color="black",back_color="white")
    folder_path = os.path.join(script_dir, subfolder)
    os.makedirs(folder_path, exist_ok=True)
    save_path = os.path.join(folder_path, "my_image.png")
    img.save(save_path)

if(__name__=="__main__"):
    import qrcode
    import os 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    subfolder = "img"
generator("https://youtu.be/Bc-2lqvm-nM?si=jyXsO14_QgDxngk5")

