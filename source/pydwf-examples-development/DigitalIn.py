#! /usr/bin/env python3

"""DigitalIn instrument demo.

Note: *** THIS DEMO IS STILL IN DEVELOPMENT ***
"""

import argparse

from pydwf import DwfLibrary, DwfEnumConfigInfo, PyDwfError
from pydwf.utilities import openDwfDevice


def enum_values_to_str(values):
    enum_type_name = None
    for value in values:
        if enum_type_name is None:
            enum_type_name = value.__class__.__name__
        elif enum_type_name !=  value.__class__.__name__:
            raise RuntimeError("Enum values are of different types.")
    return "{}.{{{}}}".format(enum_type_name, "|".join(value.name for value in values))


def print_digital_input_info(digitalIn):

    # 11 "Info" functions.

    print("=== digitalIn global info:")
    print()

    print("    digitalIn.internalClockInfo() ........... : {:10} [Hz]".format(digitalIn.internalClockInfo()))
    print("    digitalIn.clockSourceInfo() ............. : {}".format(enum_values_to_str(digitalIn.clockSourceInfo())))
    print("    digitalIn.dividerInfo() ................. : {}".format(digitalIn.dividerInfo()))
    print("    digitalIn.bitsInfo() .................... : {}".format(digitalIn.bitsInfo()))
    print("    digitalIn.bufferSizeInfo() .............. : {}".format(digitalIn.bufferSizeInfo()))
    print("    digitalIn.sampleModeInfo() .............. : {}".format(enum_values_to_str(digitalIn.sampleModeInfo())))
    print("    digitalIn.acquisitionModeInfo() ......... : {}".format(enum_values_to_str(digitalIn.acquisitionModeInfo())))
    print("    digitalIn.triggerPositionInfo() ......... : {}".format(digitalIn.triggerPositionInfo()))
    print("    digitalIn.triggerAutoTimeoutInfo() ...... : {}".format(digitalIn.triggerAutoTimeoutInfo()))
    print("    digitalIn.triggerInfo() ................. : {}".format(digitalIn.triggerInfo()))
    print("    digitalIn.triggerSourceInfo() ........... : {}".format(enum_values_to_str(digitalIn.triggerSourceInfo())))
    print()
    print("    NOTE: digitalIn.triggerSourceInfo() is obsolete.")
    print()


def print_digital_input_settings(digitalIn):

    # 13 "Get" functions.

    print("=== digitalIn global current settings:")
    print()
    print("    digitalIn.clockSourceGet() ............. : {}".format(digitalIn.clockSourceGet()))
    print("    digitalIn.dividerGet() ................. : {}".format(digitalIn.dividerGet()))
    print("    digitalIn.sampleFormatGet() ............ : {}".format(digitalIn.sampleFormatGet()))
    print("    digitalIn.bufferSizeGet() .............. : {}".format(digitalIn.bufferSizeGet()))
    print("    digitalIn.sampleModeGet() .............. : {}".format(digitalIn.sampleModeGet()))
    print("    digitalIn.sampleSensibleGet() .......... : {}".format(digitalIn.sampleSensibleGet()))
    print("    digitalIn.acquisitionModeGet() ......... : {}".format(digitalIn.acquisitionModeGet()))
    print("    digitalIn.triggerSourceGet() ........... : {}".format(digitalIn.triggerSourceGet()))
    print("    digitalIn.triggerSlopeGet() ............ : {}".format(digitalIn.triggerSlopeGet()))
    print("    digitalIn.triggerPositionGet() ......... : {}".format(digitalIn.triggerPositionGet()))
    print("    digitalIn.triggerPrefillGet() .......... : {}".format(digitalIn.triggerPrefillGet()))
    print("    digitalIn.triggerAutoTimeoutGet() ...... : {}".format(digitalIn.triggerAutoTimeoutGet()))
    print("    digitalIn.triggerGet() ................. : {}".format(digitalIn.triggerGet()))
    print()


