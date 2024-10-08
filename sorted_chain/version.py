# sorted_chain
# Copyright (C) 2024 Nicco Kunzmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

try:
    from ._version import __version__, __version_tuple__, version, version_tuple
except ModuleNotFoundError:
    __version__ = version = "0.0dev0"
    __version_tuple__ = version_tuple = (0, 0, "dev0")

__all__ = [
    "__version__",
    "version",
    "__version_tuple__",
    "version_tuple",
]
