# -*- coding: utf-8 -*-
import click
import cliaes
import time
from lib import aes
from lib import func
from tqdm import tqdm

@click.command()
@click.option(
    '--src_file',
    type = click.File(mode='r'),
    help='File in which there is the text you want to encrypt/decrypt.'
)
@click.option(
    '--dist_file',
    type=click.File('w'),
    help='File in which the encrypted / decrypted text will be written.'
)
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    help='Whether you want to encrypt the input text or decrypt it.'
)
@click.option(
    '--key',
    '-k',
    type = click.STRING,
    prompt="\033[31m\033[01m\n>>> Enter your secret KEY 🔑 \033[0m",
    hide_input=True,
    help='The key to use for the AES encryption / decryption.'
)

def AES(src_file, dist_file, encrypt, key):

    obj = aes.PrpCrypt(key)

    if src_file and dist_file:
        text = src_file.read()
        sizeFile = func.file_size(src_file.name)

        try:
            click.secho(message="\n⌛  Wait until the process is complete\n")
            for i in tqdm(range(sizeFile), desc='\033[93mprocess'):
                time.sleep(0.001)
            if encrypt:
                eTextFile = dist_file.write(obj.encrypt(text))
                click.secho(message="\n✔️  \033[32mThe process encryption is complete")
            else:
                dTextFile = dist_file.write(obj.decrypt(text))
                click.secho(message="\n✔️  \033[32mThe process decryption is complete")
            print("\n💯 See the file :\033[01m\033[36m {}\033[0m".format(dist_file.name))
        except:
            click.secho(message='\n⚡ Please Enter encrypt or decrypt option', bg="red", bold=True)
    else:
        try:
            if encrypt:
                text = click.prompt('\033[93m\033[01m>>> Enter a text \033[0m')
                e = obj.encrypt(text)
                click.secho(message="\n🔒 encrypted text : " , fg="green", bold=True)
                click.echo(e)
                click.echo()
            else:
                cipthertext = click.prompt('\033[93m\033[01m>>> Enter a cipher text \033[0m')
                d = obj.decrypt(cipthertext)
                click.secho(message="\n🔓 decrypted text : " , fg="green", bold=True)
                click.echo(d)
                click.echo()
        except:
            click.secho(message='\n⚡ Please Enter encrypt or decrypt option', bg="red", bold=True)

if __name__ == '__main__':
    AES()
