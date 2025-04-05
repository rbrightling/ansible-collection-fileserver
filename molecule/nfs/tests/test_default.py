import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_openssh_server_installed(host):
    openssh_server_package_name = "nfs-kernel-server"
    openssh_server_package = host.package(openssh_server_package_name)
    assert openssh_server_package.is_installed


def test_openssh_service(host):
    service_name = "nfs-server"
    service = host.service(service_name)
    assert service.is_running
    assert service.is_enabled
