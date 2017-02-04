#
# Copyright 2017 Russell Smiley
#
# This file is part of timetools.
#
# timetools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# timetools is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with timetools.  If not, see <http://www.gnu.org/licenses/>.
#

class LinearTemperatureSensitivity :
    def __init__( self, temperatureSensitivityPpbPerKelvin, referenceTemperatureKelvin = 293.15 ) :
        self.__referenceTemperatureKelvin = referenceTemperatureKelvin
        self.__sensitivityPpbPerKelvin = temperatureSensitivityPpbPerKelvin


    def generate( self, referenceTemperatureKelvin ) :
        # Assume zero ppb offset at the reference temperature
        ffoPpb = (referenceTemperatureKelvin - self.__referenceTemperatureKelvin) \
                 * self.__sensitivityPpbPerKelvin

        return ffoPpb
