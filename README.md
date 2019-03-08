# Alsible playbooks for labservers
Repo for setting up my lab labservers this will be eventually split into different repos per role if they become too complex.
Tests are implemented using molecule and testinfra, for more information see https://molecule.readthedocs.io and https://testinfra.readthedocs.io

### Build Status
[![Build Status](https://travis-ci.org/ruimoreira/labservers.svg?branch=master)](https://travis-ci.org/ruimoreira/labservers)

## Roles

 - base_config: basic configuration of nodes
 - dns_resolver: a dns resolver implemented using unbound
 - openldap-server: openldap server, configures a fully functional openldap server
 - openldap-client: client part of the server, sets up authentication


## Supported Operative Systems

| Role           | Centos           | Debian    |
|----------------|------------------|-----------|
| base_config    | 7 only           | pending   |
| dns_resolver   | 7 only           | pending   |
| opeldap-server | 7 only           | pending   |
| opeldap-client | 7 only           | pending   |

# Openldap Server
 Implements a replication friendly server with TLS enabled, with support for the  following schemas
   - cosine
   - posixAccount
   - shadhowAccount
   - openssh-lpk-openldap

 It also handles related tasks such as logging, log rotation seLinux etc

# Openldap client
 Implements authentication using sssd and pam as authentication mechanisms for openldap enabled servers
