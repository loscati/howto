# Set up Tex environment with VSCode in Manjaro
> Last update: 2023-04-03 15:32:33
> 
> For more recent setup, check out this public repo: https://github.com/loscati/minimal_latex_templates

This is a brief tutorial to install and work with Tex, actually to pdfTex (engine), LaTex (macros) and Biber (bibliography engine).

An introduction to Tex and [all its flavours](https://www.overleaf.com/learn/latex/Articles/What's_in_a_Name:_A_Guide_to_the_Many_Flavours_of_TeX) together with an [introduction to BibLaTex](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX) is important to understand what is happening under the hood, and thus better debug hopefully-not-so-many errors. Also [this stack exchange post](https://tex.stackexchange.com/questions/13509/biblatex-in-a-nutshell-for-beginners/13513) is useful to understand Biber as well as its [documentation](https://ctan.mirror.garr.it/mirrors/ctan/macros/latex/contrib/biblatex/doc/biblatex.pdf) for styles etc.

## Install Tex Live

We need to install a distribution which collect all the necessary tools (engines, macros etc.) to build files.
We'll use Tex Live which [in Manjaro](https://wiki.archlinux.org/index.php/TeX_Live#Installation) is contained in the `texlive-most` package. Biber, needed to use bibLaTex, is contained in a separate package named, not surprisingly, `biber`.

```bash
sudo pacman -Syu texlive-most biber
```

Watch out for all the `perl` packages required by `biber`, they can break in some unpleasant way.


## Install VSCode and its extensions

In the Manjaro repo, VSCode is called `code`

```bash
sudo pacman -Syu code
```

Open VSCode and install the extension required to work with Tex code. Use the shortcut `crtl + P` and install [`LaTex Workshop`](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) using the command:
```
ext install James-Yu.latex-workshop
```

### Option to set
WIP

## Some useful info about working with Tex in VSCode
+ **SyncTex**: to jump from source to pdf (when using an internal pdf viewer) select the text and use the shortcut `ctrl + alt + j`. Viceversa, by clicking at a specific point in the pdf while holding down `ctrl`, the software finds the relative part in the source code.
+ **Clean extra files**: shortcut `ctrl + alt + c` remove extra files produced by compilation
+ **latexmk**: software, written in perl, which installs together with Tex Live. It is automatically used by the Latex Workshop extension to chose how to build the document. For example if we have a bibliography to compile with Biber, latexmk does the following: run pdfTex, then Biber and pdfTex again as it should be.  
+ The extension can automatically format the document, if you want you can set the automatic formatting onSave

### Troubleshooting
- If the formatting does not work because `stderr: Can't locate YAML/Tiny.pm in @INC (you may need to install the YAML::Tiny module)`, then you have to install the perl modules required by using `cpan YAML::Tiny module`. This has to be done for all modules required. Tip: check `output > Latex Workshop` for hints about this problem, or call the `latexindent` program from terminal.

## Test and MWE
The Minimal Working Example (MWE) is the following

```tex
\documentclass{article}
    % General document formatting
    \usepackage[margin=0.7in]{geometry}
    \usepackage[parfill]{parskip}
    \usepackage[utf8]{inputenc}
    
    % Related to math
    \usepackage{amsmath,amssymb,amsfonts,amsthm} 

    \usepackage{biblatex}
    \addbibresource{biblio.bib}

\begin{document}

Name, date, Exercise X

\section*{Part a}

Citing \cite{clementi2000jomb}

\section*{Part b}

etc

\printbibliography

\end{document}
```

with a `biblio.bib` file as follow:

```bibtex
@article{clementi2000jomb,
  title = {Topological and Energetic Factors: What Determines the Structural Details of the Transition State Ensemble and ``En-Route'' Intermediates for Protein Folding? An Investigation for Small Globular Proteins},
  shorttitle = {Topological and Energetic Factors},
  author = {Clementi, Cecilia and Nymeyer, Hugh and Onuchic, Jos{\'e} Nelson},
  year = {2000},
  month = may,
  volume = {298},
  pages = {937--953},
  doi = {10.1006/jmbi.2000.3693},
  journal = {Journal of Molecular Biology},
  number = {5}
}
```

