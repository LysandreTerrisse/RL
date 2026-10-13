import nbformat

name = "DDPG"
nb = nbformat.read(name + ".ipynb", as_version=4)
clean = nbformat.v4.new_notebook()

for cell in nb.cells:
    if cell.cell_type == "code":
        clean.cells.append(nbformat.v4.new_code_cell(
            source=cell.source
        ))
    elif cell.cell_type == "markdown":
        clean.cells.append(nbformat.v4.new_markdown_cell(
            source=cell.source
        ))

nbformat.write(clean, name + "_clean.ipynb")