from tkinter.filedialog import askdirectory
import datetime
import pyperclip as clip
import tkinter
import time
import threading
import os

GEOMETRY = "400x200"
HEADING = "Clipboard Logging"

logging = True
no_of_thread = 0


def Ui_Init(ui_geometry):
    ui_window = tkinter.Tk()
    ui_window.geometry(ui_geometry)
    return ui_window


def Ui_Heading_Init(ui_window, ui_heading):
    heading = tkinter.Label(
        ui_window, font=("Helvetica", 14), width=400, text=ui_heading
    )
    heading.config(bg="SeaGreen3", fg="LightYellow")
    heading.pack()
    return heading


def Button_Init(ui_window, title, x_axis, y_axis, cmd, color="green"):
    ui_button = tkinter.Button(
        ui_window, text=title, width=15, bg="LightYellow", fg=color, command=cmd
    )
    ui_button.place(x=x_axis, y=y_axis)
    return ui_button


def Ask_File_Path():
    folder_path = askdirectory()
    datetime_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = folder_path + "/clipper_" + datetime_now + ".txt"
    return file_path


def Create_File(file_path):
    file = open(file_path, "x")
    file.close


def Clip_Logger(file_path):
    global logging
    current_clip = clip.paste()
    file = open(file_path, "a")
    while logging:
        if current_clip != clip.paste():
            file.write(clip.paste() + "\n")
            current_clip = clip.paste()
        time.sleep(0.01)
    file.close()
    print(file_path)
    os.system(f"Notepad.exe {file_path}")


def Threading(ui_window):
    global no_of_thread
    if no_of_thread == 0:
        no_of_thread = 1
        run_status = tkinter.Label(
            ui_window, font=("Helvetica", 14), width=400, text="<<<< Running >>>>"
        )
        run_status.config(bg="SeaGreen3", fg="LightYellow")
        run_status.pack()

        file_path = Ask_File_Path()
        Create_File(file_path)
        thread = threading.Thread(target=Clip_Logger, args=(file_path,))
        thread.start()


def Close(ui_window):
    global logging
    logging = False
    ui_window.destroy()


if __name__ == "__main__":
    ui_window = Ui_Init(GEOMETRY)
    ui_heading = Ui_Heading_Init(ui_window, HEADING)
    ui_button_1 = Button_Init(
        ui_window, "Run", 50, 95, cmd=lambda: Threading(ui_window)
    )
    ui_button_2 = Button_Init(
        ui_window, "Close", 230, 95, cmd=lambda: Close(ui_window), color="red"
    )
    ui_window.mainloop()
    logging = False
    print("All Done")
