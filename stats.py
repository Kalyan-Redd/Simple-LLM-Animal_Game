# "Stats" page: number of games, average guesses, bar charts and quality ratings.
import pandas as pd
import streamlit as st

st.title("Your Stats")

games = st.session_state.get("games", [])
if not games:
    st.info("No finished games yet. Go to the **Play** page and find an animal!")
    st.stop()

df = pd.DataFrame({
    "Game": [f"Game {i}" for i in range(1, len(games) + 1)],
    "Guesses": [g["guesses"] for g in games],
    "Average quality (0-3)": [round(g["avg_quality"], 2) for g in games],
}).set_index("Game")

# Basic numbers.
col1, col2, col3 = st.columns(3)
col1.metric("Games played", len(games))
col2.metric("Average guesses per game", f"{df['Guesses'].mean():.1f}")
col3.metric("Average guess quality (0-3)", f"{df['Average quality (0-3)'].mean():.2f}")

st.subheader("Number of guesses per game")
st.bar_chart(df["Guesses"])

# Quality estimation (the LLM rates every message, see rubric below).
st.subheader("Quality of your guesses")
st.caption("After each message, the LLM rates it: **0** = off-topic / repeated, "
           "**1** = weak, **2** = good, **3** = excellent (splits the possibilities in half "
           "or is a smart guess). Below you can see the average per game and every single rating.")
st.bar_chart(df["Average quality (0-3)"])

with st.expander("Show every rating with the reason"):
    for i, game in enumerate(games, start=1):
        st.markdown(f"**Game {i}**")
        st.dataframe(pd.DataFrame(game["ratings"]).rename(
            columns={"message": "Your message", "quality": "Quality", "reason": "Reason"}),
            hide_index=True, use_container_width=True)
