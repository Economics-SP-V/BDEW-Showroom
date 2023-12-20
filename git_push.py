# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:20:28 2023

@author: Christopher.Troost
"""

import subprocess
import os

# Set the path to your repository
repo_path = r'C:\Users\Public\_python\BDEW-Showroom'

# Change to the repository directory
os.chdir(repo_path)

# Run Git commands
try:
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Daily Update'], check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    print("Git push completed successfully.")
except subprocess.CalledProcessError as e:
    print(f'An error occurred: {e}')