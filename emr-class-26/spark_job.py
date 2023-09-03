import boto3

# Initialize the Boto3 EMR client
emr_client = boto3.client('emr', region_name='your-region-name')

# Specify the cluster ID of the EMR cluster you want to add the step to
cluster_id = 'cluster-id'

# Define the Spark step
spark_step = {
    'Name': 'MySparkStep',  # Name for your step
    'ActionOnFailure': 'CONTINUE',  # or 'TERMINATE_CLUSTER', 'CANCEL_AND_WAIT'
    'HadoopJarStep': {
        'Jar': 'command-runner.jar',  # This is a special EMR JAR
        'Args': [
            'spark-submit',
            '--master', 'yarn',
            '--deploy-mode', 'cluster',
            '--py-files', 's3://your-zip-file.zip',
            's3://your-main.py'
        ]
    }
}


# Add the step to the cluster
response = emr_client.add_job_flow_steps(JobFlowId=cluster_id, Steps=[spark_step])

print("Step added with ID:", response['StepIds'][0])
