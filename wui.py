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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",
              placeholder="Add a new ToDo...",
              on_change=addTodo,
              key="newTodo")