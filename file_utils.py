def read_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        article = file.read()
        return article
