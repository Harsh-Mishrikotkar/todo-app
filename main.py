import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    userAction = input("Type add, show, edit, complete, or exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        todo = userAction[4:] + "\n"
        todos = functions.getTodos()
        todos.append(todo)
        functions.writeTodos(todos)

    elif userAction.startswith("show"):
        todos = functions.getTodos()

        for i, j in enumerate(todos):
            row = f"{i+1}-{j.strip("\n")}"
            print(row)

    elif userAction.startswith("edit"):
        try:
            number = int(userAction[5:])
            todos = functions.getTodos()
            print("Here is existing todos: ", todos)
            newTodo = input("Enter a new todo: ")
            todos[number-1] = newTodo + "\n"
            functions.writeTodos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif userAction.startswith("complete"):
        try:
            number = int(userAction[9:])
            todos = functions.getTodos()
            removed = todos[number - 1].strip("\n")
            todos.pop(number-1)

            functions.writeTodos(todos)

            message = f"Todo {removed} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

        except ValueError:
            print("Your command is invalid.")
            continue

    elif userAction.startswith("exit"):
        break

    else:
        print("Command is not valid.")


print("Bye!")