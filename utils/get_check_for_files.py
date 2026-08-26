import subprocess

README_NAMES = ["README.md"]
CLAUDE_NAMES = ["CLAUDE.md"]
LICENSE_NAMES = ["LICENSE.md"]
CI_PATHS = [
    ".github/workflows"
]
TEST_DIR_HINTS = ["tests", "__tests__"]
TEST_FILE_HINTS = ["_test"]
DOCKERFILE_NAMES = ["Dockerfile"]

def has_readme(files):
    for file in files:
        if file in README_NAMES:
            return True
    return False

def has_claude(files):
    for file in files:
        if file in CLAUDE_NAMES:
            return True
    return False

def has_license(files):
    for file in files:
        if file in LICENSE_NAMES:
            return True
    return False

def has_ci(files):
    for file in files:
        if file in CI_PATHS:
            return True
    return False

def has_tests(files):
    for file in files:
        if file in TEST_DIR_HINTS:
            for test_file in TEST_FILE_HINTS:
                if file.startswith(test_file):
                    return True
                return True
    return False

def has_dockerfile(files):
    for file in files:
        if file.lower() in DOCKERFILE_NAMES:
            return True
    return False

def get_check_for_files(repo_path):

    try:
        result = subprocess.run(
            ["ls", "-a", str(repo_path)],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise Exception(result.returncode, result.args)

        array_of_files = result.stdout.splitlines()
        
    except Exception as e:
        print(f"\n\nError running ls command: {e}\n\n")
   
    return {
        "has_readme": has_readme(array_of_files),
        "has_claude": has_claude(array_of_files),
        "has_license": has_license(array_of_files),
        "has_tests": has_tests(array_of_files),
        "has_ci": has_ci(array_of_files),
        "has_dockerfile": has_dockerfile(array_of_files),
    }