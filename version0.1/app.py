import click
from lib import aes

@click.command()
@click.argument('text', nargs=-1)
@click.option('--encrypt/--decrypt', '-e/-d')
@click.option('--key', '-k', default=1, type = click.STRING)
def AES(text, key, encrypt):

    import cliaes
    text_string = ' '.join(text)
    obj = aes.PrpCrypt(key)
    if encrypt:
        e = obj.encrypt(text_string)
        click.secho(message=">>> encrypted text : " , fg="red", bold=True)
        click.echo(e)
    else:

        d = obj.decrypt(text_string)
        click.secho(message=">>> decrypted text : " , fg="red", bold=True)
        click.echo(d)

if __name__ == '__main__':
    AES()
