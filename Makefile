all: main.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error -pdflatex="pdflatex -shell-escape %O %S" main.tex

clean:
	git clean -fdX
