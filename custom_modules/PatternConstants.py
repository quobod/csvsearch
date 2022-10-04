#! /usr/bin/python3

import re
from .TypeTester import arg_is_a_string as aias


""" IPv4 address """


def valid_ipv4(address=None):
    if not address == None:
        if not aias(address):
            address = str(address)

        IPv4 = re.compile(r"([0-9]{1,3}\.){3}([0-9]{1,3})$")
        matched = re.search(IPv4, address)
        if not matched == None:
            return True
    return False


""" MAC address """


def valid_mac(address=None):
    if not address == None:
        IPv4 = re.compile(r"([0-9a-fA-F]{2}\:){5}([0-9a-fA-F]{2})$")
        matched = re.search(IPv4, str(address))
        return not matched == None
    return False


""" Network range  """


def valid_network_range(address=None):
    if not address == None:
        IPv4_network = re.compile(r"([0-9]{1,3}\.){3}([0-9]{1,3})\/[1-9]{1,3}$")
        matched = re.search(IPv4_network, str(address))
        return not matched == None
    return False


""" File extensions """


def has_ext(string=None):
    if not string == None:
        FILE_EXTENSION = re.compile(r"(.)+(\.[a-z]{2,3})$")
        matched = re.search(FILE_EXTENSION, string)
        return not matched == None
    return False


def has_char(string=None, character=None):
    if not string == None and not character == None:
        return "{}".format(character) in string
    return False


def is_a_number_or_float(arg=None):
    if not arg == None:
        pattern = re.compile(r"^([0-9]+(\.)?)?[0-9]{1,}$")
        matched = re.search(pattern, str(arg))
        return not matched == None
    return False


def is_a_number(arg=None):
    if not arg == None:
        pattern = re.compile(r"^([0-9]+)$")
        matched = re.search(pattern, str(arg))
        return not matched == None
    return False


def is_port_range(arg=None):
    if not arg == None:
        pattern = re.compile(r"^(([0-9]+)(\-))([0-9]+)|((\,)([0-9]+))+")
        matched = re.search(pattern, arg)

        # print("Matched: {}".format(matched))

        if matched:
            return not matched == None

    return False
