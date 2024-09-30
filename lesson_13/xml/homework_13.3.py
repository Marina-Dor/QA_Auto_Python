""" For the ideas_for_test/work_with_xml/groups.xml file, create a group/number
search function and return the timingExbytes/incoming value,
output the result to the console through the logger at the info level
"""

import xml.etree.ElementTree as ET
import xml
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

file_path = 'groups.xml'
group_number = 1


def search_incoming_by_group_number(file_path, group_number):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for group in root.findall('group'):
        if group.find('number').text == str(group_number):
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    logging.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
                else:
                    logging.info(f"Group: {group.find('name').text}, incoming: Not found")
            else:
                logging.info(f"Group: {group.find('name').text}, timing_exbytes: Not found")


search_incoming_by_group_number(file_path, group_number)
