"""
Contains functions that helps in weight initialization.
"""

import torch
import torch.nn as nn
import numpy as np

from scratchai.utils import bilinear_kernel

def xavier_normal(m:nn.Module):
  """
  Xavier Normal Initialization to all the conv layers
  And the weight of batch norm is initialized to 1
  and the bias of the batch norm to 0

  Arguments
  ---------
  m : nn.Module
        The net which to init.
  """

  if isinstance(m, nn.Conv2d):
    nn.init.xavier_normal_(m.weight)
    if m.bias is not None:
      nn.init.zeros_(m.bias)
  # Add other norms (like nn.GroupNorm2d)
  elif isinstance(m, nn.BatchNorm2d):
    nn.init.constant_(m.weight, 1)
    nn.init.constant_(m.bias, 0)


def xavier_uniform(m:nn.Module):
  """
  Xavier Uniform Initialization to all the conv layers
  And the weight of batch norm is initialized to 1
  and the bias of the batch norm to 0

  Arguments
  ---------
  m : nn.Module
        The net which to init.
  """

  if isinstance(m, nn.Conv2d):
    nn.init.xavier_uniform_(m.weight)
    if m.bias is not None:
      nn.init.zeros_(m.bias)
  # Add other norms (like nn.GroupNorm2d)
  elif isinstance(m, nn.BatchNorm2d):
    nn.init.constant_(m.weight, 1)
    nn.init.constant_(m.bias, 0)


def kaiming_normal(m:nn.Module):
  """
  Kaiming Normal Initialization to all the conv layers
  And the weight of batch norm is initialized to 1
  and the bias of the batch norm to 0

  Arguments
  ---------
  m : nn.Module
        The net which to init.
  """

  if isinstance(m, nn.Conv2d):
    nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
    if m.bias is not None:
      nn.init.zeros_(m.bias)
  # Add other norms (like nn.GroupNorm2d)
  elif isinstance(m, nn.BatchNorm2d):
    nn.init.constant_(m.weight, 1)
    nn.init.constant_(m.bias, 0)


def kaiming_uniform(m:nn.Module):
  """
  Kaiming Uniform Initialization to all the conv layers
  And the weight of batch norm is initialized to 1
  and the bias of the batch norm to 0

  Arguments
  ---------
  m : nn.Module
        The net which to init.
  """

  if isinstance(m, nn.Conv2d):
    nn.init.kaiming_uniform_(m.weight, mode='fan_out', nonlinearity='relu')
    if m.bias is not None:
      nn.init.zeros_(m.bias)
  elif isinstance(m, nn.Linear):
    nn.init.zeros_(m.bias)
  # Add other norms (like nn.GroupNorm2d)
  elif isinstance(m, nn.BatchNorm2d):
    nn.init.constant_(m.weight, 1)
    nn.init.constant_(m.bias, 0)


def msr_init(m:nn.Module):
  """
  MSR Initialization to all the conv layers
  And the weight of batch norm is initialized to 1
  and the bias of the batch norm to 0

  Arguments
  ---------
  m : nn.Module
        The net which to init.
  """

  if isinstance(m, nn.Conv2d):
    n = m.kernel_size[0] * m.kernel_size[1] * m.in_channels
    nn.init.normal_(m.weight, mean=0, std=np.sqrt(2/n))
    if m.bias is not None:
      nn.init.zeros_(m.bias)
  elif isinstance(m, nn.Linear):
    nn.init.zeros_(m.bias)
  # Add other norms (like nn.GroupNorm2d)
  elif isinstance(m, nn.BatchNorm2d):
    nn.init.constant_(m.weight, 1)
    nn.init.constant_(m.bias, 0)


def dcgan_init(m:nn.Module):
  """
  Initialization as required by DCGAN.

  Arguments
  ---------
  m : nn.Module
      The layer which to init.
  """
  cname = m.__class__.__name__
  if cname.find('Conv') != -1:
    m.weight.data.normal_(0.0, 0.02)
  elif cname.find('BatchNorm') != -1:
    m.weight.data.normal_(0.1, 0.02)
    m.bias.data.fill_(0)


def zero_init(m:nn.Module):
  """
  Zero Initialization to all the conv layers

  Arguments
  ---------
  m : nn.Module
        The net which to init.
  """

  if isinstance(m, nn.Conv2d):
    m.weight.data.zero_()
    if m.bias is not None:
      nn.init.zeros_(m.bias)
  elif isinstance(m, nn.Linear):
    m.weight.data.zero_()
    if m.bias: nn.init.zeros_(m.bias)
  """
  # Add other norms (like nn.GroupNorm2d)
  elif isinstance(m, nn.BatchNorm2d):
    nn.init.constant_(m.weight, 1)
    nn.init.constant_(m.bias, 0)
  """
