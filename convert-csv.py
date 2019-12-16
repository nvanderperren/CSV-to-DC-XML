
# imports
import csv
from xml.etree.ElementTree import Element, SubElement
from ElementTree_pretty import prettify
from argparse import ArgumentParser

# constans
XMLNS = 'http://example.org/oudenburg-dc'
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
DCTERMS = 'http://purl.org/dc/terms/'
SCHEMA = 'http://example.org/oudenburg-dc oudenburg-record.xsd http://purl.org/dc/terms/ http://dublincore.org/schemas/xmls/qdc/2008/02/11/dcterms.xsd'

# functions
def createRootXML():
    # TODO add elements of collection.xml
    root = Element('record')
    root.set('xmlns', XMLNS)
    root.set('xmlns:xsi', XSI)
    root.set('xmlns:dcterms', DCTERMS)
    root.set('xsi:schemaLocation', SCHEMA)
    return root

def createXML(file,xml):
    with open(file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            for key, value in row.items():
                child = SubElement(xml, key)
                child.text = value
            mydata = prettify(xml)
            filename = f"{row['dcterms:identifier']}.xml"
            print(filename,mydata)

def print(filename,data):
    myfile = open(filename, 'w') # change outputfolder in argparse
    myfile.write(str(data.decode('utf-8')))
    myfile.close()

# main
file = 'testdata/voorbeeld_stuk.csv' # change in argparse
createXML(file,createRootXML())