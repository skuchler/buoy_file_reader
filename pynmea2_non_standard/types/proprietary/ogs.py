
from ... import nmea

class OGS(nmea.FreeSentence):
    '''
    Generic OGS Response Message
    '''
    sentence_types = {}
    def __new__(_cls, sentence, data):
        '''
        Return the correct sentence type based on the first field
        '''
        sentence_type = data[0]
        name = sentence_type
        cls = _cls.sentence_types.get(name, cls)
        return super(OGS, cls).__new__(cls)


class METEO(nmea.FreeSentence):
    """ Meteo data
    """
#|-(1)-|----(2)---|-(3)--|-(4)--|-(5)-|-(6)|-(7)-|-(8)--|-(9)|-(10)|(11)|(12)|(13)-|(14)|(15)|
#$METEO,1320843808,110911,130328,268.1, 1.8,16.55,1022.6,78.2,167.5, 1.9, 2.1,265.9,120,   0
    fields = (
        ("controller unix timestamp", "unix_timestamp"),
        ("controller date MMDDYY", "date"),
        ("controller time hhmmss", "time"),
        ("WindDir", "wind_direction"),
        ("WindSpeed", "wind_speed"),
        ("Temperature", "temperature"),
        ("Air Pressure", "barometric_pressure"),
        ("Air humidity", "air_humidity"),
        ("Compass", "compass"),
        ("WindSpeed2", "wind_vectorial"),
        ("WindSpeedGust", "wind_gust_speed"),
        ("WindDirGust", "wind_gust_dir"),
        ("Number of samples", "samples"),
        ("Solar Radiance optional" "solar_radiance"),
    )

class PCO2_3(nmea.FreeSentence):
    """ PCO2 data
    """
#|-(1)--|---(2)----|-(3)--|-(4)--|------(5)----------|M-|-(6)-|-(7)-|--(8)--|(9)-|-(10)-|-(11)-|(12)|(13)|(14)|
#$PCO2-3,1490272518,032317,123518,2017/03/23 12:29:04, M,39061,24799,5693.69,54.8,30.809,27.920,1061,54.4,55.1,
    fields = (
        ("controller unix timestamp", "pco2_unix_timestamp"),
        ("controller date MMDDYY", "pco2_date"),
        ("controller time HHMMSS"),
        ("instrument date time YYYY/MM/DD hh:mm:ss"),
        ("capital M"),
        ("instrument zero A/D counts"),
        ("instrument measure A/D counts"),
        ("CO2 PPM"),
        ("Optical cell temperature"),
        ("humidity sensor mBar"),
        ("humidity sensor temperature"),
        ("gas stream pressure mBar"),
        ("IRGA detector temperature"),
        ("IRGA source temperature"),
    )


class PCO2_4(nmea.FreeSentence):
    """ PCO2 data
    """

#|-(1)--|---(2)----|-(3)--|-(4)--|--|------(5)----------|-(6)-|-(7)-|-(8)-|(9)-|(10)|(11)|(12)|(13)|(14)|(15)|(16)|(17)|(18)|
#$PCO2-4,1539158718,101018,080518, M,2018,10,10,08,00,00,54283,51166,429.0,55.0,21.3,29.1,1014,11.4,4095,2378,1777,0,0
    fields = (
        ("controller unix timestamp", "pco2_unix_timestamp"),
        ("controller date MMDDYY", "pco2_date"),
        ("controller time HHMMSS"),
        ("capital M"),
        ("instrument date time YYYY,MM,DD,hh,mm,ss"),
        ("instrument zero A/D counts"),
        ("instrument measure A/D counts"),
        ("CO2 PPM"),
        ("Average IRGA temperature"),
        ("humidity sensor mBar"),
        ("humidity sensor temperature"),
        ("gas stream pressure mBar"),
        ("Supply Voltage"),
        ("Logger temperature A/D Counts"),
        ("Analog input 1 AD counts"),
        ("Analog input 2 AD counts"),
        ("Digital input 1 logic level"),
        ("Digital input 2 logic level"),
    )

