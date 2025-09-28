# DemoQA Automation Project

This project automates the testing of the Practice Form feature on the DemoQA website using Selenium WebDriver and Python. The tests are structured using the Page Object Model (POM) and the `unittest` framework for better organization and scalability.

## Project Structure

```
project-root/
├── src/
│   ├── practice_form_test.py  # Main test script
├── resources/
│   ├── sample.txt             # File used for upload testing
```

## Prerequisites

1. **Python**: Ensure Python 3.10+ is installed.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: Ensure the ChromeDriver version matches your Chrome browser version.
4. **Dependencies**: Install the required Python packages:
   ```bash
   pip install selenium
   ```

## How to Run the Tests

1. Navigate to the project directory:
   ```bash
   cd path/to/project-root
   ```

2. Run the test suite:
   ```bash
   python src/practice_form_test.py
   ```

## Features Tested

- Navigation to the Practice Form page.
- Filling out the form with random data.
- Uploading a `.txt` file.
- Submitting the form.
- Verifying and closing the confirmation popup.

## Notes

- The project uses the Page Object Model (POM) to separate test logic from page interactions.
- Ensure the `sample.txt` file exists in the `resources/` folder for the upload test.

## Future Improvements

- Add more test cases for other features on the DemoQA website.
- Integrate with CI/CD pipelines for automated test execution.