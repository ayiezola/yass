# YASS, Yet Another Subdomainer Software
# Copyright 2015 Francesco Marano (@mrnfrancesco) and individual contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def without_duplicates(args):
    if args:
        if hasattr(args, '__iter__'):
            return list(set(args))
        else:
            raise TypeError("expected iterable, got {args_type} insted".format(args_type=type(args)))
    else:
        return []