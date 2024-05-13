import streamlit as st

def mo_to_mb(mo):
    return mo * 1.024

def mb_to_mo(mb):
    return mb / 1.024

def main():
    st.title("MO to MB and MB to MO Converter ;)")
    option = st.radio("Select conversion direction:", ("MO to MB", "MB to MO"))

    if option == "MO to MB":
        mo = st.number_input("Enter the size in MO:")
        mb = mo_to_mb(mo)
        st.write(f"{mo} MO is equal to {mb} MB.")
    elif option == "MB to MO":
        mb = st.number_input("Enter the size in MB:")
        mo = mb_to_mo(mb)
        st.write(f"{mb} MB is equal to {mo} MO.")

if __name__ == "__main__":
    main()

