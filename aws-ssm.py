import json
from subprocess import Popen, PIPE
import time

"""
To retrieve all ssm parameters use command:
aws ssm get-parameters-by-path --path "/" --recursive > param_store.json
"""

"""
To mass upload parameters from json to ssm parameter store use:
"""
with open('/Users/bryanolson/Programming/param_store.json') as f:
    param_store = json.load(f)

    for nums in range(len(param_store['Parameters'])):
        ssm_name = param_store['Parameters'][nums]['Name']
        ssm_value = param_store['Parameters'][nums]['Value']
        ssm_type = param_store['Parameters'][nums]['Type']

        command = f"aws ssm put-parameter --name \"{ssm_name}\" --value \"{ssm_value}\" --type \"{ssm_type}\""
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        time.sleep(1)
        
