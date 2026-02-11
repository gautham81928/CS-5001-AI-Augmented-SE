import streamlit as st
import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    st.title("Prime Number Checker")
    st.write("Enter a number to check if it is prime.")

    number = st.number_input("Number", min_value=0, step=1, value=0)
    if st.button("Check"):
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

    st.subheader("Prime Numbers Between 1 and 100")
    primes = [n for n in range(2, 101) if is_prime(n)]
    st.write(primes)

if __name__ == "__main__":
    main()
