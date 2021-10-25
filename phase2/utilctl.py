#!/usr/bin/env python3

import typer
from cli.switch import switch
from cli.interface import interface

utilctl = typer.Typer(no_args_is_help=True)
utilctl.add_typer(switch, name='switch', no_args_is_help=True)
utilctl.add_typer(interface, name='interface', no_args_is_help=True)

if __name__ == '__main__':
    utilctl()
