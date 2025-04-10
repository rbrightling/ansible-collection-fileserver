Ansible Collection - rbrightling.fileserver
===========================================


Fileserver system collection of roles to manage and configure base system features and security.

Roles
-----

| Roles                                                                                   | Build Status                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [nfs](https://github.com/rbrightling/ansible-collection-fileserver/tree/main/roles/nfs) | [![rbrightling.fileserver.nfs](https://github.com/rbrightling/ansible-collection-fileserver/actions/workflows/nfs.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-filesystem/actions/workflows/nfs.yml) |

Requirements
------------

Supported OS's:
  - Debian 12

Usage
-----

Install this ansible collection:

```bash
ansible-galaxy collection install rbrightling.fileserver
```

Example Playbook
----------------

```yaml
---
- hosts: localhost
  tasks:
    - include_role:
        name: rbrightling.fileserver.{{ role_name }}
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
