PDFLATEX_ARGS=-synctex=1 -interaction=nonstopmode --shell-escape
MANIM_ANIMATIONS=ThreePar FourPar

all: animations presentation nopause

presentation: main.tex assets/ThreePar.gif assets/FourPar.gif
	pdflatex $(PDFLATEX_ARGS) main.tex

nopause: main.tex assets/ThreePar.gif assets/FourPar.gif
	sed 's/\\pause//' main.tex > nopause.tex 
	pdflatex $(PDFLATEX_ARGS) nopause.tex
	rm nopause.tex

animations: distributions.py ammonites.py
	manim -a distributions.py
	for animation in $(MANIM_ANIMATIONS); do \
		mkdir -p assets/$$animation; \
		ffmpeg -y -i media/videos/distributions/1080p15/$$animation.mp4 assets/$$animation.gif; \
		magick assets/$$animation.gif +adjoin -coalesce assets/$$animation/%03d.png; \
	done
	manim -a ammonites.py
	cp media/images/ammonites/Ammonites_ManimCE_v0.20.1.png assets/ammonite_stratinterval.png

clean:
	rm -f *.aux \
		*.log \
		*.nav \
		*.out \
		*.pdf \
		*.snm \
		*.toc \
		*.synctex.gz
