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
