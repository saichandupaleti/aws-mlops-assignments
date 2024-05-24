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

# Output snapshots
![Screenshot 2024-05-22 214635](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/65aa4c27-e26b-48ec-8ecb-dea31cbcf7a8)
![Screenshot 2024-05-22 214617](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/e0ecda6b-a237-4094-bb86-b56e572c6416)
![Screenshot 2024-05-22 211654](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/12711f0b-0817-40c7-9252-17b3ebfd150e)
![image](https://github.com/saichandupaleti/aws-mlops-assignments/assets/162572665/0796a5c2-4b8c-433b-af8f-bedeccae0902)



