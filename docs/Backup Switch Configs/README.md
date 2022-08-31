# Backup Switch Configs Using Ansible

## Setup

1. Run `ansible-galaxy collection install dellemc.os10`
2. Copy [the inventory](#code-inventory) to `inventory.yaml` and copy [the code](#backup-code) to `backup_config.yaml`.
3. 

## Code Inventory

        all:
		  children:
		    os10:
		      hosts:
		        192.168.1.96:
		          ansible_become: 'yes'
		          ansible_become_method: enable
		          ansible_command_timeout: 120
		          ansible_connection: ansible.netcommon.network_cli
		          ansible_network_os: dellemc.os10.os10
		          ansible_password: admin
		          ansible_user: admin
		    ungrouped: {}

## Backup Code

- name: Backup Config
  hosts: all
  gather_facts: false
  vars:
    backup_dir: "YOUR_DIR_HERE"
  collections:
    - dellemc.os10
  tasks:
    - name: Backup
      os10_config:
        backup: true
        backup_options:
          dir_path: "{{ backup_dir }}"