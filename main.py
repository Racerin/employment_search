import lib

import click

@click.group()
def cli():
    pass

@cli.command()
# @click.argument(def=)
@click.argument('keyword')
def search(keyword):
    # lib.gen_read_ministry_url()
    lib.search_spreadsheet_for_job(keyword)

if __name__ == "__main__":
    cli()