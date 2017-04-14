# Swinburne University LaTeX Template

An LaTeX/XeLaTeX template intended for use in Swinburne University papers.

## Requirements

* [Sublime Text](https://www.sublimetext.com/)
* The [LaTeXTools plugin](https://github.com/SublimeText/LaTeXTools) for Sublime 
Text
* Python3 (for using the CLI tool)

## Getting Started

Clone the repo

```bash
$ git clone https://github.com/jacobmilligan/Swin-LaTeX-Template
```

Then add the project directory to your `PATH` variable.

## Usage

### Initializing a new project
Create a new project in the current directory using the build script:

```bash
$ swin-latex-template init --author="My name" --title="Assignment title" \
--unit-code=CODEXXX --unit-name="Unit name" --student-id=0000000000 --semester=1 \ 
--subtitle="Subtitle"
```

Of the above arguments, only `--subtitle` is optional. The following options are also 
supported:

* `-o, --overwrite` - Overwrites existing files and folders if a project already exists
* `-g, --gitignore` - Creates a LaTeX .gitignore file in the project root
* `-b, --bibtex` - Creates a blank bibtex bibliography file in the project root

This will generate a new project in the current directory with the following structure:

```
project
├── Content
│   ├── Sections
│   │   ├── section_a.tex
│   │   ├── section_b.tex
│   │   └── section_c.tex
│   ├── abstract.tex
│   ├── acknowledgements.tex
│   ├── appendix.tex
│   └── body.tex
├── Resources
│   ├── swin-logo-bw.pdf
│   └── swin-logo.pdf
├── Structure
│   └── preamble.tex
├── .gitignore (--gitignore option)
├── info.tex
├── paper.tex
├── ref.bib (--bibtex option)
└── unipaper.cls
```

* `info.tex` - All info for the project such as author name, title etc. is pulled in 
from this file and can be changed
* `paper.tex` - The core structure of the paper - you don't need to alter this
* `unipaper.cls` - The `swin-latex-template` document class
* `/Content`:
  * `/Sections` - All sections exist in here, with some sample sections added for a 
  generated project
  * `abstract.tex` - The abstract
  * `acknowledgements.tex` - Any acknowledgements, resource mentions etc.
  * `appendix.tex` - All appendices should be specified here
  * `body.tex` - This is the structure of the **body** part of the document and should 
  only really be for `\input{}`ing sections and some formatting
* `/Resources` - Images used by the standard generated template, all other images and 
asset files should go in this directory
* `/Structure/preamble.tex` - The preamble of the document where all definitions, 
macros, and `\usepackage{}` should be specified

### Generating files

New sections can be created from the project root directory (the one with the `unipaper
.cls` file) via the CLI tool by executing:
```bash
$ swin-latex-template new-section <section-name>
```

This will create a blank section file under `Content/Sections/<section_name>` with the 
following content:

```latex
% !TEX root = ../../paper.tex

\section{Section Name} % (fold)
\label{sec:section_name}

% section section_name (end)
```

It's important to note that the first line is important for getting autocomplete and 
finding any imported files in `LaTeXTools`