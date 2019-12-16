import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from ElementTree_pretty import prettify

top = Element('top')
top.set('XSI', 'dit is een link')
top.set('DC', 'dit is iets anders')
child = SubElement(top,'child')
child.text = 'I\'m a child'


file = 'VAI.csv'

fields = []
rows = []

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = csvreader.next()

    for row in csvreader:
        rows.append(row)

print(prettify(top))
