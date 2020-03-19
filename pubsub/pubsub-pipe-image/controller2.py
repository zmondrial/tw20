#!/usr/bin/env python
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A simple 'controller' script that determines which app script to run based
on an environment variable.
"""

import os

script = os.environ['PROCESSINGSCRIPT2']

if script == 'pubsub-to-bigquery':
    os.system("python pubsub-to-bigquery2.py")
elif script == 'twitter-to-pubsub':
    os.system("python twitter-to-pubsub2.py")
else:
    print "unknown script %s" % script