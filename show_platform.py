from ttp import ttp
import json

data_to_parse = """
Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
------  -----   ---------             -----------  --------------  -------       --------
 1       32     C9200-24P             2FCYCZBVY4R  df68.ebfc.44bb  V01           17.03.03
 2       32     C9200-24P             PW73B4U6UVW  982a.7043.0b7f  V01           17.03.03
 3       32     C9200-24P             PRJ5QKQE73S  3b9f.390b.04d2  V01           17.03.03
Switch/Stack Mac Address : df68.ebfc.44bb - Local Mac Address
Mac persistency wait time: Indefinite
                                   Current
Switch#   Role        Priority      State
-------------------------------------------
*1       Active          15         Ready
 2       Standby         14         Ready
 3       Member          13         Ready
"""

def show_platform(data_to_parse):
    ttp_template = template

    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()

    # print result in JSON format
    results = parser.result(format='json')[0]
    #print(results)

    #converting str to json. 
    result = json.loads(results)

    return(result)

print(show_platform(data_to_parse))

"""

Given Output: 

[{'SHOW_PLATFORM': [{'Current_State': 'Ready', 'Priority': '15', 'Role': 'Active', 'switch_id': '1'}, {'Current_State': 'Ready', 'Priority': '14', 'Role': 'Standby', 'switch_id': '2'}, {'Current_State': 'Ready', 'Priority': '13', 'Role': 'Member', 'switch_id': '3'}]}]

"""
