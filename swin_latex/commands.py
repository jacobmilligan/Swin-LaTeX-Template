import os
import shutil
import re
import sys

from swin_latex.settings import dirs, template_path, gitignore
from swin_latex.util import print_error


def initialize_project(args):
    cwd = os.getcwd()
    this_tmpl = template_path
    if args.type == 'problem-set':
        this_tmpl = os.path.join(this_tmpl, 'problem_set')
    else:
        this_tmpl = os.path.join(this_tmpl, 'paper')

    for d in dirs:
        path = os.path.join(this_tmpl, d)
        out_path = os.path.join(cwd, d)
        if os.path.exists(out_path):
            if args.overwrite:
                shutil.rmtree(out_path)
                shutil.copytree(path, out_path)
        else:
            shutil.copytree(path, out_path)

    shutil.copy(os.path.join(this_tmpl, 'unipaper.cls'), cwd)
    shutil.copy(os.path.join(this_tmpl, 'paper.sublime-project'), cwd)
    shutil.copy(os.path.join(this_tmpl, 'info.tex'), cwd)

    if args.gitignore:
        path = os.path.join(cwd, '.gitignore')
        with open(path, 'w+') as file:
            file.write('\n'.join(gitignore))

    if args.bibtex:
        try:
            open(os.path.join(cwd, 'ref.bib'), 'r')
        except:
            open(os.path.join(cwd, 'ref.bib'), 'w+')

    with open(os.path.join(this_tmpl, 'paper.tex'), 'r') as paper:
        paper_tex = paper.read().splitlines()

    with open(os.path.join(cwd, 'paper.tex'), 'w') as paper:
        for line in paper_tex:
            if '\input{Content/abstract}' in line:
                if args.abstract:
                    paper.write('\\thispagestyle{empty}\n')
                    paper.write(line + '\n')
                    paper.write('\clearpage\n')
            elif '\input{Content/acknowledgements}' in line:
                if args.acknowledgements:
                    paper.write(line + '\n')
                    paper.write('\clearpage\n')
            else:
                paper.write(line + '\n')

    if not args.abstract:
        abstract_path = os.path.join(os.path.join(os.getcwd(), 'Content'), 'abstract.tex')
        os.remove(abstract_path)

    if not args.acknowledgements:
        abstract_path = os.path.join(os.path.join(os.getcwd(), 'Content'), 'acknowledgements.tex')
        os.remove(abstract_path)


def create_section(args):
    name = args.name.lower()
    name = re.sub('[!@#$%^&*()[]{};:,./<>?\|`~-=+]', '_', name)
    name = name.replace(' ', '_')
    cwd = os.getcwd()

    if os.path.exists(os.path.join(cwd, 'unipaper.cls')):
        path = os.path.join(cwd, 'Content')
        path = os.path.join(path, 'Sections')
        try:
            open(os.path.join(path, '{0}.tex'.format(name)), 'r')
        except:
            file = open(os.path.join(path, '{0}.tex'.format(name)), 'w+')
            contents = '\\section{{{0}}} % (fold)\n' \
                        '\\label{{sec:{1}}}\n\n' \
                        '% section {1} (end)\n'.format(args.name, name)
            file.write(contents)
    else:
        print_error('Must be at project root to create new file')
