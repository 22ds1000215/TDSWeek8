import streamlit as st
def main():
    st.title('Subtraction Of Two Inputs')
    number1 = st.number_input('Insert Value1')
    number2 = st.number_input('Insert Value2')
    subtraction=number1-number2
    st.write('The subtraction of above numbers is  Number1-Number2 ', subtraction)
    
if __name__ == "__main__":
    main()
