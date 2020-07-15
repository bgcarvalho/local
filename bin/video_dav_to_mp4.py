#!/usr/bin/env python
"""
Use FFMPEG to convert DAV video files to MP4.
This script walks recursevily into a directory.
"""
import os
import sys
import click
import string
import re
from subprocess import run


@click.command()
@click.argument("path")
@click.option("--codec", default="libx265", help="Video codec")
@click.option(
    "--ffmpegbin",
    default=None,
    help="Path to FFMPEG binary, in case you want to use a different one",
)
def convert(path, codec, ffmpegbin):
    """
    """
    pattern = re.compile(r"[\W_]+")
    if ffmpegbin is None:
        ffmpegbin = "ffmpeg"
    for root, dirs, files in os.walk(path):
        for f in files:
            if ".dav" in f:
                out = pattern.sub("", f[:-4]) + ".mp4"
                print("Converting")
                print(f)
                print(out)
                cp = run(
                    [
                        ffmpeg,
                        "-y",
                        "-i",
                        infile,
                        "-vcodec",
                        "libx265",
                        "-crf",
                        "24",
                        out,
                    ]
                )
                if cp.returncode == 0:
                    print("success")
                else:
                    print("error")
                print("")
        for d in dirs:
            convert(d, codec, ffmpegbin)


if __name__ == "__main__":
    convert()