class MRDMT(nmea.FreeSentence):
    """ Radiance data
    """
#|-(1)-|----(2)---|-(3)--|-(4)--|-(5)-|-(6)-|(7)-|-(8)-|(9)|
#$MRDMT,1429522514,042015,093513,930.6,-94.0,16.4,304.5,120
    fields = (
        ("controller unix timestamp"),
        ("controller date MMDDYY"),
        ("controller time HHMMSS"),
        ("solar radiance W/m^2"),
        ("infrared radiance W/m^2"),
        ("infrared sensor temperature"),
        ("infrared radiance temperature correction W/m^2"),
        ("Number of samples"),
    )

class SBE37PO(nmea.FreeSentence):
    """ SBE37 Data
    """
#|--(1)--|----(2)---|-(3)--|-(4)--|---(5)---|---(6)---|---(7)---|--(8)--|----(9)-----|--(10)---|
#$SBE37PO,1490267118,032317,110518,  20.5572,  0.00004,    0.151,  6.148, 23 Mar 2017, 11:00:01
    fields = (
        ("controller unix timestamp"),
        ("controller date MMDDYY"),
        ("controller time hhmmss"),
        ("tttt.tttt = temperature C, ITS90"),
        ("ccc.ccccc = conductivity S m"),
        ("pppp.ppp = pressure decibars"),
        ("oo.ooo = oxygen ml l"),
        ("instrument date DD MMM YYYY"),
        ("instrument time hh:mm:ss"),
    )

class SBE37O_2(nmea.FreeSentence):
    """ SBE37 Data
    """
#|--(1)---|----(2)---|-(3)--|-(4)--|---(5)---|---(6)---|--(7)--|---(8)---|----(9)-----|--(10)---|
#$SBE37O_2,1539230718,101118,040518,  20.8683,  5.32632,  5.259,  38.6208, 11 Oct 2018, 04:00:34
    fields = (
        ("controller unix timestamp"),
        ("controller date MMDDYY"),
        ("controller time hhmmss"),
        ("tttt.tttt = temperature C, ITS90"),
        ("ccc.ccccc = conductivity S m"),
        ("oo.ooo = oxygen ml l"),
        ("ss.ssss = salinity PSU"),
        ("instrument date DD MMM YYYY"),
        ("instrument time hh:mm:ss"),
    )

class MSTAT(nmea.FreeSentence):
    """ STATUS data
    """
#$MST@T,1539116114,100918,201514,12.2,15.8,203.5,20.7,120,0,1,0
    fields = (
        ("controller unix timestamp"),
        ("controller date MMDDYY"),
        ("controller time hhmmss"),
        ("main battery"),
        ("aux battery"),
        ("current"),
        ("temperature"),
        ("number of samples"),
        ("flag 1"),
        ("flag 2"),
        ("flag 3"),
    )

class METRECX(nmea.FreeSentence):
    """ METRECX CTD data
    """
#|--(1)--|---(2)----|-(3)--|-(4)--|---(5)----|----(6)----|-(7)--|-(8)--|--(9)--|-(10)--|(11)-|(12)-|(13)-|-(14)-|-(15)-|--(16)--|-(17)--|
#$METRECX,1554373117,040419,101837,2019-04-04,09:57:17.06,42.016,11.253,0010.46,0000.85,00.19,02.18,316.8,008.00,37.729,1028.902,1497.72
    fields = (
        ("controller unix timestamp"),
        ("controller date MMDDYY"),
        ("controller time HHMMSS"),
        ("instrument date YYYY-MM-DD"),
        ("instrument time HH:MM:SS.SS"),
        ("conductivity mS/cm"),
        ("temperature °C"),
        ("pressure dBar"),
        ("turbidity NTU"),
        ("Chlorophyll 0-5V"),
        ("pH "),
        ("Oxygen umol/l"),
        ("battery voltage V"),
        ("salinity PSU"),
        ("density kg/m^3"),
        ("sound velocity m/s"),
    )
