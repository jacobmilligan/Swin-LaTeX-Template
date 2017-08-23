import os

dirs = ('Content', 'Resources', 'Structure')
template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                             'template')
gitignore = ['.DS_Store',
             'tex_build/',
             '_minted-*']