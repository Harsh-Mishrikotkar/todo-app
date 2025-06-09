from faulthandler import enable

import functions
import FreeSimpleGUI as sg

label = sg.Txt("Type in a To-Do")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
listBox = sg.Listbox(values=functions.getTodos(), key="todos",
                     enable_events=True, size=[45,10])
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("EXIT")

window = sg.Window("My-Todo-App",
                   layout = [[label],
                             [inputBox, addButton],
                             [listBox, editButton, completeButton],
                             [exitButton]],
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
            editTodo = values["todos"][0]
            newTodo = values["todo"] + "\n"

            todos = functions.getTodos()
            index = todos.index(todo)
            todos[index] = newTodo
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "Complete":
            completeTodo = values["todos"][0]
            todos = functions.getTodos()
            todos.remove(completeTodo)
            functions.writeTodos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "EXIT":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WINDOW_CLOSED:
            break


window.close()

