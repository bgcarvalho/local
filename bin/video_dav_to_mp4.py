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
        print(root)
        for f in files:
            if ".dav" in f:
                infile = os.path.join(root, f)
                out = pattern.sub("", f[:-4]) + ".mp4"
                #out = out[:6] + '-' + out[6:12] + '_' + out[12:] + '.mp4'
                out = out[:6] + '-' + out[6:12] + '.mp4'
                out = os.path.join(root, out)
                print("Converting")
                print('  From', infile)
                print('  To  ', out)
                cp = run(
                    [
                        ffmpegbin,
                        "-y",
                        "-i",
                        infile,
                        "-vcodec",
                        "libx265",
                        "-crf",
                        "24",
                        out,
                    ],
                    capture_output=True,
                    encoding='utf8',
                )
                if cp.returncode == 0:
                    print("  ..success!")
                else:
                    print("Error:")
                    print(cp.stderr)
                print("")
        for d in dirs:
            convert(d, codec, ffmpegbin)


if __name__ == "__main__":
    convert()
