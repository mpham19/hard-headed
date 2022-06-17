#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:18:47 2022

@author: glennturner
"""
#set your working directory to be the git repo .../GitHub/hard-headed

import xml.etree.ElementTree as ET
import os

#make a new directory if one isn't there to save the new xml files into 
if os.path.isdir('SODA Dataset/Cleaned_Annotations'):
    pass
else:
    print('creating cleaned annotations directory')
    os.mkdir('SODA Dataset/Cleaned_Annotations')
    
#initialize a couple of tracking tools    
scrubbed_count=0
empty_xml_count=0
empty_xml_files=[]

#make a list of all the files in our dataset
for filename in os.listdir('SODA Dataset/Annotations'):
    
    #if it's an xml file, enter the cleaning stage
    if filename.endswith('.xml'):
        
        #parse the xml file
        tree = ET.parse(f'SODA Dataset/Annotations/{filename}')
        root = tree.getroot()
            
        #hunt through xml file and remove objects which we don't want    
        for object in root.findall('object'):
            #print(object[0].text)
            if object[0].text not in ['person','helmet','vest']:
                root.remove(object)
            
        #check to see if we deleted all the tags from a file
        if len(root.findall('object'))<1:
            print(f'All object tags removed from {filename}')
            empty_xml_count+=1
            empty_xml_files.append(filename)
            
        #save the scrubbed xml file
        tree.write(f'SODA Dataset/Cleaned_Annotations/{filename}')
        scrubbed_count+=1
