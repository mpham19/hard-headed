#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:18:47 2022

@author: glennturner
"""

import xml.etree.ElementTree as ET
import xml
import os

tree = ET.parse('SODA Dataset/Annotations/hd02.xml')
root = tree.getroot()
    
#hunt through xml file and remove objects which we don't want    
for object in root.findall('object'):
    print(object[0].text)
    if object[0].text not in ['person','helmet', 'vest']:
        root.remove(object)

#make a new directory if one isn't there to save the new xml files into 
if os.path.isdir('SODA Dataset/Cleaned_Annotations'):
    pass
else:
    print('creating cleaned annotations directory')
    os.mkdir('SODA Dataset/Cleaned_Annotations')
    
#save the xml file
tree.write('SODA Dataset/Cleaned_Annotations/hd02.xml')
