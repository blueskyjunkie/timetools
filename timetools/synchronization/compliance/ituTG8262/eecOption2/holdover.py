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

import numpy

import timetools.synchronization.compliance.analysis as tsca


a1 = 50
a2 = 300
b = 4.63e-4
c = 1000
d = 4.63e-4

phaseErrorPolynomialNs = numpy.array([c, (a1 + a2), (0.5 * b)])
ffoPolynomialPpb = numpy.array([a1 + a2, b])

# Rec. ITU-T G.8262/Y.1362 (07/2010), pp18
phaseErrorNs = tsca.Mask([ ([0], phaseErrorPolynomialNs.tolist(), 
                            (-phaseErrorPolynomialNs).tolist()) ])

ffoPpb = tsca.Mask([ ([0], ffoPolynomialPpb.tolist(), 
                      (-ffoPolynomialPpb).tolist()) ])

ffoRatePpbPerSecond = tsca.Mask([ ([0], [d], [-d]) ])
