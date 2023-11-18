#!/usr/bin/env python3
import os
import subprocess
import configparser
import pyperclip

def get_current_directory_name():
    return os.path.basename(os.getcwd())

def get_git_username():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser("~/.gitconfig"))
    return config.get("user", "username")

def create_github_repo(repo_name):
    subprocess.run(["gh", "repo", "create", repo_name, "--public"], check=True)

def add_remote_origin(repo_name, username):
    remote_url = f"git@github.com:{username}/{repo_name}.git"
    subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
    return f"https://github.com/{username}/{repo_name}"

def push_to_origin(branch_name="main"):
    subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

def copy_to_clipboard(text):
    pyperclip.copy(text)

def main():
    repo_name = get_current_directory_name()
    username = get_git_username()
    create_github_repo(repo_name)
    https_url = add_remote_origin(repo_name, username)
    push_to_origin()  # You can modify this to push a specific branch
    copy_to_clipboard(https_url)
    print("Repository setup complete. URL copied to clipboard.")

if __name__ == "__main__":
    main()
