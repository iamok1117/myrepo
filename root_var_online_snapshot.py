import boto3
client = boto3.client('ec2')
response = client.describe_instance_attribute(
    Attribute='blockDeviceMapping',
    InstanceId='i-bjdnbdjmw'
)
my_snapshot_volume_list=[]
if 'BlockDeviceMappings' in response:
    my_device_list = response['BlockDeviceMappings']
    

    for i in my_device_list:
        if i['DeviceName'] == 'sda1':
            my_volume = i['Ebs']['VolumeId']
            my_snapshot_volume_list.append(my_volume)
        if i['DeviceName'] == 'sdf':
            my_volume = i['Ebs']['VolumeId']
            my_snapshot_volume_list.append(my_volume)
if len(my_snapshot_volume_list)<2:
    print(f"root and var volume are not listed correctly")
else:
    print("root volume is {my_snapshot_volume_list[0]}"),
    print("var volume is {my_snapshot_volume_list[1]}")
resp_root = client.create_snapshot(
    VolumeId = my_snapshot_volume_list[0]
)
resp_var = client.create_snapshot(
    VolumeId = my_snapshot_volume_list[1]
)
root_snapshot_id = resp_root['SnapshotId'],
var_snapshot_id = resp_var['SnapshotId']

#print the snapshot details along with volume

print(f"root snapshot is triggered {root_snapshot_id} for the volume{my_snapshot_volume_list[0]}")
print(f"root snapshot is triggered {var_snapshot_id} for the volume{my_snapshot_volume_list[1]}")

waiter = client.get_waiter('snapshot_completed')
print("Waiting for root snapshot to complete...")
waiter.wait(
    SnapshotIds = [root_snapshot_id]
)
print(f"root snapshot {root_snapshot_id} is completed for volume {my_snapshot_volume_list[0]}")

print("waiting for var snapshot to complete ..")
waiter.wait(
    SnapshotIds = [var_snapshot_id]
)
print(f"var snapshot {var_snapshot_id} is completed for the volume {my_snapshot_volume_list[1]}")
print("habibi come to dubai")

#habibi come to dubai this is for git hub practice
#dhoni finishes off in style

