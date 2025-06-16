import pyfiglet

def generate(text: str) -> str:
    """Convert text into ASCII art."""
    return pyfiglet.figlet_format(text)
