[![Build Status](https://travis-ci.com/UbiCastTeam/ansible-role-rocketchat.svg?branch=master)](https://travis-ci.com/UbiCastTeam/ansible-role-rocketchat)

Rocket.Chat
===========

Install and update Rocket.Chat (manual installation).

Requirements
------------

None.

Role Variables
--------------

See `defaults/main.yml`.

Dependencies
------------

None.

Example Playbook
----------------

```
- hosts: rocketchat_server
  roles:
    - role: ubicast.rocketchat
      rc_root_url: https://chat.example.net
      rc_version: 1.3.0
      rc_mail_url: mail.example.net:25
```

License
-------

BSD

Author Information
------------------

@nikaro from @UbicastTeam
