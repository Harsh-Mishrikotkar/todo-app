from faulthandler import enable

import functions
import FreeSimpleGUI as sg

label = sg.Txt("Type in a To-Do")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
listBox = sg.Listbox(values=functions.getTodos(), key="todos",
                     enable_events=True, size=[45,10])
editButton = sg.Button("Edit")

window = sg.Window("My-Todo-App",
                   layout = [[label], [inputBox, addButton], [listBox, editButton]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.getTodos()
            newTodo = values["todo"] + "\n"
            todos.append(newTodo)
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo = values["todos"][0]
            newTodo = values["todo"] + "\n"

            todos = functions.getTodos()
            index = todos.index(todo)
            todos[index] = newTodo
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break


window.close()

