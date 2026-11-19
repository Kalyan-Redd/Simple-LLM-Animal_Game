# 🐾 Guess the Animal: Guessing Game with Stats

A Streamlit app where you guess a secret animal by asking yes/no questions. The game is powered by the University of Osnabrück LLM.

**Live app:** [https://simple-animal-game.streamlit](https://simple-animal-game.streamlit.app/)

## How it works

### Play page
- The app secretly picks a random animal.
- You chat with the host (Streamlit chat component) by asking yes/no questions such as *"Does it live in water?"* or by guessing the animal.
- The LLM answers, gives a small hint after a wrong guess, and checks whether you found the animal.
- The **💡 Give me a hint** button gives an extra hint. Hints do not count as guesses.

### Stats page
- Number of games played
- Average number of guesses per game
- Bar chart of the number of guesses for each game
- **Guess quality:** the LLM rates every message from 0 to 3 and gives a reason:
  - 0 = off-topic, repeated, or already known
  - 1 = weak (barely narrows down the animals, or a random guess)
  - 2 = good (clearly narrows down the possibilities)
  - 3 = excellent (splits the possibilities roughly in half, or a smart guess)
- The page shows the average quality per game as a bar chart, and a table of every message with its rating and reason, so you can see how the score came about.

Stats are kept for the current browser session.

## Project structure

| File | Purpose |
|---|---|
| `app.py` | Entry point, sets up the pages and navigation |
| `play.py` | The "Play" page (game + LLM) |
| `stats.py` | The "Stats" page |
| `requirements.txt` | Python dependencies |

## Run locally

1. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create `.streamlit/secrets.toml` with your key from ai-keys.uni-osnabrueck.de:
   ```toml
   API_KEY = "your-key"
   BASE_URL = "https://litellm.uni-osnabrueck.de/v1"
   MODEL = "RedHatAI/gemma-4-31B-it-FP8-Dynamic"
   ```
3. Start the app:
   ```
   streamlit run app.py
   ```

## Who did 
Developed by Kalyan Reddy Gaddam
