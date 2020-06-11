import json
from subprocess import Popen, PIPE
import time
import sys

"""
To retrieve all ssm parameters use command:
aws ssm get-parameters-by-path --path "/" --recursive --with-decryption > test2.json
"""

"""
To mass upload parameters from json to ssm parameter store use:
"""
with open('/Users/bryanolson/Programming/legacy_param.json') as f:
    param_store = json.load(f)

    for nums in range(len(param_store['Parameters'])):
        ssm_name = param_store['Parameters'][nums]['Name']
        ssm_value = param_store['Parameters'][nums]['Value']
        ssm_type = param_store['Parameters'][nums]['Type']

        if len(sys.argv) == 2:
            command = f"aws ssm put-parameter --name \"{ssm_name}\" --value \"{ssm_value}\" --type \"{ssm_type}\" --profile {str(sys.argv[1])}" #optional: --overwrite
            p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            
        else:
            command = f"aws ssm put-parameter --name \"{ssm_name}\" --value \"{ssm_value}\" --type \"{ssm_type}\"" #optional: --overwrite
            p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            
        time.sleep(1)     
