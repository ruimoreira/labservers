import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_unbound_conf(host):
    configfile = host.file('/etc/unbound/unbound.conf')
    assert configfile.exists
    assert configfile.user == 'root'
    assert configfile.group == 'unbound'


def test_unbound_service(host):
    assert host.service('unbound').is_running
    assert host.service('unbound').is_enabled


def test_unbound_log(host):
    dnslog = host.file('/var/log/unbound')
    assert dnslog.exists
    assert dnslog.user == 'unbound'
    assert dnslog.group == 'unbound'
