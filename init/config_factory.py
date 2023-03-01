#!/usr/bin/python3

import os
from typing import IO

import click


@click.command()
@click.argument('template', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=False))
def config_factory(template, output):
    print("Reading template ${template} ...")
    read_file: IO = open(template, mode='r')
    content: str = read_file.read()
    read_file.close()

    for name, value in os.environ.items():
        if name.startswith('TF_VAR_'):
            content = content.replace('${' + name + '}', value)
            content = content.replace('$' + name + '', value)

    print("Writing output file ${output} ...")
    write_file: IO = open(output, "w")
    write_file.write(content)
    write_file.close()


if __name__ == '__main__':
    print("Config factory 0.1")
    config_factory()