def change_digital_input_settings(digitalOut):

    # 13 regular "Set" functions (with "Get" counterparts)

    # digitalIn.clockSourceSet(clock_source: DwfDigitalInClockSource)
    # digitalIn.dividerSet(div: int)
    # digitalIn.sampleFormatSet(nBits: int)
    # digitalIn.bufferSizeSet(nSize: int)
    # digitalIn.sampleModeSet(sample_mode: DwfDigitalInSampleMode)
    # digitalIn.sampleSensibleSet(compression_bits: int)
    # digitalIn.acquisitionModeSet(acquisition_mode: DwfAcquisitionMode)
    # digitalIn.triggerSourceSet(trigger_source: DwfTriggerSource)
    # digitalIn.triggerSlopeSet(trigger_slope: DwfTriggerSlope)
    # digitalIn.triggerPositionSet(samples_after_trigger: int)
    # digitalIn.triggerPrefillSet(samples_before_trigger: int)
    # digitalIn.triggerAutoTimeoutSet(secTimout: float)
    # digitalIn.triggerSet(fsLevelLow: int, fsLevelHigh: int, fsEdgeRise: int, fsEdgeFall: int)

    # 6 irregular "Set" functions (without "Get" counterparts)

    # digitalIn.inputOrderSet(dioFirst: bool)
    # digitalIn.mixedSet(enable: bool)
    # digitalIn.triggerResetSet(fsLevelLow: int, fsLevelHigh: int, fsEdgeRise: int, fsEdgeFall: int)
    # digitalIn.triggerLengthSet(secMin: float, secMax: float, idxSync: int)
    # digitalIn.triggerMatchSet(pin: int, mask: int, value: int, bitstuffing: int)
    # digitalIn.triggerCountSet(count: int, restart: int)

    pass


def demo_digital_in_instrument_api(digitalIn):

    # - 11 "Info" functions
    # - 13 "Get" functions
    # - 13 regular "Set" functions
    # -  6 irregular "Set" functions
    # -  3 reset/configure/status
    # -  9 status inquiry functions
    #
    # Total: 55 functions
    # Note: digitalIn.triggerSourceInfo and digitalIn.mixedSet() are obsolete.

    digitalIn.reset()

    print_digital_input_info(digitalIn)

    print_digital_input_settings(digitalIn)

    # digitalIn.configure(reconfigure: bool, start: bool)
    # digitalIn.status(readData: bool) -> DwfState

    # digitalIn.statusSamplesLeft() -> int
    # digitalIn.statusSamplesValid() -> int
    # digitalIn.statusIndexWrite() -> int
    # digitalIn.statusAutoTriggered() -> bool
    # digitalIn.statusData(count_bytes: int) -> np.ndarray
    # digitalIn.statusData2(first_sample: int, count_bytes: int) -> np.ndarray
    # digitalIn.statusNoise2(first_sample: int, count_bytes: int) -> np.ndarray
    # digitalIn.statusRecord() -> Tuple[int, int, int]
    # digitalIn.statusTime() -> Tuple[int, int, int]


def main():
    """Parse arguments and start demo."""

    parser = argparse.ArgumentParser(description="Demonstrate DigitalIn instrument usage.")

    parser.add_argument(
            "-sn", "--serial-number",
            type=str,
            nargs='?',
            dest="serial_number",
            help="serial number of the Digilent Waveforms device"
        )

    args = parser.parse_args()

    try:
        dwf = DwfLibrary()

        # A helper function to select the most suitable configuration.
        # Select the first configuration with the highest possible "DigitalInBufferSize" configuration parameter.
        def maximize_digital_in_buffer(configuration_parameters):
            return configuration_parameters[DwfEnumConfigInfo.DigitalInBufferSize]

        with openDwfDevice(dwf, serial_number = args.serial_number, score_func = maximize_digital_in_buffer) as device:
            demo_digital_in_instrument_api(device.digitalIn)
    except PyDwfError as exception:
        print("PyDwfError: {}".format(exception))
    except KeyboardInterrupt:
        print("Keyboard interrupt, ending demo.")


if __name__ == "__main__":
    main()
