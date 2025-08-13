import streamlit as st
import bank_backend as bank

st.set_page_config("StreamBank", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None

# Sidebar menu
menu = ["Home", "Login", "Create Account"]
if st.session_state.user:
    menu = ["Dashboard", "Logout"]
choice = st.sidebar.selectbox("Navigation", menu)

# Create account
if choice == "Create Account":
    st.title("🚀 Create a New Account")
    with st.form("signup"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        email = st.text_input("Email")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        submit = st.form_submit_button("Create")

        if submit:
            success, message = bank.create_account(name, age, email, pin)
            if success:
                st.success("Account created!")
                st.info(f"Save your A/C number: `{message}`")
            else:
                st.error(message)

# Login
elif choice == "Login":
    st.title("🔐 Login")
    with st.form("login"):
        ac = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        login = st.form_submit_button("Login")

        if login:
            user = bank.authenticate(ac, pin)
            if user:
                st.session_state.user = user
                st.success(f"Welcome, {user['name']}")
                st.rerun()  # 🔁 Updated
            else:
                st.error("Invalid credentials")

# Dashboard
elif choice == "Dashboard":
    user = st.session_state.user
    st.title(f"🏦 Welcome, {user['name']}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["💰 Deposit", "💸 Withdraw", "📄 Details", "✏️ Update", "❌ Close"])

    with tab1:
        amt = st.number_input("Deposit amount (max ₹10000):", step=100)
        if st.button("Deposit"):
            if 0 < amt <= 10000:
                user["Balance"] += amt
                bank.update_balance(user, user["Balance"])
                st.success(f"Deposited ₹{amt}")
            else:
                st.error("Invalid amount")

    with tab2:
        amt = st.number_input("Withdraw amount:", step=100, key="withdraw")
        if st.button("Withdraw"):
            if amt <= 0:
                st.error("Invalid amount")
            elif amt > user["Balance"]:
                st.error("Insufficient balance")
            else:
                user["Balance"] -= amt
                bank.update_balance(user, user["Balance"])
                st.success(f"Withdrew ₹{amt}")

    with tab3:
        st.subheader("📄 Account Info")
        for k, v in user.items():
            st.text(f"{k}: {v}")

    with tab4:
        st.subheader("✏️ Update Info")
        name = st.text_input("New name", value=user["name"])
        email = st.text_input("New email", value=user["email"])
        pin = st.text_input("New PIN (optional)", max_chars=4)

        if st.button("Update Info"):
            updates = {"name": name, "email": email}
            if pin:
                if len(pin) == 4 and pin.isdigit():
                    updates["pin"] = int(pin)
                else:
                    st.error("PIN must be 4-digit.")
                    st.stop()

            updated_user = bank.update_user_info(user["A/C No."], updates)
            st.session_state.user = updated_user
            st.success("Account updated!")

    with tab5:
        if st.button("Yes, close my account"):
            bank.close_account(user["A/C No."])
            st.success("Account closed")
            st.session_state.user = None
            st.rerun()  # 🔁 Updated

# Logout
elif choice == "Logout":
    st.session_state.user = None
    st.success("Logged out")
    st.rerun()  # 🔁 Updated

# Home
elif choice == "Home":
    st.title("💼 StreamBank - Banking App")
    st.markdown("""
Welcome to **StreamBank**, your local banking simulator built in Python using Streamlit.

Features:
- Create & manage bank accounts
- Deposit & withdraw money
- Update account info or close account
""")
