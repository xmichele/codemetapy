import sys
import json
import os.path
from typing import Union, IO
from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import RDF
import lxml
from codemeta.common import AttribDict, add_triple, CODEMETA, SOFTWARETYPES, add_authors, SDO, COMMON_SOURCEREPOS, SOFTWARETYPES, license_to_spdx, generate_uri

def parse_authors(g: Graph, res: Union[URIRef, BNode], file: IO, args: AttribDict, property=SDO.author):
    """Parses a plain-text file of people, one person (author/contributor/maintainer) per line"""
    for line in file.readlines():
        line = line.strip()
        add_authors(g, res, line, single_author=args.single_author, baseuri=args.baseuri,property=property, skip_duplicates=True)
