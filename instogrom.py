import streamlit as st
import pandas as pd
from datetime import datetime
# Simulated Database (in-memory)
if "posts" not in st.session_state:
    st.session_state.posts = []
# Function to add a new post
def add_post(user, content):
    if content:
        new_post = {
            "user": user,
            "content": content,
            "likes": 0,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.posts.insert(0, new_post)  
# Newest post at the top
# Function to like a post
def like_post(index):
    st.session_state.posts[index]["likes"] += 1
# Streamlit UI
st.title("🗣 Social App")
# Sidebar for User Info
st.sidebar.header("User Info")
username = st.sidebar.text_input("Enter your name", "Guest")
# for Posting Section
st.subheader("Create a Post")
content = st.text_area("What's on your mind?")
if st.button("Post"):
    add_post(username, content)
st.write("---")
#  for Displaying Posts
st.subheader("📢 Community Posts")
if st.session_state.posts:
    for index, post in enumerate(st.session_state.posts):
        with st.container():
            st.write(f"**{post['user']}** at *{post['time']}*")
            st.write(post["content"])
            col1, col2 = st.columns([0.1, 0.9])
            with col1:
                if st.button(f"👍 {post['likes']}", key=index):
                    like_post(index)
            st.write("---")
else:
    st.info("No posts yet. Be the first to share something!")
