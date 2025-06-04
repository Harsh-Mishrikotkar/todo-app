def getTodos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todoslocal= file.readlines()
    return todoslocal

def writeTodos(todosARG, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todosARG)
    return

if __name__ == "__main__":
    print("Hello!")
    print(getTodos())