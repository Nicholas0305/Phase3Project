#!/usr/bin/env python3
from planets import planet
from stars import Star
from big_round_thing import big_round_thing
import click

@click.command()
def create_a_planet():
    click.echo('Hello World!')

if __name__ == "__main__":
    hello()