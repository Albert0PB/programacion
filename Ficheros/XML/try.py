from xml.etree.ElementTree import Element, SubElement, tostring

file = 'data.xml'

root = Element('nodo_raiz')

child1 = SubElement(root, "nodo_hijo1")
child2 = SubElement(root, "nodo_hijo2")
child3 = SubElement(root, "nodo_hijo3")

grandchild1 = SubElement(child1, "nodo_hijo1_de_hijo1")
grandchild2 = SubElement(child1, "nodo_hijo2_de_hijo1")
grandchild3 = SubElement(child1, "nodo-hijo3-de-hijo1")

grandchild4 = SubElement(child2, "nodo_hijo1_de_hijo2")
grandchild5 = SubElement(child2, "nodo_hijo2_de_hijo2")
grandchild6 = SubElement(child2, "nodo-hijo3-de-hijo2")

grandchild7 = SubElement(child3, "nodo_hijo1_de_hijo3")
grandchild8 = SubElement(child3, "nodo_hijo2_de_hijo3")
grandchild9 = SubElement(child3, "nodo-hijo3-de-hijo3")

with open(file, 'w') as xml_file:
    xml_file.write(tostring(root).decode('utf8'))
