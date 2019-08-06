import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_user(host):
    u = host.user("rocketchat")

    assert u.exists
    assert u.name == "rocketchat"
    assert u.group == "rocketchat"
    assert u.shell == "/usr/bin/nologin"


def test_mongodb_repo(host):
    f = host.file("/etc/apt/sources.list.d/mongodb-org-4.0.list")

    assert f.exists
    assert f.contains("repo.mongodb.org")


def test_mongodb_pkg(host):
    p = host.package("mongodb-org")

    assert p.is_installed


def test_nodejs_repo(host):
    f = host.file("/etc/apt/sources.list.d/nodesource.list")

    assert f.exists
    assert f.contains("deb.nodesource.com")


def test_nodejs_pkg(host):
    p = host.package("nodejs")

    assert p.is_installed


def test_mongod_conf(host):
    f = host.file("/etc/mongod.conf")

    assert f.exists
    assert f.contains("engine: mmapv1")
    assert f.contains("replSetName: rs01")


def test_mongod_service(host):
    s = host.service("mongod")

    assert s.is_running


def test_mongod_socket(host):
    s = host.socket("tcp://127.0.0.1:27017")

    assert s.is_listening


def test_n_bin(host):
    f = host.file("/usr/local/bin/n")

    assert f.exists


def test_rocketchat_directory(host):
    f = host.file("/usr/local/rocketchat")

    assert f.exists
    assert f.is_directory
    assert f.user == "rocketchat"
    assert f.group == "rocketchat"


def test_rocketchat_service_file(host):
    f = host.file("/lib/systemd/system/rocketchat.service")

    assert f.exists


def test_rocketchat_service(host):
    s = host.service("rocketchat")

    assert s.is_running


def test_rocketchat_socket(host):
    s = host.socket("tcp://3000")

    assert s.is_listening
