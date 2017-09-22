# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def openness(path):
  """openness

  Data loads lazily. Type data(openness) into the console.

  A data.frame with 114 rows and 12 variables:

  -  open. imports as percent GDP, '73-

  -  inf. avg. annual inflation, '73-

  -  pcinc. 1980 per capita inc., U.S. $

  -  land. land area, square miles

  -  oil. =1 if major oil producer

  -  good. =1 if 'good' data

  -  lpcinc. log(pcinc)

  -  lland. log(land)

  -  lopen. log(open)

  -  linf. log(inf)

  -  opendec. open/100

  -  linfdec. log(inf/100)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `openness.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 114 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'openness.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/wooldridge/openness.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='openness.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata