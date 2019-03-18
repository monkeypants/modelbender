""" modelbender.util

code that I did not want to keep looking at in the main modelender.py script
"""
import os
import os.path
import re
import subprocess

# OS level commands
CMD_DOT = "dot -Tpng {0}.dot -o {0}.png"
CMD_BLOCKDIAG = "blockdiag {}.diag"
CMD_BLOCKDIAG_SVG = "blockdiag -Tsvg {}.diag"
CMD_SEQDIAG = "seqdiag {}.diag"
CMD_SEQDIAG_SVG = "seqdiag {}.diag"
CMD_ACTDIAG = "actdiag {}.diag"
CMD_ACTDIAG_SVG = "actdiag {}.diag"
CMD_NWDIAG = "nwdiag {}.diag"
CMD_NWDIAG_SVG = "nwdiag {}.diag"

# patterns for determining what kind of file it is
# note, these are implicit in the template names used in doc generation
DOT_PATTERN = re.compile('^.*\.dot$')
DIAG_PATTERN = re.compile('^.*\.diag$')
BLOCK_DIAG_PATTERN = re.compile('^.*\_block.diag$')
SEQ_DIAG_PATTERN = re.compile('^.*\_seq.diag$')
ACT_DIAG_PATTERN = re.compile('^.*_act\.diag$')
NW_DIAG_PATTERN = re.compile('^.*_nw\.diag$')


def gen_doc_renderer(indir, outdir):
    """ renders the generated documents

    This is the core of the render cli command.
    It is better than asking the user to render the diagrams themselves,
    because this container will have all the dependencies.

    Assumes:

     * the container has all the OS-level dependencies installed
     * your .diag files are named \*_block.diag, \*_seq.diag,
       \*_act.diag and \*_nw.diag

    Containerisation (and templates) should make those assumptions safe.

    """
    domain_base = os.path.join(indir, 'domains')
    for domain_name in os.listdir(domain_base):
        domain_path = os.path.join(domain_base, domain_name)
        if os.path.isdir(domain_path):
            print("rendering diagrams in {}".format(domain_name))
            for resource_name in os.listdir(domain_path):
                resource_path = os.path.join(domain_path, resource_name)
                if os.path.isfile(resource_path):
                    if DOT_PATTERN.match(resource_name):
                        # print("    TODO: do the DOT thing to {}".format(resource_path))  # NOQA
                        cmds = (DOT_PATTERN,)
                        execute_commands(cmds, resource_name, domain_path)
                    elif DIAG_PATTERN.match(resource_name):
                        # print("    TODO: do one of the DIAG things to {}".format(resource_path)) # NOQA
                        if BLOCK_DIAG_PATTERN.match(resource_name):
                            cmds = (CMD_BLOCKDIAG, CMD_BLOCKDIAG_SVG)
                        elif SEQ_DIAG_PATTERN.match(resource_name):
                            cmds = (CMD_SEQDIAG, CMD_SEQDIAG_SVG)
                        elif ACT_DIAG_PATTERN.match(resource_name):
                            cmds = (CMD_ACTDIAG, CMD_ACTDIAG)
                        elif NW_DIAG_PATTERN.match(resource_name):
                            cmds = (CMD_NWDIAG, CMD_NWDIAG_SVG)
                        else:
                            msg_tmpl = "{} is a diag that does not match our naming convention"
                            msg = msg_tmpl.format(resource_path)
                            raise Exception(msg)
                        execute_commands(cmds, resource_name, domain_path)


def execute_commands(cmds, resource_name, domain_path):
    parts = resource_name.split('.')[:-1]  # ignore suffix
    name_part = parts[0]
    if len(parts) > 1:  # some lout may have put a dot in the name.
        for part in parts[1:]:
            name_part = "{}.{}".format(name_part, part)
    for cmd in cmds:
        # print("cd {}".format(domain_path))
        os.chdir(domain_path)
        # print(cmd.format(name_part))  # DEBUG
        subprocess.run(cmd.format(name_part), shell=True)
