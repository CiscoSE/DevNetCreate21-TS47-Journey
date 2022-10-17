# Library Developer Experience (phase3)

This directory includes some of the highlights from this section of
the talk, specifically the experience I required from the underlying
SDK as I was developing the library.

The sample code in this directory highlights some of the architecture
decisions that resulted from those perspectives. 

## Goals

Insulate library from API changes

Well defined classes for specific resources
- Interfaces, Switches, Fabrics

Product deploys a lot of state via generic templates/policies
- Need robust class to handle that broad class of functionality
- Need to have general template class that can then be specialized
- Need policy instantiation functionality

## Technology Outcomes

Template/Policy Class
- Polymorphism will abound
- Class methods to extract/Leverage inherent defaults in template

Abstraction layer for API calls that are version dependent
- Some more polymorphism tricks
- Separation of models/methods from API calls

Directory Structure
- cli/**resource**/action.py
- sdk/**resource**/list_switch.py
- api/rest/...
- api/models...
