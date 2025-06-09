import streamlit as st
import functions

todos = functions.getTodos()

def addTodo():
    todo = st.session_state["newTodo"] + "\n"
    todos.append(todo)
    functions.writeTodos(todos)


st.title("My ToDo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder="Add a new ToDo...",
              on_change=addTodo,
              key="newTodo")