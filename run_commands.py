#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This script can be used to distribute many jobs, each consisting of a console command, on a cluster of machines.
"""

#  ----------------------------------------------------------------------------------------------------------------------

import os
import argparse
import json
import logging
import random
from cluster_manager import ClusterManager, Job, Host, TransferableFile

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO,
                    datefmt='%a, %d %b %Y %H:%M:%S')


# ----------------------------------------------------------------------------------------------------------------------
# Load settings either from config.json or from the command line

def load_settings():
    parser = argparse.ArgumentParser(
        description='Use this script to distribute your commands over a cluster of workers.'
        )

    parser.add_argument(
        '--config-file',
        help='configuration file to use',
        default='config.json'
    )
    parser.add_argument(
        '--workers-file',
        help='json file with workers details'
    )
    args = parser.parse_args()
    return args

# ----------------------------------------------------------------------------------------------------------------------


def random_hex_string(length):
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))


def load_json(file):
    with open(file, 'r') as f:
        return json.load(f)


def prepare_local_machine(settings):
    if "local_preparation" in settings:
        if "create_folders" in settings["local_preparation"]:
            for required_directory in settings["local_preparation"]["create_folders"]:
                os.makedirs(required_directory)


def create_jobs(settings):
    jobs = []
    if "jobs" in settings:
        for job in settings["jobs"]:
            required_files = []
            commands = []
            return_files = []

            if "required_files" in job:
                for required_file in job["required_files"]:
                    req_file = TransferableFile(local_path=required_file["local_path"],
                                                remote_path=required_file["remote_path"])
                    required_files.append(req_file)

            if "return_files" in job:
                for return_file in job["return_files"]:
                    ret_file = TransferableFile(local_path=return_file["local_path"],
                                                remote_path=return_file["remote_path"])
                    return_files.append(ret_file)

            if "commands" in job:
                for command in job["commands"]:
                    commands.append(command)

            if "id" in job:
                job_id = job["id"]
            else:
                job_id = "job_{id}".format(id=random_hex_string(10))

            jobs.append(
                Job(commands=commands,
                    required_files=required_files,
                    return_files=return_files,
                    id=job_id))
    return jobs


def create_hosts(workers_settings):
    hosts = []
    for worker in workers_settings:
        host = Host(
            no_cpu=worker['no_cpu'],
            hostname=worker['hostname'],
            username=worker['username'],
            password=worker['password'],
            key_filename=worker['private_key_file']
        )
        hosts.append(host)
    return hosts


if __name__ == "__main__":
    args = load_settings()
    settings = load_json(args.config_file)
    jobs = create_jobs(settings)
    workers_settings = load_json("workers.json")
    hosts = create_hosts(args.workers_file)
    cm = ClusterManager(hosts, jobs)
    results = cm.start()
