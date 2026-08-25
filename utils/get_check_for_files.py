import subprocess

README_NAMES = ["readme.md", "readme.rst", "readme.txt", "readme"]
CLAUDE_NAMES = {"claude.md", ".claude"}
LICENSE_NAMES = {"license", "license.md", "license.txt", "copying"}
CI_PATHS = {
    ".github/workflows", ".gitlab-ci.yml", ".circleci/config.yml",
    "azure-pipelines.yml", "jenkinsfile", ".travis.yml",
}
TEST_DIR_HINTS = {"test", "tests", "spec", "specs", "__tests__"}
TEST_FILE_HINTS = ("test_", "_test.", ".test.", ".spec.")
DOCKERFILE_NAMES = {"dockerfile", "dockerfile.dev", "dockerfile.prod", ".dockerfile"}

def has_readme(files):
    for file in files:
        if file.lower() in README_NAMES:
            return True
    return False

def has_claude(files):
    for file in files:
        if file.lower() in CLAUDE_NAMES:
            return True
    return False

def has_license(files):
    for file in files:
        if file.lower() in LICENSE_NAMES:
            return True
    return False

def has_ci(files):
    for file in files:
        if file.lower() in CI_PATHS:
            return True
    return False

def has_tests(files):
    for file in files:
        if file.lower() in TEST_DIR_HINTS or any(hint in file.lower() for hint in TEST_FILE_HINTS):
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