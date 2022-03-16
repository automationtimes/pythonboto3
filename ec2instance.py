
from asyncio import events
import boto3
def main():
    region = 'us-east-2'
    ec2 = boto3.client('ec2', region_name=region)
    resp =ec2.describe_instances()
    instance_ids = []

    for reservation in resp['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Key'].lower() == 'updown' \
                    and tag['Value'].lower() == 'march-16-2022':
                    instance_ids.append(instance['InstanceId'])
                    instance_state = instance['State']['Name']
                    
    if instance_state == 'running':
        print("STOP your instances: " + str(instance_ids))
        ec2.stop_instances(InstanceIds=instance_ids)
    elif instance_state == 'stopped':
        print("Start your instances: " + str(instance_ids))
        ec2.start_instances(InstanceIds=instance_ids)
        print("Successfully start your instances: " + str(instance_ids))
if __name__ == "__main__":
 main() 

        



        
      
        
    
    
