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

import unittest

import timetools.synchronization.clock as sc
import timetools.synchronization.oscillator as tso
import timetools.synchronization.oscillator.noise.gaussian as tsong
import timetools.synchronization.time as st

import timetools.synchronization.compliance.frequency as tscf


class TestFrequencyCompliance( unittest.TestCase ) :
    def testFfo16Ppb1( self ) :
        timeStepSeconds = 1 / 16
        numberSamples = 1000

        clockFfoPpb = 0
        clockRmsJitterPpb = 3.0

        referenceTimeGenerator = st.referenceGenerator( timeStepSeconds )
        referenceTimeSeconds = referenceTimeGenerator.generate( numberSamples )

        clockModel = sc.ClockModel( tso.OscillatorModel( initialFfoPpb = clockFfoPpb,
                                                         noiseModel = tsong.GaussianNoise(
                                                             standardDeviationPpb = clockRmsJitterPpb,
                                                             seed = 1459 ) ) )

        localTimeSeconds, instantaneousLoFfoPpb = clockModel.generate( referenceTimeSeconds )

        analysisResult = tscf.ffo16ppbMask.evaluate( (referenceTimeSeconds, instantaneousLoFfoPpb) )

        self.assertTrue( analysisResult, 'Failed 16 ppb mask when should not have' )


    def testFfo16Ppb2( self ) :
        timeStepSeconds = 1 / 16
        numberSamples = 1000

        clockFfoPpb = 0
        clockRmsJitterPpb = 10

        referenceTimeGenerator = st.referenceGenerator( timeStepSeconds )
        referenceTimeSeconds = referenceTimeGenerator.generate( numberSamples )

        clockModel = sc.ClockModel( tso.OscillatorModel( initialFfoPpb = clockFfoPpb,
                                                         noiseModel = tsong.GaussianNoise(
                                                             standardDeviationPpb = clockRmsJitterPpb,
                                                             seed = 1459 ) ) )

        localTimeSeconds, instantaneousLoFfoPpb = clockModel.generate( referenceTimeSeconds )

        analysisResult = tscf.ffo16ppbMask.evaluate( (referenceTimeSeconds, instantaneousLoFfoPpb) )

        self.assertFalse( analysisResult, 'Passed 16 ppb mask when should not have' )


    def testGenerateThresholdMask1( self ) :
        timeStepSeconds = 1 / 16
        numberSamples = 1000

        clockFfoPpb = 0
        clockRmsJitterPpb = 0.2

        complianceThresholdPpb = 1.0

        thisMask = tscf.generateThresholdMask( complianceThresholdPpb )

        referenceTimeGenerator = st.referenceGenerator( timeStepSeconds )
        referenceTimeSeconds = referenceTimeGenerator.generate( numberSamples )

        clockModel = sc.ClockModel( tso.OscillatorModel( initialFfoPpb = clockFfoPpb,
                                                         noiseModel = tsong.GaussianNoise(
                                                             standardDeviationPpb = clockRmsJitterPpb,
                                                             seed = 1459 ) ) )

        localTimeSeconds, instantaneousLoFfoPpb = clockModel.generate( referenceTimeSeconds )

        analysisResult = thisMask.evaluate( (referenceTimeSeconds, instantaneousLoFfoPpb) )

        self.assertTrue( analysisResult, 'Failed 1 ppb mask when should not have' )


    def testGenerateThresholdMask2( self ) :
        timeStepSeconds = 1 / 16
        numberSamples = 1000

        clockFfoPpb = 0
        clockRmsJitterPpb = 3.0

        complianceThresholdPpb = 1.0

        thisMask = tscf.generateThresholdMask( complianceThresholdPpb )

        referenceTimeGenerator = st.referenceGenerator( timeStepSeconds )
        referenceTimeSeconds = referenceTimeGenerator.generate( numberSamples )

        clockModel = sc.ClockModel( tso.OscillatorModel( initialFfoPpb = clockFfoPpb,
                                                         noiseModel = tsong.GaussianNoise(
                                                             standardDeviationPpb = clockRmsJitterPpb,
                                                             seed = 1459 ) ) )

        localTimeSeconds, instantaneousLoFfoPpb = clockModel.generate( referenceTimeSeconds )

        analysisResult = thisMask.evaluate( (referenceTimeSeconds, instantaneousLoFfoPpb) )

        self.assertFalse( analysisResult, 'Passed 1 ppb mask when should not have' )


if __name__ == "__main__" :
    unittest.main( )
