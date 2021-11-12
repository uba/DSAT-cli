# DSAT-cli
A command-line implementation of the DSAT/INPE tool in Python.
This tool downloads images and products taken by the GOES-16 satellite, processed by National Institute for Space Research ([INPE](www.inpe.br))
and creates animations/GIFs from those images. See an example below.

[DSAT](www.cptec.inpe.br/dsat) is the INPE's GOES-16 satellite image viewer application. Visit www.cptec.inpe.br/dsat 🌎🛰️

**Note:** DSAT-cli implementation is inspired by https://github.com/colinmcintosh/SLIDER-cli and [@colinmcintosh](https://github.com/colinmcintosh).

### Motivation

This tool is meant to replicate most of the features of DSAT and includes some additional
flexibility in configuration options. The goal of this utility is to resolve some common issues with
the DSAT web interface, specifically:

- Missing tiles / tiles not being rendered on animation export
- Slow to generate animations
- Web browser may crash for complex animations
- Limited options for features like time-step and speed

## Example Usage

```bash
# Donwload single image (2021/11/12 - 12:00 UTC) Full-disk at level 2
dsat-cli.py -p true_color_ch13_dsa -d 202111121200 -i 1 -l 2 -o full-disk.png
```
<img src="examples/full-disk.png" width="400px"/>

```bash
# Donwload animation (Start 2021/11/12 - 12:00 UTC + 17 images, step 10 min) Brazil at level 4
dsat-cli.py -p true_color_ch13_dsa -d 202111121200 -i 18 -l 4 --tiles-extent 5 4 9 8 -o brazil-l4-anim.gif
```
<img src="examples/brazil-l4-anim.gif" width="300px"/>

```bash
# Donwload animation (Start 2021/11/12 - 12:00 UTC + 17 images, step 10 min) Fortaleza - CE at level 6
dsat-cli.py -p true_color_ch13_dsa -d 202111121200 -i 18 -l 6 --tiles-extent 34 22 35 23 -o fortaleza-l4-anim.gif
```
<img src="examples/fortaleza-l6-anim.gif" width="300px"/>

```bash
# Donwload animation (Start 2021/11/12 - 12:00 UTC + 17 images, step 10 min) Brasília - DF at level 7
dsat-cli.py -p ch02 -d 202111091200 -i 18 -l 7 --tiles-extent 63 55 63 55 -o brasilia-l7-anim.gif
```
<img src="examples/brasilia-l7-anim.gif" width="300px"/>
