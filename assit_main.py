from tkinter import *
import wikipedia
import wolframalpha

LARGE_FONT= ("Verdana", 12)


class assitGUI:
 

    def __init__(self, master):
        self.master = master
        self.master.title("Assit")

        self.label = Label(master, text="Hello I am AssitYou! Tell me How can I help You?", font=LARGE_FONT)
        self.label.pack(fill='x', pady='5')

        self.entry = Entry(master, selectborderwidth='5', font=LARGE_FONT)
        self.entry.focus()
        self.entry.bind("<Return>", self.onReturnPressed)
        self.entry.pack(padx='10',pady='10',fill='x')
        self.centerWindow()

    def centerWindow(self):
        w=800
        h=80
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onReturnPressed(self,event):
        query = self.entry.get()
        query.lower()
        try:
            app_id="AW8AWJ-GEGXVQVWLX"
            client = wolframalpha.Client(app_id)
            res = client.query(query);
            ans = next(res.results).text
        except:
            try:
                wikipedia.set_lang("en")
                ans = wikipedia.summary(query, sentences = 2)
            except wikipedia.exceptions.DisambiguationError as e:
                ans = "I might have multiple matchings  \n"+"\n".join(map(str, e.options))

        window = Toplevel(self.master)
        answer = Text(window, font=LARGE_FONT)
        answer.insert(INSERT, ans)
        answer.pack(padx='5', pady='5')
        window.geometry("800x200")

if __name__ == '__main__':
    root = Tk()
    my_gui = assitGUI(root)
    root.mainloop()
