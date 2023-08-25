# import the mscl library
# import sys
# sys.path.append("../../dependencies/Python")
import mscl

# TODO: change these constants to match your setup
COM_PORT = "/dev/ttyACM0"


try:
    # create a Serial Connection with the specified COM Port, default baud rate of 921600
    connection = mscl.Connection.Serial(COM_PORT)

    # create an InertialNode with the connection
    node = mscl.InertialNode(connection)

    #node.setAdaptiveFilterOptions

    # many other settings are available than shown below
    # reference the documentation for the full list of commands

    # if the node supports AHRS/IMU

    if node.features().supportsCategory(mscl.MipTypes.CLASS_AHRS_IMU):
        ahrsImuChs = mscl.MipChannels()
        ahrsImuChs.append(mscl.MipChannel(mscl.MipTypes.CH_FIELD_SENSOR_SCALED_ACCEL_VEC, mscl.SampleRate.Hertz(1)))
        ahrsImuChs.append(mscl.MipChannel(mscl.MipTypes.CH_FIELD_SENSOR_SCALED_GYRO_VEC, mscl.SampleRate.Hertz(1)))
        ahrsImuChs.append(mscl.MipChannel(mscl.MipTypes.CH_FIELD_SENSOR_SCALED_MAG_VEC, mscl.SampleRate.Hertz(1)))
        
        
        # ahrsImuChs.append(mscl.MipChannel(mscl.MipTypes.CH_FIELD_SENSOR))

        # apply to the node
        node.setActiveChannelFields(mscl.MipTypes.CLASS_AHRS_IMU, ahrsImuChs)
        
    # aopt = mscl.InertialTypes.FILTERING_AGGRESIVE
    # node.setAdaptiveFilterOptions(mscl.InertialTypes.FILTERING_CONSERVATIVE)

    # if the node supports Estimation Filter
    if node.features().supportsCategory(mscl.MipTypes.CLASS_ESTFILTER):
        estFilterChs = mscl.MipChannels()
        #
        #estFilterChs.append(mscl.MipChannel(mscl.MipTypes.CH_FIELD_ESTFILTER_ESTIMATED_GYRO_BIAS, mscl.SampleRate.Hertz(1)))
        estFilterChs.append(mscl.MipChannel(mscl.MipTypes.CH_FIELD_ESTFILTER_ESTIMATED_ORIENT_EULER, mscl.SampleRate.Hertz(1)))

        # apply to the node
        node.setActiveChannelFields(mscl.MipTypes.CLASS_ESTFILTER, estFilterChs)
        print("Filter set")
    
    mcomm = mscl.MipCommands

except mscl.Error as e:
    print("Error:", e)
