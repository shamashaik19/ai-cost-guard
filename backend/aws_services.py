import boto3

def get_running_services():
    services = {}

    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    running = sum(
        1
        for r in instances['Reservations']
        for i in r['Instances']
        if i['State']['Name'] == 'running'
    )
    services['EC2'] = running

    s3 = boto3.client('s3')
    services['S3'] = len(s3.list_buckets()['Buckets'])

    rds = boto3.client('rds')
    services['RDS'] = len(rds.describe_db_instances()['DBInstances'])

    lambda_client = boto3.client('lambda')
    services['Lambda'] = len(lambda_client.list_functions()['Functions'])

    return services
