#CurrentIP python script
##Usage

Rename the sample_setting to base_setting.ini .

 > for example :

  ```sh
  mv sample_setting base_setting.ini
  ```
###Set the script to crontab .

  ```sh
  crontab -e
  ```

###input this command :
  ```sh
  */30 * * * *    python /home/to/myhom/scriptdir/getmyip.py
  ```

  > admire the stars with a 'tab'

##Settings

Edit the email login info in base_setting.ini .

- notify\_to\_email - input the email you want to send.
- sender - set a name@localhost for your server.
- server - input the smtp server want to connect. 
- port - smtp server port for example the google smtp is 587.
- name - login email account.
- password - login email password .
