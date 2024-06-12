from tkinter import *
import requests
from tkinter.messagebox import showerror

response = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js").json()


def show_exchange_rate():
    exchange_rate = entry1.get().upper()
    if not exchange_rate:
        label1.config(text="")
        showerror("Ошибка", "Строка не может быть пустой!")
    else:
        if exchange_rate not in response["Valute"].keys():
            label1.config(text="")
            showerror("Ошибка", "Указанный код валюты не найден!")
        else:
            label1.config(text=f"Курс: {round(response['Valute'][exchange_rate]['Value'], 2)} RUB\n"
                               f"Валюта: {response['Valute'][exchange_rate]['Name']}")


window = Tk()
window.geometry(f"500x200")
window.title("Курсы валют")
window.resizable(False, False)

text = Label(window, text="Введите буквенный код валюты", font=("Times New Roman", 12, "bold"))
text.pack(expand=True, anchor="center")

entry1 = Entry(window)
entry1.pack(expand=True, anchor="center")
entry1.focus()

label1 = Label(window, font=("Times New Roman", 20))
label1.pack(expand=True, anchor="center")

button1 = Button(window, text="Показать обменный курс", command=show_exchange_rate)
button1.pack(expand=True, anchor="center")

window.mainloop()
