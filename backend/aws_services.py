import boto3
import os
from botocore.exceptions import ClientError, NoCredentialsError, NoRegionError

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

def get_running_services():
    services = {}

    try:
        ec2 = boto3.client("ec2", region_name=AWS_REGION)
        reservations = ec2.describe_instances()["Reservations"]
        services["EC2"] = sum(
            1 for r in reservations for i in r["Instances"]
            if i["State"]["Name"] == "running"
        )
    except Exception as e:
        services["EC2"] = f"Error: {str(e)}"

    try:
        s3 = boto3.client("s3", region_name=AWS_REGION)
        services["S3"] = len(s3.list_buckets()["Buckets"])
    except Exception as e:
        services["S3"] = f"Error: {str(e)}"

    try:
        rds = boto3.client("rds", region_name=AWS_REGION)
        services["RDS"] = len(rds.describe_db_instances()["DBInstances"])
    except Exception as e:
        services["RDS"] = f"Error: {str(e)}"

    try:
        lam = boto3.client("lambda", region_name=AWS_REGION)
        services["Lambda"] = len(lam.list_functions()["Functions"])
    except Exception as e:
        services["Lambda"] = f"Error: {str(e)}"

    return services
