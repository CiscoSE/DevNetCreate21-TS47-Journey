# User Experience (phase1)

This directory includes some of the highlights from this section of
the talk, specifically the experience I was hoping to provide. Those
experience requirements naturally translated into some technology
decisions.  The sample code in this directory showcases the results.

## Goals

A *kubectl* style command of the form:
- utilctl **command** [**subcommand**] *arguments --options*

What we will do
- Focus on a CLI analogs to common GUI actions

What we won’t do
- Generic inputs: this is not a CLI replacement for OpenAPI GUI or Postman

Leverage existing default values if not provided
- Don’t want a 30-page command line

## Technology Outcomes

Python Command Line Parsing Candidates
- [docopt](http://docopt.org)
- [click](https://click.palletsprojects.com/en/8.0.x/)
- [Typer](https://typer.tiangolo.com)

Directory Structure
- cli/**resource**/action.py

Provided guidance to separate CLI/UI from the complex logic around the
service I am consuming.
