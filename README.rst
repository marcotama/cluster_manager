=====
Cluster Manager
=====

Distribute jobs across workers reachable via SSH.


Workers specification
---------------------
Workers must be specified in JSON format.
The JSON root object must include a property `workers` containing an array
of objects, each of which must have the following properties:

 - `hostname`: the IP of the worker or a name that resolves to it;
 - `no_cpu`: the number of jobs that the worker should execute in parallel;
 - `username`: the name of the user that SSH uses for authentication;
 - `private_key_file`: (can be null if authentication is password based)
  the path to the private key file SSH uses for authentication;
 - `password`: (can be null if authentication is key based and the key is not encrypted)
  either the password SSH uses to authenticate the user or, if a key is provided,
  the password to decrypt the key file.

An example follows:

::

    {
      "workers": [
        {"no_cpu": 2, "hostname": "1.2.3.4", "username": "john", "password": null, "private_key_file": "~/.ssh/id_john"},
        {"no_cpu": 1, "hostname": "1.2.3.5", "username": "jack", "password": "unguessable", "private_key_file": "id_jack"},
        {"no_cpu": 4, "hostname": "1.2.3.6", "username": "judie", "password": "very_unguessable", "private_key_file": null}
      ]
    }


Jobs specification
------------------
Jobs must be specified in JSON format as well.
The root object should contain two properties: `local_preparation` (object) and `jobs` (array).

The former must contain a property `create_folders` which is an array of folders to be created.
The latter must be an array of objects specifying a job. A job is specified by:

 - `commands`: an array of commands to be executed;
 - `required_files`: an array objects containing two properties `local_path` and `remote_path`,
 each specifying a file to be copied on the worker before the commands are executed;
 - `return_files`: an array objects containing two properties `local_path` and `remote_path`,
 each specifying a file to be copied from the worker after the commands are executed;
 - `id`: a string identifying the job uniquely.

An example follows:

::

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

k
