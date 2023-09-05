# USING NEMO Speaker diarization

""""
! pip install wget
! apt-get install sox libsndfile1 ffmpeg
! pip install text-unidecode
BRANCH = 'r1.20.0'
! python -m pip install git+https://github.com/NVIDIA/NeMo.git@$BRANCH
! pip install torchaudio -f https://download.pytorch.org/whl/torch_stable.html
"""

import nemo.collections.asr as nemo_asr
import numpy as np
from IPython.display import Audio, display
import librosa
import os
import wget
import matplotlib.pyplot as plt
import nemo
import glob
import pprint



pp = pprint.PrettyPrinter(indent=4)