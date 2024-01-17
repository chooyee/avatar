{"filter":false,"title":"layers.py","tooltip":"/faceutils/face_segmentation/layers.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":63,"column":16},"action":"insert","lines":["# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.","#","# Licensed under the Apache License, Version 2.0 (the \"License\");","# you may not use this file except in compliance with the License.","# You may obtain a copy of the License at","#","#    http://www.apache.org/licenses/LICENSE-2.0","#","# Unless required by applicable law or agreed to in writing, software","# distributed under the License is distributed on an \"AS IS\" BASIS,","# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.","# See the License for the specific language governing permissions and","# limitations under the License.","","import paddle","import paddle.nn as nn","import paddle.nn.functional as F","","","def SyncBatchNorm(*args, **kwargs):","    \"\"\"In cpu environment nn.SyncBatchNorm does not have kernel so use nn.BatchNorm instead\"\"\"","    if paddle.get_device() == 'cpu':","        return nn.BatchNorm(*args, **kwargs)","    else:","        return nn.SyncBatchNorm(*args, **kwargs)","","","class ConvBNReLU(nn.Layer):","    def __init__(self,","                 in_channels,","                 out_channels,","                 kernel_size,","                 padding='same',","                 **kwargs):","        super().__init__()","","        self._conv = nn.Conv2D(","            in_channels, out_channels, kernel_size, padding=padding, **kwargs)","","        self._batch_norm = SyncBatchNorm(out_channels)","","    def forward(self, x):","        x = self._conv(x)","        x = self._batch_norm(x)","        x = F.relu(x)","        return x","","","class ConvBN(nn.Layer):","    def __init__(self,","                 in_channels,","                 out_channels,","                 kernel_size,","                 padding='same',","                 **kwargs):","        super().__init__()","        self._conv = nn.Conv2D(","            in_channels, out_channels, kernel_size, padding=padding, **kwargs)","        self._batch_norm = SyncBatchNorm(out_channels)","","    def forward(self, x):","        x = self._conv(x)","        x = self._batch_norm(x)","        return x"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":63,"column":16},"end":{"row":63,"column":16},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1705474907320,"hash":"bb6ef1581e15d9195d9dd23259ae5504ab173454"}