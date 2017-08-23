import os
import sys

def get_info(args):
    author = args.author
    title = args.title
    university = "Swinburne University of Technology"
    unit = args.unit_name
    unitcode = args.unit_code
    student = args.student_id
    semester = args.semester

    info = '\\title{{{0}}}'.format(title)

    if args.subtitle:
        info += '\n\\subtitle{{{0}}}'.format(args.subtitle)

    info += '\n\\university{{{0}}}' \
            '\n\\unitcode{{{1}}}' \
            '\n\\unitname{{{2}}}' \
            '\n\\author{{{3}}}' \
            '\n\\studentid{{{4}}}' \
            '\n\\semester{{{5}}}' \
            '\n\\crest{{' \
            '\\includegraphics[width=0.6\\textwidth]{{' \
            'Resources/swin-logo.pdf}}}}'.format(university, unitcode, unit, author,
                                                 student, semester)

    return info


def print_error(msg):
    prog_name = os.path.basename(__file__)
    print('{0}: error: {1}', prog_name, msg)
