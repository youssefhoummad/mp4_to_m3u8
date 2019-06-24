#!/usr/bin/env python3
#
# Copyright 2019 youssef hoummad (youssef.hoummad@outlook.com)
#

import os
from pathlib import WindowsPath
import subprocess


def mp4_to_m3u8(src, dst, resolution="SD", output_file_name=None):
    """
    convert file .mp4 to file .m3u8

    src         : path of mp4 file
    dst         : path of m3u8 list
    resulution  : SD / HD / FHD

    NB: name of file m3u8 generate automatique.
    """

    resolutions = {'SD':'720:576', 'HD':'1280:720', 'FHD':'1920:1080'}
    dimension = resolutions.get(resolution, 'SD')

    file_name = generate_file_name(file_name=output_file_name, resolution=resolution)
    dst = create_dir(dst, resolution)
    full_dst = set_path(dst, file_name)
    
    src = fix_whitespace_in_path(src)
    full_dst = fix_whitespace_in_path(full_dst)

    return os.system(f"ffmpeg -i {src} -vf scale={dimension} -bsf:v h264_mp4toannexb -hls_list_size 0 {full_dst}")

def generate_file_name(file_name="playlist", resolution="SD", extention="m3u8"):
    """ return file name with resulotion
    ex: generate_file_name('output', 'HD')
        >> 'output_HD.m3u8
    """
    if file_name is None: file_name="playlist"
    if extention is None: extention="m3u8"
    
    return f"{file_name}_{resolution}.m3u8"


def create_dir(path, dir_name):
    """Creating a Directory in Specific Path if not exists.
        ex: create_dir('c:\\', 'temp')
        create a folder in c:\\ with name <temp>
        >> 'c:\\temp'
    """
    full_path = os.path.join(path, dir_name)
    try:
        os.mkdir(full_path)
    except:
        pass
    return full_path


def set_path(path, file_name):
    return os.path.join(path, file_name)


def fix_whitespace_in_path(path):
    "fix whitespace path on windows"
    if os.name == 'nt': #if run prog on Windows
        return '\"' + path + '\"' # envlop path by two ""
    return path


if __name__ == "__main__":
    src = input("path of video: ")
    dst = input("path to save: ")
    if dst == "": dst = src
    mp4_to_m3u8(src, dst, output_file_name='File')
    print("file converted!")
