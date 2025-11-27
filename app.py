import streamlit as st
import random

st.title("🚫 Anti-Ex Text Generator")
st.subheader("For when your narcissistic, lying, Machiavellian ex drunk-texts 'I miss you'")

pain_points = [
    "You treated me like absolute garbage.",
    "You lied to my face every single day.",
    "You're a narcissistic sociopath.",
    "You drunk-texted your exes while we were together.",
    "You manipulated and gaslit me constantly.",
    "I regret ever believing your fake apologies.",
    "No contact was the best decision I ever made.",
    "Your 'I miss you' means nothing—you just miss control.",
    "Go bother someone else with your toxic games.",
    "I'm finally free from your bullshit."
]

if st.button("Generate savage reply 💅"):
    reply = "Hey, no.\n\n" + " ".join(random.sample(pain_points, 4)) + "\n\nNever text me again. Goodbye."
    st.success(reply)
    st.code(reply)
