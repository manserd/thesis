all: main.tex
	python3 preprocess.py
	latexmk -outdir=build -pdf -interaction=nonstopmode -halt-on-error main.tex
	cp build/main.pdf .

clean:
	rm -rf build

fresh:
	make clean
	make
