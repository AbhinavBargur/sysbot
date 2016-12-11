#/usr/bin/python
import boto.ec2
# specify AWS keys
auth = {"aws_access_key_id": "AKIAJYL3V74CIAAOXWEQ", "aws_secret_access_key": "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"}
 
#client = boto.client('ec2')
my_list=boto.ec2.regions()
print my_list
conn = boto.ec2.connect_to_region("eu-west-1",**auth)
conn.stop_instances(instance_ids=['i-051bfc5a0a6e98408'])