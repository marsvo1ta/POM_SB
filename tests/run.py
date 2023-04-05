import pytest


if __name__ == "__main__":
    
    pytest.main(["-s", "-v", "-n=4", "--headless", "--github-report", "--dashboard", "--pls=none", "--sjw"])
    