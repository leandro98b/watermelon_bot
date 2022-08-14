#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Libraries
import os
import requests
import click

# Variables
URL_TRANSFERSH = 'https://transfer.sh'

def transfersh(filename):
    """ Program that uploads a file to Transfer.sh """
    try:
        # Open file
        with open(filename, 'rb') as data:
            click.echo('Uploading file')
            # Upload file
            conf_file = {filename: data}
            headers = {}
            r = requests.post(URL_TRANSFERSH, files=conf_file, headers=headers)
            # Shows route to download
            download_url = r.text
            print(download_url)
    except Exception:
        click.echo('Something has failed. The file could not be uploaded.')