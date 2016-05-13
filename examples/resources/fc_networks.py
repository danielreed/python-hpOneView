# -*- coding: utf-8 -*-

from pprint import pprint
from hpOneView.oneview_client import OneViewClient

config = {"ip": "172.16.102.59",
          "credentials": {
              "authLoginDomain": "",
              "userName": "administrator",
              "password": ""}}

oneview_client = OneViewClient(config)

# Get all, with defaults
fc_nets = oneview_client.fc_networks.get_all()
pprint(fc_nets)

# Filter by name
fc_nets_filtered = oneview_client.fc_networks.get_all(filter='name="MyFibreNetwork"')
pprint(fc_nets_filtered)

# Sort by name descending
fc_nets_sorted = oneview_client.fc_networks.get_all(sort='name:descending')
pprint(fc_nets_sorted)

# Gets the second record
fc_nets_limited = oneview_client.fc_networks.get_all(1, 1)
pprint(fc_nets_limited)
