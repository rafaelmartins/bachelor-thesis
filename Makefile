# Makefile for build my bachelor thesis, using LaTeX/ABNTeX
# 
# Released under the BSD License:
# http://www.opensource.org/licenses/bsd-license.php

MAIN = monografia

TEX_FILES = \
	$(MAIN) \
	aprovacao \
	resumo \
	abstract \
	agradecimentos \
	dedicatoria \
	acronimos \
	cap1-introducao \
	cap2-processos_referenciais \
	cap3-metodos_de_identificacao_e_sintonia \
	cap4-software \
	cap5-conclusoes \
	anexo1-metodos_numericos \
	anexo2-modelagem_uml


.PHONY: all
all: $(MAIN).pdf

.PHONY: clean
clean:
	$(RM) *.{aux,bbl,blg,dvi,lof,log,lot,pdf,toc}

$(MAIN).pdf: $(addsuffix .tex, $(TEX_FILES))
	latex $(MAIN)
	latex $(MAIN)
	$(MAKE) $(MAIN).bbl
	latex $(MAIN)
	dvipdf $(MAIN)

$(MAIN).bbl: $(MAIN).bib $(addsuffix .aux, $(TEX_FILES))
	bibtex $(MAIN) || [[ -f $(MAIN).bbl ]]
