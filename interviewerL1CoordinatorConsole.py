import tkinter as tk
import tkinter.font as font
import datetime as dt

window = tk.Tk()

main_background = '#023e8a'
button_bgcolor = '#48CAE4'
font_color = 'white'

timeEmailSentAll = ""
timeEmailSentAbsent = ""
weekExcelSheetAdded = ""
weekOf = dt.datetime.now()

window.iconbitmap(default='cognizant.ico')
window.title('L1 Reminder emails')
window.geometry('550x350+325+0')
window.configure(bg=main_background)

titleFont = font.Font(family='Arial', weight='bold', size=18)
labelFont = font.Font(family='Arial', weight='bold', size=12)

title = tk.Label(window, bg=main_background, fg=font_color, font=titleFont, text="L1 Interviewer Coordination Console")
title.pack(pady=10)


def on_show_and_hide_result(label, message):
    label.configure(text=message)
    window.after(4000, lambda: label.configure(text=''))


def on_send_all():
    global timeEmailSentAll

    if timeEmailSentAll == "" or dt.datetime.now() > timeEmailSentAll:
        # TODO: add ALL interviewers email functionality here
        email_all_interviewers_result.configure(fg="lightGreen")
        on_show_and_hide_result(email_all_interviewers_result, 'email sent to all L1 interviewers')
        timeEmailSentAll = dt.datetime.now() + dt.timedelta(hours=24)
    else:
        email_all_interviewers_result.configure(fg="red")
        on_show_and_hide_result(email_all_interviewers_result, 'sorry, an email was already sent today')


def on_send_absent():
    global timeEmailSentAbsent

    if timeEmailSentAbsent == "" or dt.datetime.now() > timeEmailSentAbsent:
        # TODO: add ABSENT interviewers email functionality here
        email_absent_interviewers_result.configure(fg="lightGreen")
        on_show_and_hide_result(email_absent_interviewers_result, 'email sent to all L1 interviewers not in spreadsheet')
        timeEmailSentAbsent = dt.datetime.now() + dt.timedelta(hours=24)
    else:
        email_absent_interviewers_result.configure(fg="red")
        on_show_and_hide_result(email_absent_interviewers_result, 'sorry, an email was already sent today')


def on_add_week():
    global weekExcelSheetAdded
    # if a spreadsheet hasn't been added before or it's been longer than a week since the last one, add spreadsheet
    if weekExcelSheetAdded == "" or dt.datetime.now() > weekExcelSheetAdded:
        # TODO: add addSpreadsheet functionality here
        add_newWeek_toSpreadsheet_fromTemplate_result.configure(fg="lightGreen")
        # If today is monday, set next Monday as next day to add new spreadsheet:
        if dt.datetime.now().weekday() == 0:
            weekExcelSheetAdded = dt.datetime.now() + dt.timedelta(days=7)
        # else add enough days to current day make next Monday the next day to add new spreadsheet.
        else:
            if weekExcelSheetAdded == "":
                weekExcelSheetAdded = dt.datetime.now()
            weekExcelSheetAdded = weekExcelSheetAdded + dt.timedelta(days=7 - weekExcelSheetAdded.weekday())
        on_show_and_hide_result(add_newWeek_toSpreadsheet_fromTemplate_result, f"New week added starting {weekExcelSheetAdded:%A, %B %d, %Y}")
    else:
        add_newWeek_toSpreadsheet_fromTemplate_result.configure(fg="red")
        on_show_and_hide_result(add_newWeek_toSpreadsheet_fromTemplate_result, 'sorry, a new L1 spreadsheet has already been added for next week')


# TODO: make this more modular
email_all_interviewers_label = tk.Label(window, font=labelFont, fg=font_color, bg=main_background, text="Send reminder to all L1 Interviewers")
email_all_interviewers_button = tk.Button(window, text="Send", width=25, bg=button_bgcolor, command=on_send_all)
email_all_interviewers_result = tk.Label(window, fg=font_color, bg=main_background, text="")
email_all_interviewers_label.pack()
email_all_interviewers_button.pack()
email_all_interviewers_result.pack()

email_absent_interviewers_label = tk.Label(window, font=labelFont, fg=font_color, bg=main_background, text="Send reminder to absent L1 Interviewers")
email_absent_interviewers_button = tk.Button(window, text="Send", width=25, bg=button_bgcolor, command=on_send_absent)
email_absent_interviewers_result = tk.Label(window, fg=font_color, bg=main_background, text="")
email_absent_interviewers_label.pack()
email_absent_interviewers_button.pack()
email_absent_interviewers_result.pack()

add_newWeek_toSpreadsheet_fromTemplate_label = tk.Label(window, font=labelFont, fg=font_color, bg=main_background, text="Add new week to spreadsheet")
add_newWeek_toSpreadsheet_fromTemplate_button = tk.Button(window, text="Add Week", width=25, bg=button_bgcolor, command=on_add_week)
add_newWeek_toSpreadsheet_fromTemplate_result = tk.Label(window, fg=font_color, bg=main_background, text="")
add_newWeek_toSpreadsheet_fromTemplate_label.pack()
add_newWeek_toSpreadsheet_fromTemplate_button.pack()
add_newWeek_toSpreadsheet_fromTemplate_result.pack()

window.mainloop()
