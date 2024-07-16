from mylib.bot import scrape


import click

@click.command()
@click.option('--name',
              help='The web page we wanna scrape.')

def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}", bg = 'red',fg='blue'))

if __name__ == '__main__':
    cli()



