"""
    Unlocke
    Copyright (C) 2020  Errite Games LLC/ ErriteEpticRikez
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def makeParameterArray(array_string):
    passes = 0
    param_array = []
    finished = False
    while not finished:
        if not passes == 0:
            last = current_space
            current_space = array_string.find(" ",last + 1)
        else:
            current_space = array_string.find(" ")
            end = array_string.find(" ", current_space)
        if passes == 0:
            last = 0
        if current_space == -1:
            finished = True
            param_array.append(array_string[last:len(array_string)])
        else:
            if passes == 0:
                param_array.append(array_string[0:current_space])
            elif not current_space == -1:
                param_array.append(array_string[last:current_space])
        passes = passes + 1
    return param_array