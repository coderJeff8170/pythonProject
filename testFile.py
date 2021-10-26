import tkinter as tk
from tkinter import BOTTOM

window = tk.Tk()
main_background = '#ADE8F4'
button_bgcolor = '#48CAE4'
font_color = '03045E'

# TODO: fix the icon
window.iconbitmap(default='img.png')
window.title('L1 Reminder emails')
window.geometry('550x350+325+0')
window.configure(bg=main_background)

title = tk.Label(window, bg=main_background, font=24, text="L1 Interviewer Email Console")
title.pack(pady=10)
frame1 = tk.Frame(window).pack()
frame2 = tk.Frame(window).pack(side=BOTTOM)


def incrementHex(hex_str, increment):
    red = int(hex_str[1:3], 16)
    green = int(hex_str[3:5], 16)
    blue = int(hex_str[5:], 16)
    red += increment
    green += increment
    blue += increment
    new_hex_str = '#' + str(hex(red)[2:]) + str(hex(blue)[2:]) + str(hex(green)[2:])
    print(new_hex_str)
    return new_hex_str


def fade(start_hex, increment):
    new_hex = incrementHex(start_hex, increment)
    title.configure(bg=new_hex)
    return new_hex;
    # while new_hex != '#aaaaaa':
    #     fade(new_hex, increment)
    #     print(new_hex)

    # window.after(50, lambda: fade(new_hex, increment))
    # TODO: code to stop it fading?


def on_send_absent():
    print("email sent to L1 interviewers absent from Excel spreadsheet")
    email_absent_interviewers_result.configure(text='email sent to all L1 interviewers not in spreadsheet')
    first_hex = '#FFFFFF'
    i = 50
    while i > 0:
        first_hex = fade(first_hex, -1)
        i -= 1
    print(hex(11))


def on_send_all():
    print("email sent to all L1 interviewers")
    email_all_interviewers_result.configure(text='email sent to all L1 interviewers')


# TODO: I'd like these messages to fade out after like 5 seconds, and perhaps not be able to be resubmitted if same
#  day... while color is not equal to 0%, subtract 1%;


email_all_interviewers_label = tk.Label(frame1, bg=main_background, text="Send reminder to all L1 Interviewers")
email_all_interviewers_button = tk.Button(frame1, text="Send", width=25, bg=button_bgcolor, command=on_send_all)
email_all_interviewers_result = tk.Label(frame1, bg=main_background, text="")

email_absent_interviewers_label = tk.Label(frame2, bg=main_background, text="Send reminder to absent L1 Interviewers")
email_absent_interviewers_button = tk.Button(frame2, text="Send", width=25, bg=button_bgcolor, command=on_send_absent)
email_absent_interviewers_result = tk.Label(frame2, bg=main_background, text="")

email_all_interviewers_label.pack()
email_all_interviewers_button.pack()
email_all_interviewers_result.pack()

email_absent_interviewers_label.pack()
email_absent_interviewers_button.pack()
email_absent_interviewers_result.pack()

window.mainloop()
