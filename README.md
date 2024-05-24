# Flask App with Rds

This project sets up a VPC with public and private subnets, an RDS MySQL instance, and an auto-scaling Flask application. The Flask app records timestamps of API calls into a MySQL database, with Lambda functions for dynamic scaling based on the day of the week.

## Steps

# aws-mlops-assignments
This Repository contains assignments concerned with AWS cloud training

## VPC and Subnets
Create a VPC with one public and one private subnet.

## Create RDS MySQL Instance
Create an RDS MySQL instance in the public subnet, create a logs table in the MySQL database, and move the RDS instance to the private subnet and change the security group to allow traffic through ec2 instance

## EC2 Instances
Launch EC2 instances in the public subnet within the same VPC and ensure the security group allows inbound traffic on necessary ports such as 5000 ,8085

## Flask Application
Develop a Flask app with an endpoint that inserts a timestamp into the logs table on each API call, deploy the app to the EC2 instances, and configure an Application Load Balancer to distribute traffic across the instances in the auto-scaling group.

## Auto Scaling Group
Create an auto-scaling group with a desired size of 2 instances and attach the Application Load Balancer to the group.

## Lambda Functions for Scaling
Create a Lambda function to scale down the auto-scaling group to 0 instances on Saturdays and another Lambda function to scale up the group to 1 instance on Mondays. Schedule these functions using CloudWatch Events or EventBridge.

# Instructions to run the flask app on EC2 instance
## Connect to EC2 instance "FlaskApp" using SSH
- ssh -i RSAkey ubuntu@public-ip-of-ec2-instance

## Activate the environment and launch the app
- invoke deploy

## Check the flaskapp
- Open the EC2 instance public-ip:8085 to visualize the flask application


# For notebooks
Create two notebooks in the aws glue one contains pre-processing and other containing model creating and evaluation part which uses dataset inside s3
Create a Workflow for those 2 notebooks by creating corresponding triggers and run the workflow
## output snapshots
![Screenshot 2024-05-24 122143](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/dd60ce99-23c2-4cfe-bf85-b813287ba5be)
![Screenshot 2024-05-24 122159](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/4f0bab41-1ad6-4da6-ab8d-02de92f316d3)
![Screenshot 2024-05-24 122217](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/27961d9c-e7f3-42cf-a881-8bd33b14fd91)
![Screenshot 2024-05-24 122256](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/924ca94d-7efb-4280-a29b-f8d2426128bb)




