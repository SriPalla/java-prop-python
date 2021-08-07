import yaml

import jprops
import argparse


def main(filepath):
    props = jprops.getJavaProperties(open(filepath))
    yamlDict = dict()
    envProp = dict()
    for key, value in props.items():
        envProp[key] = value

    yamlDict['env'] = envProp
    print(yamlDict)
    yamlFile = open("sample.yaml", "w")

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
