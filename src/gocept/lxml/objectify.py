# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt

import lxml.etree
import lxml.objectify


objectify_parser = lxml.etree.XMLParser(remove_blank_text=True)
objectify_parser.set_element_class_lookup(
    lxml.etree.ElementNamespaceClassLookup(
        lxml.objectify.ObjectifyElementClassLookup()))


def fromstring(s):
    return lxml.etree.fromstring(s, objectify_parser)


XML = fromstring


def fromfile(handle):
    return lxml.etree.parse(handle, objectify_parser).getroot()
