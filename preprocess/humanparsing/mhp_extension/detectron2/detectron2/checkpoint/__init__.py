# Modified by Tanuj Saxena
# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# File:


from . import catalog as _UNUSED  # register the handler
from .detection_checkpoint import DetectionCheckpointer
from fvcore.common.checkpoint import Checkpointer, PeriodicCheckpointer

__all__ = ["Checkpointer", "PeriodicCheckpointer", "DetectionCheckpointer"]
