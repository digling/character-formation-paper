dataset:
	@python create-data.py

sandeng:
	@python app.py sandeng

sandeng-p:
	pandoc -i output/sandeng.html --template=templates/default.latex --latex-engine=xelatex -o output/sandeng.pdf

uvulars:
	@python app.py uvulars

uvulars-p:
	pandoc -i output/uvulars.html --template=templates/default.latex --latex-engine=xelatex -o output/uvulars.pdf


kl:
	@python app.py kl

kl-p:
	pandoc -i output/kl.html --template=templates/default.latex --latex-engine=xelatex -o output/kl.pdf

all: data sandeng uvulars kl
all-p: sandeng-p uvulars-p kl-p

