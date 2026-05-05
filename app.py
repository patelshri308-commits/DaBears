import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

game_stats = pd.read_csv("game_stats.csv")

X = game_stats[["YPP_Diff", "turnover_margin", "explosive_play_margin"]]
y = game_stats["point_diff"]

model = LinearRegression()
model.fit(X, y)

st.title("Chicago Bears Game Outcome Predictor")

st.write(
    "Adjust the game-level metrics below to estimate the Bears' point differential."
)

ypp_diff = st.slider("Yards Per Play Differential", -5.0, 5.0, 0.0, 0.1)
turnover_margin = st.slider("Turnover Margin", -5, 5, 0)
explosive_play_margin = st.slider("Explosive Play Margin", -5, 5, 0)

input_data = pd.DataFrame([{
    "YPP_Diff": ypp_diff,
    "turnover_margin": turnover_margin,
    "explosive_play_margin": explosive_play_margin
}])

prediction = model.predict(input_data)[0]

st.metric("Predicted Point Differential", round(prediction, 1))

if prediction > 0:
    st.success("Prediction: Bears Win")
elif prediction < 0:
    st.error("Prediction: Bears Loss")
else:
    st.warning("Prediction: Toss-up")

st.divider()

st.subheader("Model Features")
st.write("""
- **YPP Differential**: efficiency advantage/disadvantage  
- **Turnover Margin**: possession swing impact  
- **Explosive Play Margin**: big-play advantage/disadvantage  
""")
