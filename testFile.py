import tkinter as tk
import tkinter.font as font
from tkinter import *
import datetime as dt
from tkinter import ttk

window = tk.Tk()

main_background = '#023e8a'
button_bgcolor = '#48CAE4'
font_color = 'white'
timeSentAll = dt.datetime.now()
timeSentAbsent = dt.datetime.now()

weekOf = dt.datetime.now()

# TODO: fix the icon
window.iconbitmap(default='img.png')
window.title('L1 Reminder emails')
window.geometry('550x350+325+0')
window.configure(bg=main_background)
print(window.configure().keys())

titleFont = font.Font(family='Arial', weight='bold', size=18)
labelFont = font.Font(family='Arial', weight='bold', size=12)

title = tk.Label(window, bg=main_background, fg=font_color, font=titleFont, text="L1 Interviewer Coordination Console")
title.pack(pady=10)
frame1 = tk.Frame(window).pack()
frame2 = tk.Frame(window).pack(side=BOTTOM)


def on_show_and_hide_result(label, message):
    label.configure(text=message)
    window.after(4000, lambda: label.configure(text=''))


def on_send_all():
    # make variable to hold 'timeSentAll' - if it's less than 24hours than last one, or is empty, don't allow new email sent
    # else send new email and update the date
    # if(timeSentAll):
    on_show_and_hide_result(email_all_interviewers_result, 'email sent to all L1 interviewers')


def on_send_absent():
    on_show_and_hide_result(email_absent_interviewers_result, 'email sent to all L1 interviewers not in spreadsheet')


def on_add_week():
    on_show_and_hide_result(add_newWeek_toSpreadsheet_fromTemplate_result, 'new week added to spreadsheet')
    global weekOf
    weekOf += dt.timedelta(days=7)
    label.configure(text=f"{weekOf:%A, %B %d, %Y}")

# TODO: make this more modular
email_all_interviewers_label = tk.Label(frame1, font=labelFont, bg=main_background, text="Send reminder to all L1 Interviewers")
email_all_interviewers_button = tk.Button(frame1, text="Send", width=25, bg=button_bgcolor, command=on_send_all)
email_all_interviewers_result = tk.Label(frame1, bg=main_background, text="")
email_all_interviewers_label.pack()
email_all_interviewers_button.pack()
email_all_interviewers_result.pack()

email_absent_interviewers_label = tk.Label(frame2, font=labelFont, bg=main_background, text="Send reminder to absent L1 Interviewers")
email_absent_interviewers_button = tk.Button(frame2, text="Send", width=25, bg=button_bgcolor, command=on_send_absent)
email_absent_interviewers_result = tk.Label(frame2, bg=main_background, text="")
email_absent_interviewers_label.pack()
email_absent_interviewers_button.pack()
email_absent_interviewers_result.pack()

add_newWeek_toSpreadsheet_fromTemplate_label = tk.Label(frame2, font=labelFont, bg=main_background, text="Add new week to spreadsheet")
add_newWeek_toSpreadsheet_fromTemplate_button = tk.Button(frame2, text="Add Week", width=25, bg=button_bgcolor, command=on_add_week)
add_newWeek_toSpreadsheet_fromTemplate_result = tk.Label(frame2, bg=main_background, text="")
add_newWeek_toSpreadsheet_fromTemplate_label.pack()
add_newWeek_toSpreadsheet_fromTemplate_button.pack()
add_newWeek_toSpreadsheet_fromTemplate_result.pack()

# label = Label(frame2, text=f"{timeSentAll:%A, %B %d, %Y}", font="Calibri, 20")
label = Label(frame2, text='', font="Calibri, 20")
label.pack(pady=20)

window.mainloop()
