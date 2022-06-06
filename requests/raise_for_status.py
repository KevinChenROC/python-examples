# import axapi_utils
# device_capture_config_name = '123'
# device_id = 'b1110820-3346-4353-a8dc-e70c85cb5616'
# import pdb; pdb.set_trace()
# axapi_utils.get_capture_config_by_name(device_capture_config_name, device_id)

# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com/')

# print response
print(response)

# print check if an error has occurred
print(response.raise_for_status())

import pdb; pdb.set_trace()
# ping an incorrect url
response = requests.get('https://geeksforgeeks.org/kevin/')

# print check if an error has occurred
print(response.raise_for_status())
