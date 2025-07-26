import os
import matplotlib.pyplot as plt

SCORE_FILE = "results/score_log.txt"
CHART_FILE = "charts/score_summary.png"

def log_result(result, word):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{result.upper()} | Word: {word}\\n")

def generate_score_chart():
    if not os.path.exists(SCORE_FILE):
        return

    with open(SCORE_FILE, "r") as f:
        lines = f.readlines()

    wins = sum(1 for line in lines if "WIN" in line.upper())
    losses = sum(1 for line in lines if "LOSE" in line.upper())

    plt.figure(figsize=(6, 4))
    plt.bar(["Wins", "Losses"], [wins, losses], color=["green", "red"])
    plt.title("🏆 Hangman Score Summary")
    plt.ylabel("Number of Games")
    plt.savefig(CHART_FILE)
    plt.close()
