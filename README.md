# DSAT-cli
A command-line implementation of the DSAT/INPE tool in Python.
This tool downloads images and products taken by the GOES-16 satellite, processed by National Institute for Space Research ([INPE](http://www.inpe.br))
and creates animations/GIFs from those images. See an example below.

[DSAT](http://www.cptec.inpe.br/dsat) is the INPE's GOES-16 satellite image viewer application. Visit www.cptec.inpe.br/dsat 🌎🛰️

**Note:** DSAT-cli implementation is inspired by https://github.com/colinmcintosh/SLIDER-cli and [@colinmcintosh](https://github.com/colinmcintosh).

### Motivation

This tool is meant to replicate most of the features of DSAT and includes some additional
flexibility in configuration options. The goal of this utility is to resolve some common issues with
the DSAT web interface, specifically:

- Missing tiles / tiles not being rendered on animation export
- Slow to generate animations
- Web browser may crash for complex animations
- Limited options for features like time-step and speed

## Products

Ch01 | Ch02 | Ch03 | Ch04
--- | --- | --- |---
<img src="examples/ch01.png" width="200px"/> | <img src="examples/ch02.png" width="200px"/> | <img src="examples/ch03.png" width="200px"/> | <img src="examples/ch04.png" width="200px"/>

Ch05 | Ch06 | Ch07 | Ch08
--- | --- | --- |---
<img src="examples/ch05.png" width="200px"/> | <img src="examples/ch06.png" width="200px"/> | <img src="examples/ch07.png" width="200px"/> | <img src="examples/ch08.png" width="200px"/>

Ch09 | Ch10 | Ch11 | Ch12
--- | --- | --- |---
<img src="examples/ch09.png" width="200px"/> | <img src="examples/ch10.png" width="200px"/> | <img src="examples/ch11.png" width="200px"/> | <img src="examples/ch12.png" width="200px"/>

Ch13 | Ch14 | Ch15 | Ch16
--- | --- | --- |---
<img src="examples/ch13.png" width="200px"/> | <img src="examples/ch14.png" width="200px"/> | <img src="examples/ch15.png" width="200px"/> | <img src="examples/ch16.png" width="200px"/>

Ch08 (WVCOLOR35) | Ch09 (WVCOLOR35) | Ch10 (WVCOLOR35)
--- | --- | ---
<img src="examples/ch08_cpt_WVCOLOR35.png" width="200px"/> | <img src="examples/ch09_cpt_WVCOLOR35.png" width="200px"/> | <img src="examples/ch10_cpt_WVCOLOR35.png" width="200px"/>

Ch13 (IR4AVHRR6) | Ch13 (DSA)
--- | ---
<img src="examples/ch13_cpt_IR4AVHRR6.png" width="200px"/> | <img src="examples/ch13_cpt_DSA.png" width="200px"/>

Airmass | Ash | Cloud Phase (Eumetsat) | Cloud Phase (JMA)
--- | --- | --- |---
<img src="examples/airmass.png" width="200px"/> | <img src="examples/ash.png" width="200px"/> | <img src="examples/cloud_phase_eumetsat.png" width="200px"/> | <img src="examples/day_cloud_phase_jma.png" width="200px"/>

Convective Storm | Day Snow Fog | Differential WV | Dust
--- | --- | --- |---
<img src="examples/convective_storm.png" width="200px"/> | <img src="examples/day_snow_fog.png" width="200px"/> | <img src="examples/differential_wv.png" width="200px"/> | <img src="examples/dust.png" width="200px"/>

Fire Temperature | Natural Color | Night Microphysics | Simple WV
--- | --- | --- |---
<img src="examples/fire_temperature.png" width="200px"/> | <img src="examples/natural_color.png" width="200px"/> | <img src="examples/night_microphysics.png" width="200px"/> | <img src="examples/simple_wv.png" width="200px"/>

SO2 | True-color + Ch13 (DSA)
--- | --- 
<img src="examples/so2.png" width="200px"/> | <img src="examples/true_color_ch13_dsa.png" width="200px"/>

## Install
Clone the DSAT-Cli Repository:
```
git clone https://github.com/uba/DSAT-cli.git
```
Go to the source code folder:
```
cd DSAT-cli
```
Install:
```
pip3 install -r requirements.txt
```

## Usage
```
dsat-cli.py --help
usage: dsat-cli [-h]
                [--product {ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch08_cpt_WVCOLOR35,ch09_cpt_WVCOLOR35,ch10_cpt_WVCOLOR35,ch13_cpt_IR4AVHRR6,ch13_cpt_DSA,airmass,ash,cloud_phase_eumetsat,day_cloud_phase_jma,convective_storm,day_snow_fog,differential_wv,dust,fire_temperature,natural_color,night_microphysics,simple_wv,so2,true_color_ch13_dsa}]
                [--date DATE] [-i I] [--time-step TIME] [--level {2,3,4,5,6,7}] [--tiles-extent xmin ymin xmax ymax]      
                [--speed SPEED] [--processes PROCESSES] --output OUTPUT [--verbose] [--version]

DSAT-Cli. Copyright (C) 2021-2022 INPE.

optional arguments:
  -h, --help            show this help message and exit
  --product, -p         Product that will be retrieved
  --date DATE, -d DATE  Desired image datetime. Format: YYYYMMDDhhmm
  -i I                  Number of images that will be requested from the given date as start.
  --time-step TIME, -t TIME
                        Interval of image capture times in minutes. (default 10)
  --level {2,3,4,5,6,7}, -l {2,3,4,5,6,7}
                        Level (zoom) that will be retrieved
  --tiles-extent xmin ymin xmax ymax
                        Optional tiles extent
  --speed SPEED         Frame rate, i.e. time between two consecutive frames. Default: 0.5 (in seconds)
  --processes PROCESSES
                        Number of processes to use for image requests. Default: Number of CPUs
  --output OUTPUT, -o OUTPUT
                        Output filename to save resut
  --verbose             Increase output verbosity
  --version, -v         show program's version number and exit
```

**Tip:** You can search *tile-extent* numbers here [Tiles](http://www.cptec.inpe.br/dsat/?tiles=true&options=false).

## Example Usage

```bash
# Download single image (2021/11/12 - 12:00 UTC) Full-disk at level 2
dsat-cli.py -p true_color_ch13_dsa -d 202111121200 -i 1 -l 2 -o full-disk.png
```
<img src="examples/full-disk.png" width="400px"/>

```bash
# Download animation (Start 2021/11/12 - 12:00 UTC + 17 images, step 10 min) Brazil at level 4
dsat-cli.py -p true_color_ch13_dsa -d 202111121200 -i 18 -l 4 --tiles-extent 5 4 9 8 -o brazil-l4-anim.gif
```
<img src="examples/brazil-l4-anim.gif" width="400px"/>

```bash
# Download animation (Start 2021/11/12 - 12:00 UTC + 17 images, step 10 min) Fortaleza - CE at level 6
dsat-cli.py -p true_color_ch13_dsa -d 202111121200 -i 18 -l 6 --tiles-extent 34 22 35 23 -o fortaleza-l4-anim.gif
```
<img src="examples/fortaleza-l6-anim.gif" width="400px"/>

```bash
# Download animation (Start 2021/11/12 - 12:00 UTC + 17 images, step 10 min) Brasília - DF at level 7
dsat-cli.py -p ch02 -d 202111091200 -i 18 -l 7 --tiles-extent 63 55 63 55 -o brasilia-l7-anim.gif
```
<img src="examples/brasilia-l7-anim.gif" width="256px"/>

## License
Copyright (C) 2020-2021 INPE.

DSAT-Cli is free software; you can redistribute it and/or modify it
under the terms of the MIT License; see LICENSE file for more details.
