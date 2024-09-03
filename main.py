import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.minsize(400,400)
root.title("ვალუტის კურსის გამოთვლა")

from_currency = tk.Label(root,text = "from currency")
from_currency.pack()

from_currency_var = tk.StringVar(value="ლარი")
currencychoosen = ttk.Combobox(root, width = 27, textvariable = from_currency_var)

currencychoosen['values']  = ("ლარი","დოლარი","ევრო")
currencychoosen.place(x=100,y=30)


to_currency = tk.Label(root,text = "to currency")
to_currency.place(x=160,y=70)

to_currency_var = tk.StringVar(value="ლარი")
currencychoosen1 = ttk.Combobox(root, width = 27, textvariable = to_currency_var)

currencychoosen1['values']  = ("ლარი","დოლარი","ევრო")
currencychoosen1.place(x=100,y=110)

amount = tk.Label(root,text = "თანხა")
amount.place(x=160,y=150)

entry = tk.Entry()
entry.place(x=123,y=180)

exchange_rates = {
    "ლარი": {"დოლარი": 0.37, "ევრო": 0.34},
    "დოლარი": {"ლარი": 2.69, "ევრო": 0.91},
    "ევრო": {"ლარი": 2.98, "დოლარი": 1.10},
}

def convert_currencies():
    fromcur = from_currency_var.get()
    tocur = to_currency_var.get()
    amount1 = entry.get()



    if amount1=='':
        text_label.config(text="გთხოვთ შეიყვანოთ თანხა")
    elif fromcur==tocur:
        text_label.config(text=f'{amount1} {fromcur} უდრის {amount1} {tocur}')
    else:
        new = float(amount1) * exchange_rates[fromcur][tocur]
        text_label.config(text=f'{amount1} {fromcur} უდრის {new} {tocur}')



def clear_all():
    entry.delete(0,tk.END)
    text_label.config(text="")


convert_button = tk.Button(text='კონვერტაცია', command= convert_currencies,width=15)
convert_button.place(x=130,y=220)

text_label = tk.Label(root,text='')
text_label.place(x=105,y=260)

clear_button = tk.Button(root,text='გასუფთავება', width=15, command=clear_all)
clear_button.place(x=130,y=330)

root.mainloop()

