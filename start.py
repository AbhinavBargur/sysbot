#/usr/bin/python
import boto.ec2
import commands
commands.getoutput("Start")

auth = {"aws_access_key_id": "AKIAJYL3V74CIAAOXWEQ", "aws_secret_access_key": "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"}
 
my_list=boto.ec2.regions()

conn = boto.ec2.connect_to_region("eu-west-1",**auth)
conn.start_instances(instance_ids=['i-051bfc5a0a6e98408'])