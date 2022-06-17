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
exported_count=0
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
        
        #keep track of how many files we have scrubbed
        scrubbed_count+=1
        
        #check to see if we deleted all the tags from a file
        if len(root.findall('object'))<1:
            #print(f'All object tags removed from {filename}')
            empty_xml_count+=1
            empty_xml_files.append(filename)
            continue #don't write out the empty xml files with no objects
            
        #save the scrubbed xml file
        tree.write(f'SODA Dataset/Cleaned_Annotations/{filename}')
        exported_count+=1
        
#now let's go through the actual images and 
#delete all the files which no longer have any object tags
image_titles_to_delete=[item[:-3]+'jpg' for item in empty_xml_files]
for filename in os.listdir('SODA Dataset/Images'):
    if filename in image_titles_to_delete:
        #print(filename)
        os.remove(f'SODA Dataset/Images/{filename}')
    
        
    
    
    
#now let's check and make sure we still have good data
annotation_files=os.listdir('SODA Dataset/Cleaned_Annotations')
image_files=os.listdir('SODA Dataset/Images')

if len(annotation_files)==len(image_files):
    print('Check complete - Same number of images and annotations')
else: print('DATA ERROR - unequal number of images and annotations')


annotation_names=[item[:-4] for item in annotation_files]
image_names=[item[:-4] for item in image_files]
if annotation_names.sort()==image_names.sort():
    print('Check complete - file names match between images and annotations')
else: print('DATA ERROR - file names do match between images and annotations')

if len(set(annotation_names))==len(annotation_names) and len(set(image_names))==len(image_names):
    print('Check complete - image and annotation names are unique')
else: print('DATA ERROR - duplicate image or annotation names detected')
    
