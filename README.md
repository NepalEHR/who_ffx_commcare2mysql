# WHO FFX COMMCARE TO MYSQL

## QUICK START (without changing config):

1. ssh into “ubuntu@ec2-54-254-181-130.ap-southeast-1.compute.amazonaws.com”
2. Run “python3 ~/bin/who_ffx_commcare2mysql.py”
3. Log into mysql “mysql -u ubuntu -p covid19”, password: ******, and the data should have populated into “covid_case” table

## MORE INFO

### Test machine:
* ubuntu@ec2-54-254-181-130.ap-southeast-1.compute.amazonaws.com

### Files:
* Script location: ~/bin/who_ffx_commcare2mysql.py
* Config location: ~/bin/who_ffx_c2m_config.py

### To run:
* python3 ~/bin/who_ffx_commcare2mysql.py

### MySQL credentials, and database

### Data from Commcare:
* Uses Data Feed “COVID-19 Case Data”
    * Adjust the filters for feed date range (would suggest using the since date, as old case data can be updated as new info comes in)
    * While another odata feed can be used, I think the case data feed includes everything we would need

