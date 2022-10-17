#!/usr/bin/env python3

import typer
import sdk.interface as interface

resource = typer.Typer()

@resource.command(no_args_is_help=True)
def add(
    switch: str = typer.Argument(..., help="Switch name"),
    intf_name: str = typer.Argument(..., help="Interface name"),
):
    """
    Add the specified logical interface (loopback, SVI, VPC, Portchannel, etc)
    to the specified switch.
    """

    typer.echo(f"Interface: {intf_name}, Switch Name: {switch}")
    
    # Call the underlying library and retrieve the results
    results = interface.add_interface(switch, intf_name)

    # Output the results in some meaningful way
    pass

@resource.command(no_args_is_help=True)
def list(
    switch: str = typer.Argument(..., help="Switch name"),
    intf_name: str = typer.Argument(None, help="Interface name")
):
    """
    List all interfaces on a given switch, if no interface is given.
    List interface details if an interface name is provided.
    """

    typer.echo(f"Interface: {intf_name}, Switch Name: {switch}")

    # Call the underlying library to generate the interface data
    results = interface.list_interface(switch, intf_name)

    # Output the results in some meaningful way, need one option
    # for all interfaces, secoond option for interface details
    pass
