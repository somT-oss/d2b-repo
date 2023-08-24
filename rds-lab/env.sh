#!/usr/bin/bash

echo "Setting evnironnemt variables!"

echo "export RDS_HOST=db-instance-identifier.cfd1mkirrlto.us-east-1.rds.amazonaws.com" >> ~/.profile
echo "export RDS_USERNAME=postgres" >> ~/.profile
echo "export RDS_PASSWORD=testing" >> ~/.profile
echo "export RDS_DATABASE=users" >> ~/.profile
echo "export RDS_PORT=5432" >> ~/.profile

echo "Done setting environment variables"