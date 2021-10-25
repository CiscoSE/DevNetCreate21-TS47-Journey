# CLI Developer Experience (phase2)

This directory includes some of the highlights from this section of
the talk, specifically the experience I required from the underlying
libraries as I was developing the CLI.

The sample code in this directory highlights some of the architecture
decisions that resulted from those perspectives. 

## Goals

Keep the option of multiple UIs open ("today" CLI, "tomorrow" Ansible wrappers and web UI).
- Keep the API workflow logic separated from the UI implementation.

```python
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
```

## Technology Outcomes

Library with logical tasks
- list_switch, add_switch

Desire to standardize on Python data structures for data returned to UI
- Will have to document those expected values well in the library

Directory Structure
- cli/**resource**/action.py
- sdk/**resource**/list_switch.py
