from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.engel import engel


def test_engel():
  """Test module engel.py by downloading
   engel.csv and testing shape of
   extracted data has 235 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = engel(test_path)
  try:
    assert x_train.shape == (235, 2)
  except:
    shutil.rmtree(test_path)
    raise()
