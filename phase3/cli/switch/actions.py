#!/usr/bin/env python3

import typer
import sdk.switch as switch

resource = typer.Typer()

@resource.command(no_args_is_help=True)
def add(
    fabric: str = typer.Argument(..., help="Fabric in which to add switch"),
    role: str = typer.Argument(..., help="Switch role in fabric"),
    name: str = typer.Argument(..., help="Switch name"),
    serial: str = typer.Option(None, help="Switch Serial Number"),
    ip: str = typer.Option(None, help="Switch mgmt0 IP Number")
):
    """
    Add a switch to the specifed fabric with the specified role, identifying
    the switch by its switch name.  Optionally, you can provide the serial
    number or mgmt0 IP in case of duplicate switch names.
    """

    typer.echo(f"Fabric: {fabric}, Switch role: {role}, Switch Name: {name}")
    typer.echo(f"Options: Serial '{serial}', mgmt0 ip '{ip}'")

    # Call the underlying library and retrieve the results
    results = switch.add_switch(fabric, role, name, serial, ip)

    # Output the results in some meaningful way
    pass

@resource.command(no_args_is_help=True)
def list(
    fabric: str = typer.Argument(..., help="Fabric in which to add switch"),
    name: str = typer.Argument(None, help="Switch name"),
):
    """
    List all switches in the given fabric, if no name is given.
    List switch details if a switch name is provided.
    """

    typer.echo(f"Fabric: {fabric}, Switch Name: {name}")

    # Call the underlying library and retrieve the results
    results = switch.list_switch(fabric, name)

    # Output the results in some meaningful way.  One option would display
    # all switches in fabric, second option would display switch details
    pass
