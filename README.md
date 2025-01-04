


# Gmail Email Variations Generator

## Overview

This Python script generates variations of a given Gmail address by appending random strings to the local part of the email. It's useful for creating disposable addresses, testing purposes, or managing Gmail aliases.

### Features

- **Email Validation**: Ensures the entered email is in a valid format.

- **Gmail-Specific**: Works exclusively with Gmail addresses (`gmail.com`).

- **Random Variations**: Generates unique email variations by appending random alphanumeric strings.

- **File Output**: Saves the generated email variations to a file for easy access.

## How It Works

1. **Email Validation**: The script first checks whether the entered email is valid using a regular expression.

2. **Generate Variations**: After validation, the script generates random strings and appends them to the local part of the email, creating unique variations.

3. **Output**: The generated email variations are displayed in the terminal and saved in a file named `generated_emails.txt`.

## Requirements

- Python 3.x (No additional libraries are needed aside from the built-in `re`, `random`, and `string` modules).

## Installation

1. Clone the repository:

```bash

git clone https://github.com/Abol-Ghasem/Infinity-Gmail

```

2. Navigate into the project directory:

```bash

cd Infinity-Gmail

```

3. Ensure you have Python 3 installed.

## Usage

1. Run the script:

```bash

python main.py

```

2. Enter a valid Gmail address when prompted.

3. Specify the number of variations you want to generate.

4. The generated variations will be shown in the terminal and saved to a file named `generated_emails.txt`.

### Example

```text

Enter your email: example@gmail.com

Enter the number of variations: 5

Generated variations:

example+abc12@gmail.com

example+xy34z@gmail.com

example+qwe456@gmail.com

example+gh78w@gmail.com

example+fgh987@gmail.com

The variations have been saved to 'generated_emails.txt'.

```

## Notes

- The tool **only supports Gmail addresses**. If a non-Gmail address is entered, an error message will be displayed.

- The generated random strings are lowercase alphabetic characters by default, but the code can be customized to change this behavior.

