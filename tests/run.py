import pytest
import datetime


if __name__ == "__main__":
    
    # pytest.main(['tests/test_0_start_staging.py', 'tests/test_6_calculator.py', 'tests/test_1_np.py', 'tests/test_1_register.py', "-s", "-v", "-n=4"])
    start = datetime.datetime.today()
    pytest.main(["-s", "-v", "-n=4", "--headless"])
    end = datetime.datetime.today()
    print(end-start)