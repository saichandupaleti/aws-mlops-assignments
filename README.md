# Flask S3 File Lister

This project creates a Flask application that lists files from folders in an S3 bucket. The app is deployed on an EC2 instance.

## Steps

# aws-mlops-assignments
This Repository contains assignments concerned with AWS cloud training
# Instructions to run the flask app on EC2 instance

## Connect to EC2 instance "FlaskAppYat" using SSH
- ssh -i RSAkey ubuntu@public-ip-of-ec2-instance

## Activate the python virtual environment
- source venv/bin/activate

## Run the flask app on port 8085
- flask --app app run --host=0.0.0.0 --port=8085

## Check the flaskapp
- Open the EC2 instance public-ip:8085 to visualize the flask application

# Output snapshots
