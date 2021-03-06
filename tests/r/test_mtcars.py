from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mtcars import mtcars


def test_mtcars():
  """Test module mtcars.py by downloading
   mtcars.csv and testing shape of
   extracted data has 32 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mtcars(test_path)
  try:
    assert x_train.shape == (32, 11)
  except:
    shutil.rmtree(test_path)
    raise()
