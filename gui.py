import functions
import FreeSimpleGUI as sg
import time

sg.theme("Reds")

clock = sg.Txt("", key="Clock")
label = sg.Txt("Type in a To-Do")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
listBox = sg.Listbox(values=functions.getTodos(), key="todos",
                     enable_events=True, size=(45,10))
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("EXIT")

window = sg.Window("My-Todo-App",
                   layout = [[clock],
                             [label],
                             [inputBox, addButton],
                             [listBox, editButton, completeButton],
                             [exitButton]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=500)
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.getTodos()
            newTodo = values["todo"] + "\n"
            todos.append(newTodo)
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                editTodo = values["todos"][0]
                newTodo = values["todo"] + "\n"

                todos = functions.getTodos()
                index = todos.index(editTodo)
                todos[index] = newTodo
                functions.writeTodos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                completeTodo = values["todos"][0]
                todos = functions.getTodos()
                todos.remove(completeTodo)
                functions.writeTodos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "EXIT":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WINDOW_CLOSED:
            break


window.close()

