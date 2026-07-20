def load_css():
    with open("assets/style.css") as f:
        return f"<style>{f.read()}</style>"