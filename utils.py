def colored_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "end": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"
