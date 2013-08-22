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

