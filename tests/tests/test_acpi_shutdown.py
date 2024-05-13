"""
Call "poweroff" command within VM
"""

import logging
import time
import pytest
from pycloudstack.vmparam import VM_TYPE_LEGACY, VM_STATE_SHUTDOWN, VM_TYPE_EFI, VM_TYPE_TD

__author__ = 'cpio'

LOG = logging.getLogger(__name__)


# pylint: disable=invalid-name
pytestmark = [
    pytest.mark.vm_image("latest-guest-image"),
    pytest.mark.vm_kernel("latest-guest-kernel"),
]


def test_tdvm_acpi_shutdown(vm_factory, vm_ssh_pubkey, vm_ssh_key):
    """
    Test ACPI shutdown for TD guest
    """
    LOG.info("Create TD guest")
    inst = vm_factory.new_vm(VM_TYPE_TD)
    inst.image.inject_root_ssh_key(vm_ssh_pubkey)

    # create and start VM instance
    inst.create()
    inst.start()
    assert inst.wait_for_ssh_ready()

    inst.ssh_run(["poweroff"], vm_ssh_key)

    # Sleep for a while for shutdown first
    time.sleep(5)
    assert inst.wait_for_state(VM_STATE_SHUTDOWN), "shutdown fail"

def test_efi_acpi_shutdown(vm_factory, vm_ssh_pubkey, vm_ssh_key):
    """
    Test ACPI shutdown for EFI guest
    """
    LOG.info("Create EFI guest")
    inst = vm_factory.new_vm(VM_TYPE_EFI)
    inst.image.inject_root_ssh_key(vm_ssh_pubkey)

    # create and start VM instance
    inst.create()
    inst.start()
    assert inst.wait_for_ssh_ready()

    inst.ssh_run(["poweroff"], vm_ssh_key)

    # Sleep for a while for shutdown first
    time.sleep(5)
    assert inst.wait_for_state(VM_STATE_SHUTDOWN), "shutdown fail"

def test_legacy_acpi_shutdown(vm_factory, vm_ssh_pubkey, vm_ssh_key):
    """
    Test ACPI shutdown for legacy VM
    """
    LOG.info("Create legacy guest")
    inst = vm_factory.new_vm(VM_TYPE_LEGACY)
    inst.image.inject_root_ssh_key(vm_ssh_pubkey)

    # create and start VM instance
    inst.create()
    inst.start()
    assert inst.wait_for_ssh_ready()

    inst.ssh_run(["poweroff"], vm_ssh_key)

    # Sleep for a while for shutdown first
    time.sleep(5)
    assert inst.wait_for_state(VM_STATE_SHUTDOWN), "shutdown fail"
