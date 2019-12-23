#!/usr/bin/env python3

# imports
import csv
from xml.etree.ElementTree import Element, SubElement
from ElementTree_pretty import prettify
from argparse import ArgumentParser

# functions
def create_base_xml(fieldnames):
    # function variables
    xmlns = 'http://example.org/oudenburg-dc'
    xsi = 'http://www.w3.org/2001/XMLschema-instance'
    dcterms = 'http://purl.org/dc/terms/'
    schema = 'http://example.org/oudenburg-dc oudenburg-record.xsd http://purl.org/dc/terms/ http://dublincore.org/schemas/xmls/qdc/2008/02/11/dcterms.xsd'
    marcrel = 'http://www.loc.gov/loc.terms/relators/'
    cld = 'http://purl.org/cld/terms/'
    dc = 'http://purl.org/dc/elements/1.1/'

    root = Element('record')
    root.set('xmlns', xmlns)
    root.set('xmlns:xsi', xsi)
    
    if 'dc:creator' in fieldnames:
        root.set('xmlns:dc', dc)
        schema += ' http://purl.org/dc/elements/1.1/ http://dublincore.org/schemas/xmls/qdc/2008/02/11/dc.xsd'

    root.set('xmlns:dcterms', dcterms)

    if 'marcrel:own' in fieldnames:
        root.set('xmlns:marcrel', marcrel)
    
    if 'cld:itemformat' in fieldnames or 'cld:isLocatedAt' in fieldnames:
        root.set('xmlns:cld', cld)

    root.set('xsi:schemaLocation', schema)
    return root

def create_dc_xml(file):
    with open(file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        xml = create_base_xml(csvreader.fieldnames)
        for row in csvreader:
            for key, value in row.items():
                if key.startswith('dc:') or key.startswith('dcterms:') or \
                key.startswith('cld:') or key.startswith('marcrel:'):
                    child = SubElement(xml, key)
                    child.text = value
            mydata = prettify(xml)
            filename = f"{row['dcterms:identifier']}.xml"
            print_xml(filename, mydata)

def print_xml(filename, data):
    myfile = open(filename, 'w') # change outputfolder in argparse
    myfile.write(str(data.decode('utf-8')))
    myfile.close()

# main
file = 'testdata/voorbeeld_collectie.csv' # change in argparse
create_dc_xml(file)