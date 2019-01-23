sandeng:
	@python app.py sandeng
	pandoc -i output/sandeng.html --template=templates/default.latex --latex-engine=xelatex -o output/sandeng.pdf

uvulars:
	@python app.py uvulars
	pandoc -i output/uvulars.html --template=templates/default.latex --latex-engine=xelatex -o output/uvulars.pdf


kl:
	@python app.py kl
	pandoc -i output/kl.html --template=templates/default.latex --latex-engine=xelatex -o output/kl.pdf

all: sandeng uvulars kl

