import subprocess
import streamlit as st

def run_command(command, cwd=None):
    """Helper function to run a shell command and return its output."""
    process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout.decode(), stderr.decode()

def setup_and_run_interstellar():
    # Run 'npm install' to install dependencies
    returncode, stdout, stderr = run_command(['npm', 'install'], cwd='.')
    if returncode != 0:
        st.error(f'Error during npm install: {stderr}')
        return
    st.success('Dependencies installed successfully.')

    # Run 'npm run start' to launch the Interstellar proxy
    returncode, stdout, stderr = run_command(['npm', 'run', 'start'], cwd='.')
    if returncode == 0:
        st.success('Interstellar is running!')
    else:
        st.error(f'Error starting Interstellar: {stderr}')

if st.button('Setup and Start Interstellar'):
    setup_and_run_interstellar()
