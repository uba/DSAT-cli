# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

"""DSAT Products."""

class Product:
    def __init__(self, name, minLevel, maxLevel):
        self.name = name
        self.minLevel = minLevel
        self.maxLevel = maxLevel

class Catalog:
    def __init__(self,):
        self.products = {}
    
    def addProduct(self, p):
        self.products[p.name] = p

    def getProduct(self, name):
        return self.products[name]
        
    def getProducts(self):
        return list(self.products.keys())

Catalog = Catalog()
# Channels
Catalog.addProduct(Product('ch01', 2, 6))
Catalog.addProduct(Product('ch02', 2, 7))
Catalog.addProduct(Product('ch03', 2, 6))
Catalog.addProduct(Product('ch04', 2, 5))
Catalog.addProduct(Product('ch05', 2, 6))
Catalog.addProduct(Product('ch06', 2, 5))
Catalog.addProduct(Product('ch07', 2, 5))
Catalog.addProduct(Product('ch08', 2, 5))
Catalog.addProduct(Product('ch09', 2, 5))
Catalog.addProduct(Product('ch10', 2, 5))
Catalog.addProduct(Product('ch11', 2, 5))
Catalog.addProduct(Product('ch12', 2, 5))
Catalog.addProduct(Product('ch13', 2, 5))
Catalog.addProduct(Product('ch14', 2, 5))
Catalog.addProduct(Product('ch15', 2, 5))
Catalog.addProduct(Product('ch16', 2, 5))
# Pallete
Catalog.addProduct(Product('ch08_cpt_WVCOLOR35', 2, 5))
Catalog.addProduct(Product('ch09_cpt_WVCOLOR35', 2, 5))
Catalog.addProduct(Product('ch10_cpt_WVCOLOR35', 2, 5))
Catalog.addProduct(Product('ch13_cpt_IR4AVHRR6', 2, 5))
Catalog.addProduct(Product('ch13_cpt_DSA', 2, 5))
# RGBs
Catalog.addProduct(Product('airmass', 2, 5))
Catalog.addProduct(Product('ash', 2, 5))
Catalog.addProduct(Product('cloud_phase_eumetsat', 2, 5))
Catalog.addProduct(Product('day_cloud_phase_jma', 2, 5))
Catalog.addProduct(Product('convective_storm', 2, 5))
Catalog.addProduct(Product('day_snow_fog', 2, 5))
Catalog.addProduct(Product('differential_wv', 2, 5))
Catalog.addProduct(Product('dust', 2, 5))
Catalog.addProduct(Product('fire_temperature', 2, 5))
Catalog.addProduct(Product('natural_color', 2, 6))
Catalog.addProduct(Product('night_microphysics', 2, 6))
Catalog.addProduct(Product('simple_wv', 2, 6))
Catalog.addProduct(Product('so2', 2, 6))
Catalog.addProduct(Product('true_color_ch13_dsa', 2, 6))