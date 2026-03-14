import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = ["Create Account", "Deposit Money", "Withdraw Money", "Show Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    email = st.text_input("Email")
    pin = st.number_input("Pin", 1000, 9999)

    if st.button("Create Account"):
        bank.data.append({
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": pin,
            "Account No": bank._Bank__account_generate(),
            "Balance": 0
        })
        bank._Bank__update()
        st.success("Account created successfully!")

elif choice == "Deposit Money":
    st.subheader("Deposit Money")
    acc = st.text_input("Account No")
    pin = st.number_input("Pin", 1000, 9999)
    amount = st.number_input("Amount", 0)
    if st.button("Deposit"):
        user = bank._Bank__find_user(acc, pin)
        if user:
            user['Balance'] += amount
            bank._Bank__update()
            st.success(f"Deposited! New Balance: {user['Balance']}")
        else:
            st.error("User not found!")

elif choice == "Withdraw Money":
    st.subheader("Withdraw Money")
    acc = st.text_input("Account No")
    pin = st.number_input("Pin", 1000, 9999)
    amount = st.number_input("Amount", 0)
    if st.button("Withdraw"):
        user = bank._Bank__find_user(acc, pin)
        if user:
            if user['Balance'] >= amount:
                user['Balance'] -= amount
                bank._Bank__update()
                st.success(f"Withdrawn! Remaining Balance: {user['Balance']}")
            else:
                st.error("Insufficient balance!")
        else:
            st.error("User not found!")

elif choice == "Show Details":
    st.subheader("Account Details")
    acc = st.text_input("Account No")
    pin = st.number_input("Pin", 1000, 9999)
    if st.button("Show Details"):
        user = bank._Bank__find_user(acc, pin)
        if user:
            st.json(user)
        else:
            st.error("User not found!")
