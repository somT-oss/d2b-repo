import boto3

# Create an EMR client
emr_client = boto3.client('emr', region_name='your-region')

# Specify the ID of the cluster you want to describe
cluster_id = 'your-cluster-id'

# Describe the EMR cluster
response = emr_client.describe_cluster(ClusterId=cluster_id)

# Retrieve cluster details safely using .get()
cluster_info = response.get('Cluster', {})

# Print cluster details
print(f"Cluster ID: {cluster_info.get('Id', 'N/A')}")
print(f"Cluster Name: {cluster_info.get('Name', 'N/A')}")
print(f"Cluster Status: {cluster_info['Status'].get('State', 'N/A')}")
print(f"Cluster Creation Date: {cluster_info['Status']['Timeline'].get('CreationDateTime', 'N/A')}")
print(f"Cluster End Date: {cluster_info['Status']['Timeline'].get('EndDateTime', 'N/A')}")
print(f"Cluster Master Public DNS: {cluster_info.get('MasterPublicDnsName', 'N/A')}")
print(f"Cluster EC2 Key Name: {cluster_info['Ec2InstanceAttributes'].get('KeyName', 'N/A')}")
print(f"Cluster Auto Termination Status: {cluster_info.get('AutoTerminate', 'N/A')}")

# Retrieve instance groups safely using .get()
instance_groups = cluster_info.get('InstanceGroups', [])

# Print instance groups information
for instance_group in instance_groups:
    print(f"Instance Group ID: {instance_group.get('Id', 'N/A')}")
    print(f"Instance Group Name: {instance_group.get('Name', 'N/A')}")
    print(f"Instance Group Type: {instance_group.get('InstanceGroupType', 'N/A')}")
    print(f"Instance Group Status: {instance_group['Status'].get('State', 'N/A')}")
    print(f"Instance Group Instance Count: {instance_group.get('InstanceCount', 'N/A')}")

# Print other cluster details as needed
