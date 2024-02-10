# Dashboard Application with Prototype Design Pattern

This Python project implements a dashboard application utilizing the Prototype design pattern. The application enables users to create, configure, and duplicate widgets within a customizable interface.

## Overview

A dashboard application provides users with a platform to monitor various metrics or data points. Widgets are fundamental components of such applications, responsible for displaying data. Often, users need to replicate widgets with similar configurations across different parts of the dashboard. The Prototype design pattern facilitates this process by allowing the creation of new objects through copying an existing object (prototype), simplifying the creation of similar objects.

## Components

- `widget.py`: Contains the implementation of the Widget prototype and the WidgetFactory class responsible for managing widget prototypes and creating new widgets by cloning the prototypes.

## Implementation Details

The `Widget` class defines the interface for creating new widgets. It contains a method `clone()` which creates a deep copy of the widget, enabling independent instances to be created.

The `WidgetFactory` class manages a collection of widget prototypes and provides methods to register new prototypes and create widgets by cloning the registered prototypes.

## Usage

To use this application, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Run the main script to see the demonstration.

