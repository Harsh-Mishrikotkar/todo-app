import functions
import FreeSimpleGUI as sg

label = sg.Txt("Type in a To-Do")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")

window = sg.Window("My-Todo-App",
                   layout = [[label], [inputBox, addButton]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.getTodos()
            newTodo = values["todo"] + "\n"
            todos.append(newTodo)
            functions.writeTodos(todos)
        case sg.WINDOW_CLOSED:
            break


window.close()

