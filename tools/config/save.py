# Copyright 2021 Oliver Smith
# SPDX-License-Identifier: GPL-3.0-or-later
import os
import logging
import tools.config
from multiprocessing import shared_memory


def save(args, cfg):
    logging.debug("Save config: " + args.config)
    os.makedirs(os.path.dirname(args.config), 0o700, True)
    with open(args.config, "w") as handle:
        cfg.write(handle)

def save_session(cfg):
    config_path = tools.config.session_defaults["config_path"]
    logging.debug("Save session config: " + config_path)
    save_state(tools.config.stats[cfg["session"]["state"]])
    os.makedirs(os.path.dirname(config_path), 0o700, True)
    with open(config_path, "w") as handle:
        cfg.write(handle)

def init_state(state):
    session_name = tools.config.session_name
    shm_state = shared_memory.SharedMemory(name=session_name, create=True, size=1)
    shm_state.buf[0] = state
    shm_state.close()
    os.chmod("/dev/shm/" + session_name, 0o666)
    return True

def destroy_state():
    session_name = tools.config.session_name
    shm_state = shared_memory.SharedMemory(name=session_name, create=False)
    shm_state.close()
    shm_state.unlink()
    return True

def save_state(state):
    session_name = tools.config.session_name
    logging.debug("Save state: {}".format(state))
    shm_state = shared_memory.SharedMemory(name=session_name, create=False)
    shm_state.buf[0] = state
    shm_state.close()
    return True
