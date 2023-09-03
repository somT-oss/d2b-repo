import boto3

# Create an EMR client
emr_client = boto3.client('emr', region_name='us-east-1')

# Define cluster configuration
cluster_name = 'MyEMRCluster'
release_label = 'emr-6.5.0'  # EMR release label
instance_type = 'c1.xlarge'  # EC2 instance type for the master and core nodes
instance_count = 1  # Number of core instances
log_uri = 's3://your-s3-url'  # S3 URI for EMR logs
key_name = 'keypair_name'  # EC2 key pair for SSH access
subnet_id = 'subnet_id'  # Subnet ID where EMR cluster will be launched
job_flow_role = 'job_flow_role'
service_role = 'service_role'  # IAM role for EMR service
applications = ['Spark']  # List of applications to install

# Create EMR cluster
response = emr_client.run_job_flow(
    Name=cluster_name,
    ReleaseLabel=release_label,
    Instances={
        'InstanceGroups': [
            {
                'Name': 'MasterNode',
                'InstanceRole': 'MASTER',
                'InstanceType': instance_type,
                'InstanceCount': 1,
            },
            {
                'Name': 'CoreNode',
                'InstanceRole': 'CORE',
                'InstanceType': instance_type,
                'InstanceCount': instance_count,
            },
        ],
        'Ec2KeyName': key_name,
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': subnet_id,
    },
    LogUri=log_uri,
    ServiceRole=service_role,
    JobFlowRole=job_flow_role,
    Applications=[
        {'Name': app} for app in applications
    ],
)

# Print the cluster ID
print(f"Cluster ID: {response['JobFlowId']}")
