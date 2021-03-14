#!/bin/bash

# Add the below line in crontab to take backup every night at 2 using crontab -e
#	0 2 * * * sudo ./backup.sh >/dev/null 2>&1


backup_dir="/hdd/Backup/"

dateTime=$(date +%d-%b-%Y-%H%M)

backup_logs="/var/log/backlogs_$dateTime"

backup_files="/home /root /etc /var/spool /var/opt"

# Checking if backup directory exist or not
if [[ -d $backup_dir ]]; then
	rsync -aAXlzv --no-o --no-g --munge-links --exclude={"*/__pycache__/*","*/.cache/*"} $backup_files $backup_dir | tee -a $backup_logs

	# PIP2 installed pkges
	pip2 freeze > $backup_dir/pip2_packages.txt

	if [[ $? -eq 0 ]]; then
		echo "[INFO]: PIP2 packges are backup in $backup_dir/pip2_packages.txt" >> $backup_logs
	else
		echo "[WARNING]: PIP2 packges are not backup" >> $backup_logs
	fi

	# PIP3 installed pkges
	pip3 freeze > $backup_dir/pip3_packages.txt

	if [[ $? -eq 0 ]]; then
		echo "[INFO]: PIP3 packges are backup in $backup_dir/pip3_packages.txt" >> $backlogs_logs
	else
		echo "[WARNING]: PIP3 packges are not backup" >> $backup_logs
	fi

	# APT installed pkges
	apt list | grep -v "Listing... Done" > $backup_dir/apt_packages.txt

	if [[ $? -eq 0 ]]; then
		echo "[INFO]: APT packges are backup in $backup_dir/apt_packages.txt" >> $backup_logs
	else
		echo "[WARNING]: APT packges are not backup" >> $backup_logs
	fi

else
	echo -e "\n[ERROR]: Backup disk not mounted. Can't take backup !!!" >> /var/log/backlogs_$dateTime
fi
