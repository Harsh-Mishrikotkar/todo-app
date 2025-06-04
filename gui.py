import functions
import FreeSimpleGUI as sg

label = sg.Txt("Type in a To-Do")
inputBox = sg.InputText(tooltip="Enter todo")
addButton = sg.Button("Add")

window = sg.Window("My-Todo-App", layout = [[label], [inputBox, addButton]])
window.read()
print("hello")
window.close()

