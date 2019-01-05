import glob
import pathlib
import cairosvg

imgs=glob.glob('svg/*.svg')
print(imgs)
for f in imgs:
    # print(f)
    # print(pathlib.Path(f).stem)
    # print(pathlib.Path(f).suffix)
    outfile=f'png/{pathlib.Path(f).stem}.png'
    cairosvg.svg2png(url=f, write_to=outfile, scale=4)