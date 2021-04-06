from pyqrcode import create
import tkinter 

canvas = tkinter.Tk()
canvas.title('Qr Code Generator')

data = tkinter.Entry(canvas,justify='center', width = 40 ,font="poppins 20",background="#82eefd")


def gen_qr():
    global dta
    dta = data.get()
    dta = create(dta)
    test = dta.xbm(scale=5)
    global xbm_image
    xbm_image = tkinter.BitmapImage(data=test, foreground="indigo", background='#82eefd')
    image_view.config(image=xbm_image)
    statement.config(text="This is a QR Code for : " + str(data.get()))


heading = tkinter.Label(canvas, text="QR code Generator", font="poppins 40",bg='coral',borderwidth=3, relief="groove")
subtitle = tkinter.Label(canvas, text="Enter the Data ", font="times 30")
make_button = tkinter.Button(canvas, text=" Generate QR", font="times 20",activebackground="coral",borderwidth="7", command=gen_qr)
image_view = tkinter.Label(canvas)
statement = tkinter.Label(canvas, font="times 15")



heading.grid(row=0, column=0, columnspan=2)
subtitle.grid(row=1, column=0,columnspan=2)
data.grid(row=2, column=0,columnspan=2)
make_button.grid(row=4, column=0, columnspan=2,pady=10)
image_view.grid(row=5, column=0, columnspan=2)
statement.grid(row=6, column=0, columnspan=2)

canvas.mainloop()