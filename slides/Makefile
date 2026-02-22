TEX_FILE_NAME := bisection_method
TIKZ_FIGURES_DIR := figures
LATEX_ENGINE := lualatex
ENGINE_ARGS := -synctex=1 -interaction=nonstopmode

.PHONY: build clean watch

build: $(TEX_FILE_NAME).pdf

$(TEX_FILE_NAME).pdf: ./$(TIKZ_FIGURES_DIR)/$(TEX_FILE_NAME)%.pdf
	$(LATEX_ENGINE) $(ENGINE_ARGS) ./$(TEX_FILE_NAME).tex

./figures/%.md5:
	$(LATEX_ENGINE) $(ENGINE_ARGS) ./$(TEX_FILE_NAME).tex

./$(TIKZ_FIGURES_DIR)/%.pdf: ./$(TIKZ_FIGURES_DIR)/%.md5
	make -j -f ./$(TEX_FILE_NAME).makefile

watch:
	nodemon -w ./$(TEX_FILE_NAME).tex -x "make -j"

clean:
	latexmk -C
	rm -r ./$(TIKZ_FIGURES_DIR)

-include bisection_method.makefile
