import boto3

# Create an EMR client
emr_client = boto3.client('emr', region_name='your-region')

# List EMR clusters
response = emr_client.list_clusters(ClusterStates=['TERMINATED', 'WAITING'])

# Print the cluster information
for cluster in response['Clusters']:

    if cluster['Status']['State'] == 'WAITING':
        print(f"Cluster ID: {cluster['Id']}")
        print(f"Cluster Name: {cluster['Name']}")
        print(f"Cluster Status: {cluster['Status']['State']}")
        print(f"Cluster Creation Date: {cluster['Status']['Timeline']['CreationDateTime']}")
        print("\n")
    else: 
        print(f"Cluster ID: {cluster['Id']}")
        print(f"Cluster Name: {cluster['Name']}")
        print(f"Cluster Status: {cluster['Status']['State']}")
        print(f"Cluster Creation Date: {cluster['Status']['Timeline']['CreationDateTime']}")
        print(f"Cluster End Date: {cluster['Status']['Timeline']['EndDateTime']}")
        print("\n")