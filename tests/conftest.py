import pytest
import rubrik.rubrik


@pytest.fixture(scope='module')
def rubrik_init():
    node_ip = "172.21.8.90"
    username = "pythonsdk@rangers.lab"
    password = "DummyPassword!"

    return rubrik.connect(node_ip, username, password)
