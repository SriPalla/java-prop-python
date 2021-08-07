import yaml

import jprops
import ruamel.yaml
import argparse


def main(filepath):
    props = jprops.getJavaProperties(open(filepath))
    yamlDict = dict()
    envProp = []
    for key, value in props.items():
        entry = dict()
        entry['name'] = key
        entry['value'] = value
        envProp.append(entry)

    yamlDict['envProp'] = envProp
    print(yamlDict)
    yamlFile = open("sample.yaml", "w")
    yaml = ruamel.yaml.YAML()
    yaml.indent(sequence=4, offset=2)
    yaml.dump(yamlDict, yamlFile)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="input file name with path", required=True)
    args = parser.parse_args()
    return args


# Using jprops to get properties from a java style property file
if __name__ == '__main__':
    inputs = parse_args()
    main(inputs.file)
