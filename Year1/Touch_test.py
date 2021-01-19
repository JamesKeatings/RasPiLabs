from guizero import App, Box, PushButton

def backfunc():
    i=i-1
    textbox.text=textarray[i]

def nextfunc():
    i=i+1
    textbox.text=textarray[i]

i=1

textarray = ["1", "2", "3"]
#textarray[1] = "This is the first page of text.\nIt displays the first message in this array"
#textarray[2] = "This is the second page of text.\nIt displays the second message in this array"
#textarray[3] = "This is the third page of text.\nIt displays the third message in this array"


app=App()

text_box = Box(app, text=repr(textarray[0]), width="fill", align="top")
button_box = Box(app, width="fill", align="bottom")
back_button = PushButton(button_box, backfunc, text="back", align="right")
next_button = PushButton(button_box, nextfunc,text="next", align="left")






app.display()
