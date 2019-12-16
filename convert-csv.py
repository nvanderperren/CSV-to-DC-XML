import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from ElementTree_pretty import prettify

root = Element('record')
root.set('xmlns', 'http://example.org/oudenburg-dc')
root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
root.set('xmlns:dcterms', 'http://purl.org/dc/terms/')
root.set('xsi:schemaLocation', 'http://example.org/oudenburg-dc oudenburg-record.xsd http://purl.org/dc/terms/ http://dublincore.org/schemas/xmls/qdc/2008/02/11/dcterms.xsd')
child = SubElement(root,'child')
child.text = 'I\'m a child'


file = 'VAI.csv'

fields = []
rows = []

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = csvreader.next()

    for row in csvreader:
        rows.append(row)

print(prettify(root))
