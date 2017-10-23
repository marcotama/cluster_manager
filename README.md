# MANAGE YOUR CLUSTER #

This script can be used to distribute many jobs, each consisting of a console command, on a cluster of machines.

Uses SSH to launch commands and copy files.
Supports authentication via password, plain-text key and encrypted key.

Configuration is done via JSON files.

Example of jobs configuration:
```
{
  "local_preparation": [
    {
      "create_folders": [
        "./logs/"
      ]
    }
  ],


  "jobs": [
    {
      "commands": [
        "date >> datetime.log"
      ],

      "required_files": [
        {"local_path": "message.txt", "remote_path": "message.txt"}
      ],

      "return_files": [
        {"local_path": "datetime.log", "remote_path": "datetime.txt"}
      ],

      "id": "job_1"
    }
  ]
}
```


Example of workers configuration:
```
{
  "workers": [
    {"no_cpu": 2, "hostname": "1.2.3.4", "username": "nir", "password": null, "private_key_file": "~/.ssh/id_nir"}, // private key authentication if private key is plain
    {"no_cpu": 1, "hostname": "1.2.3.5", "username": "seba", "password": "unguessable", "private_key_file": "id_seba"}, // private key authentication if private key is password protected
    {"no_cpu": 4, "hostname": "1.2.3.6", "username": "marco", "password": "more_unguessable", "private_key_file": null} // password authentication
  ]
}
```



### Install requirements ###

Run this command to install requirements:
`pip install -r requirements.txt`
