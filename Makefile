dataset:
	@python create-data.py


pt:
	@python app.py pt

pt-p:
	pandoc -i output/pt.html --template=templates/default.latex --latex-engine=xelatex -o output/pt.pdf


qu:
	@python app.py qu

qu-p:
	pandoc -i output/qu.html --template=templates/default.latex --latex-engine=xelatex -o output/qu.pdf

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

