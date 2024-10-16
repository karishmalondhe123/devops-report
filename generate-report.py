import boto3
import csv
from datetime import datetime

# Set up clients
cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')

# Define the time range for the report
one_week_ago = datetime.now() - timedelta(days=7)

def get_cpu_utilization(instance_id, start_time, end_time):
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=3600,
        Statistics=['Average']
    )
    # Return the average CPU utilization from the response
    return sum(dp['Average'] for dp in response['Datapoints']) / len(response['Datapoints']) if response['Datapoints'] else 0

def get_recent_instances():
    # Retrieve instances launched in the last week
    response = ec2.describe_instances()
    recent_instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['LaunchTime'] >= one_week_ago:
                recent_instances.append(instance)
    return recent_instances

# Generate CSV Report
def generate_csv():
    with open('weekly_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['InstanceId', 'CPUUtilization', 'MemoryUsed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Process instances and metrics
        for instance in get_recent_instances():
            instance_id = instance['InstanceId']
            cpu_utilization = get_cpu_utilization(instance_id, one_week_ago, datetime.now())
            memory_used = 'N/A'  # Placeholder for memory logic, if applicable
            
            writer.writerow({
                'InstanceId': instance_id,
                'CPUUtilization': cpu_utilization,
                'MemoryUsed': memory_used
            })

if __name__ == "__main__":
    generate_csv()
