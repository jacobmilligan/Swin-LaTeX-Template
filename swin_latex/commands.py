import os
import shutil
import re
import sys

from swin_latex.settings import dirs, template_path, gitignore
from swin_latex.util import get_info, print_error


def initialize_project(args):
    cwd = os.getcwd()
    for d in dirs:
        path = os.path.join(template_path, d)
        out_path = os.path.join(cwd, d)
        if os.path.exists(out_path):
            if args.overwrite:
                shutil.rmtree(out_path)
                shutil.copytree(path, out_path)
        else:
            shutil.copytree(path, out_path)

    shutil.copy(os.path.join(template_path, 'paper.tex'), cwd)
    shutil.copy(os.path.join(template_path, 'unipaper.cls'), cwd)
    shutil.copy(os.path.join(template_path, 'paper.sublime-project'), cwd)

    if args.gitignore:
        path = os.path.join(cwd, '.gitignore')
        with open(path, 'w+') as file:
            file.write('\n'.join(gitignore))

    if args.bibtex:
        try:
            open(os.path.join(cwd, 'ref.bib'), 'r')
        except:
            open(os.path.join(cwd, 'ref.bib'), 'w+')

    info = get_info(args)
    with open(os.path.join(cwd, 'info.tex'), 'w+') as file:
        file.write(info)


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
