import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_basic_packages(host):
    packages = ["epel-release", "bind-utils",
                "ntp", "net-tools"]
    for pack in packages:
        assert host.package(pack).is_installed


def test_basic_services(host):
    services = ["sshd", "ntpd", "firewalld"]
    for service in services:
        assert host.service(service).is_running
        assert host.service(service).is_enabled


def test_ntp_config_file(host):
    ntpf = host.file('/etc/ntp.conf')
    assert ntpf.is_file
    assert ntpf.exists
    assert ntpf.user == 'root'
    assert ntpf.group == 'root'
    assert ntpf.mode == 0644
