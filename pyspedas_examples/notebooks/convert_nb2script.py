import os
import subprocess

"""
def convert_notebooks_to_scripts(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter out only the Jupyter Notebook files
    notebooks = [f for f in files if f.endswith('.ipynb')]

    for notebook in notebooks:
        # Construct the full path to the notebook
        notebook_path = os.path.join(directory, notebook)

        # Convert the notebook to a Python script using nbconvert
        # The "--output" flag specifies the output filename without the extension
        output_name = os.path.splitext(notebook)[0]
        subprocess.run(["jupyter", "nbconvert", "--to", "script", notebook_path, "--output", output_name])

# Specify the directory you want to search in
directory_path = "pyspedas_examples/notebooks/"  # Current directory. Change this if needed.
convert_notebooks_to_scripts(directory_path)
"""

import nbformat

def convert_nb2script(notebook_path, output_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    output_content = ""

    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            # Convert markdown content to comments
            comment_lines = ["# " + line for line in cell.source.split("\n")]
            output_content += "\n".join(comment_lines) + "\n\n"
        elif cell.cell_type == "code":
            output_content += cell.source + "\n\n"

    # Save to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content)

def convert_wrapper(directory, out_directory):

    files = os.listdir(directory)

    notebooks = [file for file in files if file.endswith('.ipynb')]

    for notebook in notebooks:
        # Construct the full path to the notebook
        notebook_path = os.path.join(directory, notebook)

        # Construct the output path
        outfile = os.path.splitext(notebook)[0] + '.py'
        outfile_path = os.path.join(out_directory, outfile)

        # Convert
        convert_nb2script(notebook_path, outfile_path)

convert_wrapper('pyspedas_examples/notebooks/', 'pyspedas_examples/notebooks/scripts/')
