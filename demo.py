import yaml

import jprops
import ruamel.yaml

# Using jprops to get properties from a java style property file
if __name__ == '__main__':
    props = jprops.getJavaProperties(open("sample.properties"))
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

