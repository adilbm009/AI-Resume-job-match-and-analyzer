def load_jobs(path):

    with open(path, "r") as f:
        text = f.read()

    jobs = text.split("---")   # split the text

    jobs = [j.strip() for j in jobs if j.strip()]

    return jobs