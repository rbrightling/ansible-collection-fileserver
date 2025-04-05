NFS
===

Install and manage Network File System shares and services. 

Requirements
------------

Supported OS's:
 - Debian 12

Role Variables
--------------



Dependencies
------------

None

Example Playbook
----------------

```
- hosts: servers
  tasks:
    - name: "Include rbrightling.fileserver.nfs"
      ansible.builtin.include_role:
        name: "rbrightling.fileserver.nfs"
```

Testing
-------

NFS may need to be run via root `su --login` to be able to test under podman

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
