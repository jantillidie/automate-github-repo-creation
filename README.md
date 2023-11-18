# GitHub Repository Setup Script

This Python script automates the process of creating a new GitHub repository, adding a remote origin, and pushing the current branch. It's a convenient tool for quickly setting up your GitHub projects from the command line. It runs the following steps:

```bash
gh repo create <directory name where you are currently in> --public
git remote add origin git@github.com:<get the github username from the local gitconfig>/<directory name where you are currently in>.git
git push -u origin main
# and copys the URL of the github repo to the clipboard
```

## Prerequisites

Before you begin, ensure you have the following installed on your macOS:

- Python 3
- Git
- GitHub CLI (`gh`)
- `pyperclip` Python module

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/jantillidie/automate-github-repo-creation.git && cd automate-github-repo-creation
   ```

2. **Install Python Dependencies:**

   ```bash
   pip3 install pyperclip
   ```

3. **Make the Script Executable:**

   ```bash
   chmod +x create_repo.py
   ```

4. **Add the Script to Your Path:**

   - Move the script to your `bin` directory (create one in your home directory if it doesn't exist):
     ```bash
     mv create_repo.py ~/bin/
     ```
   - Ensure your `bin` directory is in your PATH. Add this line to your `.bashrc`, `.bash_profile`, or `.zshrc`:
     ```bash
     export PATH="$HOME/bin:$PATH"
     ```

5. **Reload Your Shell Configuration:**
   ```bash
   source ~/.bashrc  # Or the appropriate file for your shell
   ```

## Configuration

### Adding GitHub Username to Git Config

1. **Set Your GitHub Username:**

   ```bash
   git config --global user.username "YourGitHubUsername"
   ```

2. **Verify Configuration:**
   ```bash
   git config --global user.username
   ```
   This should display your GitHub username.

## Usage

Run the script from any initialized git directory where you want to create a new GitHub repository:

```bash
create_repo.py
```

Or, if you've set up an alias:

```bash
create-repo
```

The script will automatically create a new GitHub repository matching the name of your current git directory, set up the remote origin, push the current branch, and copy the repository's URL to your clipboard.

## License

TODO

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.
