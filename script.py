from asyncio import events
import boto3

def main():
    region = 'us-east-2'
    ec2 = boto3.client('ec2', region_name=region)
    resp =ec2.describe_instances()
    instance_tostart_ids = []
    instance_tostop_ids = []

    for reservation in resp['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Key'].lower() == 'updown' \
                    and tag['Value'].lower() == 'march-16-2022':
                    instance_state = instance['State']['Name']
                    instance_tostop_ids.append(instance['InstanceId'])
                    instance_tostart_ids.append(instance['InstanceId'])
                    
    if instance_state == 'running':
        print("STOP your instances: " + str(instance_tostart_ids)) 
        ec2.stop_instances(InstanceIds=instance_tostart_ids)
    elif instance_state == 'stopped':
         ec2.start_instances(InstanceIds=instance_tostop_ids)
         print("STart your instances: " + str(instance_tostart_ids)) 
                        
                       
                    
    
 
if __name__ == "__main__":
 main()  
