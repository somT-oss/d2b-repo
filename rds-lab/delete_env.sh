sed -i '/RDS_HOST/d' ~/.profile
sed -i '/RDS_USERNAME/d' ~/.profile
sed -i '/RDS_PASSWORD/d' ~/.profile
sed -i '/RDS_PORT/d' ~/.profile
sed -i '/RDS_DATABASE/d' ~/.profile

echo "Removed all environment variables"