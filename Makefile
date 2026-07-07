all: animations presentation

presentation:
	pdflatex -synctex=1 -interaction=nonstopmode --shell-escape main.tex

animations:

