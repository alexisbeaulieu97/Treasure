from pathlib import Path
import sys
import os
import click
from click.decorators import pass_context
from utils import data


@click.group()
@click.option('--input', '-i', type=click.Path(exists=True), default=None, show_default=True, help='input file/directory path')
@click.option('--output', '-o', type=click.Path(), default=None, help='output file/directory path')
@click.pass_context
def cli(ctx, input, output):
    ctx.obj['input'] = input
    ctx.obj['output'] = output
    check_args(ctx.obj)


@cli.command()
@click.pass_context
def lock(ctx):
    """ Encrypt content """
    i = ctx.obj['input'] or sys.stdin.buffer

    click.echo(i.read().rstrip(b'\r\n'))


@cli.command()
@click.pass_context
def unlock(ctx):
    """ Decrypt content """
    click.echo()


def check_args(args):
    # check if args.input or stdin is not empty
    if args['input'] is sys.stdin.buffer and input.isatty():
        raise Exception('stdin is empty')


if __name__ == '__main__':
    cli(obj={})
