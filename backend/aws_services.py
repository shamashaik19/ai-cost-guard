import boto3
import os

REGION = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")

def get_services():
    ec2 = boto3.client("ec2", region_name=REGION)
    s3 = boto3.client("s3", region_name=REGION)
    rds = boto3.client("rds", region_name=REGION)
    lam = boto3.client("lambda", region_name=REGION)

    return {
        "EC2": len(ec2.describe_instances()["Reservations"]),
        "S3": len(s3.list_buckets()["Buckets"]),
        "RDS": len(rds.describe_db_instances()["DBInstances"]),
        "Lambda": len(lam.list_functions()["Functions"])
    }
