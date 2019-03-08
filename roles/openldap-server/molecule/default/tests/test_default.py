import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_server_packages(host):
    packages = ["openldap-servers", "python-ldap",
                "openldap-clients", "pyOpenSSL", "openssh-ldap"]
    for package in packages:
        assert host.package(package).is_installed


def test_ldap_db_directory(host):
    ldap_directory_location = host.file('/var/lib/ldap')
    assert ldap_directory_location.exists
    assert ldap_directory_location.user == 'ldap'
    assert ldap_directory_location.group == 'ldap'


def test_services(host):
    services = ["sssd", "slapd", "firewalld"]
    for service in services:
        assert host.service(service).is_running
        assert host.service(service).is_enabled


def test_ldap_users(host):
    ldapuser = host.user("test1")
    assert ldapuser.name == "test1"
    assert ldapuser.group == "Admin"
    assert ldapuser.shell == "/bin/bash"
    assert ldapuser.home == '/home/test1'


def test_ldap_groups(host):
    ldapgroup = host.group("Admin")
    assert ldapgroup.exists
    assert ldapgroup.gid == int('501')


def test_ldap_logging(host):
    rsyslogfile = host.file('/etc/rsyslog.conf')
    assert rsyslogfile.contains("local4.* /var/log/ldap.log")


def test_ldap_log_exists(host):
    ldaplog = host.file('/var/log/ldap.log')
    assert ldaplog.exists
    assert ldaplog.is_file
    assert ldaplog.user == 'root'
    assert ldaplog.group == 'root'


def test_nsswitch(host):
    nsswitchfile = host.file('/etc/nsswitch.conf')
    assert nsswitchfile.contains("passwd:     files sss")
    assert nsswitchfile.contains("shadow:     files sss")
    assert nsswitchfile.contains("group:      files sss")


def test_openssh_lpk_schema(host):
    lpk_schema_files = ["/etc/openldap/schema/openssh-lpk-openldap.ldif",
                        "/etc/openldap/schema/openssh-lpk-openldap.schema"]
    for schemafile in lpk_schema_files:
        assert host.file(schemafile).exists
        assert host.file(schemafile).is_file


def test_ldap_logrotate_config(host):
    ldap_logrotate = "/etc/logrotate.d/ldap"
    assert host.file(ldap_logrotate).exists
    assert host.file(ldap_logrotate).is_file
    assert host.file(ldap_logrotate).user == 'root'
    assert host.file(ldap_logrotate).group == 'root'
