import torch
import torch.nn as nn
import os
from subprocess import call
from scratchai._config import home

def load_from_pth(url, fname='random', key='state_dict'):
  """
  Function to download/load the pth file and return the key mentioned.

  Arguments
  ---------
  url : str
        The url from which to download the file.
  key : str
        The key of the dict to return
  fname : str
          The name with which the file should be saved.
  Returns
  -------
  val : the type of element stored in the key (mostly torch.tensor)
        The value.
  """
  
  # TODO Download this file to a location where it doesn't need to 
  # be downloaded again and again.
  prefix = home
  if not os.path.isfile(prefix + fname + '.pth'):
    call(['wget', '-O', '{}{}.pth'.format(prefix, fname), url])
  ckpt = torch.load('{}{}.pth'.format(prefix, fname), map_location='cpu')
  return ckpt[key] if key in ckpt else ckpt



def count_modules(net:nn.Module):
  """
  TODO
  """
  allm = []
  mdict = {}
  for m in net.modules():
    name = m.__class__.__name__
    if name in allm:
      mdict[name] += 1
    else:
      allm.append(name)
      mdict[name] = 1

  return mdict

