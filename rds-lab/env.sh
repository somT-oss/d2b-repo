#!/usr/bin/bash

echo "Setting evnironnemt variables!"

# Environment variables
echo "export RDS_HOST={rds_host}" >> ~/.profile
echo "export RDS_USERNAME={rds-master-username}" >> ~/.profile
echo "export RDS_PASSWORD={rds-master-password}">> ~/.profile
echo "export RDS_DATABASE={rds-database}" >> ~/.profile
echo "export RDS_PORT={rds-port}" >> ~/.profile

echo "Done setting environment variables"