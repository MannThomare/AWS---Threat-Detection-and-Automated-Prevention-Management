import boto3
ec2 = boto3.resource('ec2')
isolated_sg = 'sg-09edba92e2ae7e358'
def lambda_handler(event, context):
 finding_type = event['detail']['type']
 instance_id = event['detail']['resource']['instanceDetails']['instanceId']
 
 print(f"Finding type: {finding_type}")
 print(f"Instance ID: {instance_id}")
 
 if finding_type == 'Recon:EC2/Portscan':
  victim_ec2 = ec2.Instance(instance_id)
  victim_ec2.modify_attribute(Groups=[isolated_sg])
