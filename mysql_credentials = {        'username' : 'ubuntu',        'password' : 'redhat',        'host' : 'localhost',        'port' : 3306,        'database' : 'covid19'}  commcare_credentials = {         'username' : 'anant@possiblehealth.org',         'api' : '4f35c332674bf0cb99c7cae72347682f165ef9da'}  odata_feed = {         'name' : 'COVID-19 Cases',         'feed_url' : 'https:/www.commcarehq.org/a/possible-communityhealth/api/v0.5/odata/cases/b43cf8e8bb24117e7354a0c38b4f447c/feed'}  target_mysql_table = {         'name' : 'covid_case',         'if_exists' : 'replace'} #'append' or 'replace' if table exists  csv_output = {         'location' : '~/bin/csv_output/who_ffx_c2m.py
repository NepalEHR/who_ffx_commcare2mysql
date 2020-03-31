mysql_credentials = {
       'username' : 'ubuntu',
       'password' : '******',
       'host' : 'localhost',
       'port' : 3306,
       'database' : 'covid19'}

commcare_credentials = {
        'username' : 'user@company.org',
        'api' : 'xyzxyz'}

odata_feed = {
        'name' : 'COVID-19 Cases',
        'feed_url' : 'https://www.commcarehq.org/a/project/api/v0.5/odata/cases/xyz/feed'}

target_mysql_table = {
        'name' : 'covid_case',
        'if_exists' : 'replace'} #'append' or 'replace' if table exists

csv_output = {
        'location' : '~/bin/csv_output/',
        'skip' : 'false'} # skip generation of csv file (true or false)
