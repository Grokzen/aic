import salt.config
import salt.loader


def process_salt_interface():
    """
    Use salt-stacks grains system to extract all data.
    """
    return salt.loader.grains({'extension_modules': '', 'cachedir': ''})
