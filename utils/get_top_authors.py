from utils.git import git

def get_top_authors(repo_path, top_n=3):
    result = git(repo_path, "--no-pager", "shortlog", "-sn")

    authors = []

    count = 0
    for line in result.splitlines():
        name = line.strip().split()

        if len(name) >= 2:
            name = " ".join(name[1:])
            authors.append(name)
            count += 1
            if count >= top_n:
                break

    return authors