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
	anexo2-documentacao_da_api

SCRIPTS = \
	cap2.py \
	cap3.py \
	cap4.py

IMAGES_PNG = \
	cefet \
	cap4-pidsim_home \
	cap4-pacotes \
	cap4-model5-inicio \
	cap4-model5-valores \
	cap4-model5-valores_manual


.PHONY: all
all: $(MAIN).pdf

.PHONY: clean
clean:
	$(RM) *.{aux,bbl,blg,dvi,lof,log,lot,pdf,toc}

.PHONY: view
view: all
	evince $(MAIN).pdf

$(MAIN).pdf: $(addsuffix .tex, $(TEX_FILES)) cefet.cls $(MAIN).bib
	latex $(MAIN)
	latex $(MAIN)
	$(MAKE) $(MAIN).bbl
	latex $(MAIN)
	latex $(MAIN)
	dvipdf $(MAIN)

$(MAIN).bbl: $(MAIN).bib $(addsuffix .aux, $(TEX_FILES))
	bibtex $(MAIN) || [[ -f $(MAIN).bbl ]]

imagens/%.eps: imagens_raw/%.png
	convert $< $@

.PHONY: all_images
all_images: $(addsuffix .eps, $(addprefix imagens/, $(IMAGES_PNG)))

.PHONY: images
images:
	for i in $(SCRIPTS); do python scripts/$${i}; done
	touch $(MAIN).tex
	$(MAKE) all


