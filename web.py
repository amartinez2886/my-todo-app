import streamlit as st
import functions

# get the todos from todos.txt
todos = functions.get_todos()


# adds todo from input line
def add_todo():
    # gets the data from input field
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)



todos = functions.get_todos()

# Main title
st.title("My Todo App")

# Sub header
st.subheader("This is my todo app")

# p tag equivalent
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    # returns a boolean to determined if it was checked
    checkbox = st.checkbox(todo, key=todo)
    # if it is checked it will remove it from the list
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # delete the session state of the deleted todo
        del st.session_state[todo]
        # needed for checkbox and to re-run
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo", label_visibility="hidden")

