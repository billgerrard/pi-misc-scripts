#!/usr/bin/python3

import sys
from os import system
from datetime import date, datetime, time, timedelta

# DEBUG MODE flag
debug_mode = ''



def addSeconds(tm, sec):
    ###return datetime.combine(date.today(), tm) + timedelta(seconds=sec) # datetime
    return (datetime.combine(date.today(), tm) + timedelta(seconds=sec)).time() # time

def logger(str):
    if debug_mode == 'DEBUG':
        print(str)
    else:
        system('/usr/bin/logger "' + str +'"')

###raise SystemExit()
###sys.exit()

def main():
    from astral import LocationInfo
    city = LocationInfo("Salt Lake City", "Utah", "America/Denver", 40.54515, -112.04447)

    from astral.sun import sun
    s = sun(city.observer, date=date.today(), tzinfo=city.timezone)

    time_dawn = s["dawn"].time()
    time_dusk = s["dusk"].time()
    time_sunrise = s["sunrise"].time()
    time_sunset = s["sunset"].time()
    before_dawn = addSeconds(time_dawn, -60*30)
    before_sunrise = addSeconds(time_sunrise, -60*30)
    after_sunrise = addSeconds(time_sunrise, 60*30)
    before_sunset = addSeconds(time_sunset, -60*30)
    after_sunset = addSeconds(time_sunset, 60*30)
    after_dusk = addSeconds(time_dusk, 60*30)

    ###print("30 minutes before dawn: ",before_dawn)
    ###print("time_dawn: ",time_dawn)
    ###print("30 minutes before sunrise: ",before_sunrise)
    ###print("time_sunrise: ",time_sunrise)
    ###print("30 minutes after sunrise: ",after_sunrise)
    ###print("30 minutes before sunset: ",before_sunset)
    ###print("time_sunset: ",time_sunset)
    ###print("30 minutes after sunset: ",after_sunset)
    ###print("time_dusk: ",time_dusk)
    ###print("30 minutes after dusk: ",after_dusk)

    now = datetime.now()
    time_now = now.time()
    ###print("time_now: ", time_now)

    # Only capture photos during 'daylight' hours (dawn to dusk)
    #
    if time_now >= before_dawn and time_now <= after_dusk:

        # Normal day time: 1 image per minute
        #
        day_type = "day time"
        max_pix = 2
        
        if (time_now >= before_sunrise and time_now <= after_sunrise):
            # +/-30 minutes near sunrise: 3 images per minute
            #
            day_type = "near sunrise"
            max_pix = 4
        elif (time_now >= before_sunset and time_now <= after_sunset):
            # +/-30 minutes near sunset: 3 images per minute
            #
            day_type = "near sunset"
            max_pix = 4

        for x in range(max_pix):
            now = datetime.now()
            dt_date = now.strftime("%Y%m%d")

            tl_filepath = '/media/pi/SeagateExternal/timelapse_images/original/' + dt_date

            # create YYYYMMDD directory if it doesn't exist
            #
            import pathlib
            pathlib.Path(tl_filepath).mkdir(exist_ok=True)

            dt_filename = debug_mode + "image-" + now.strftime("%Y%m%d-%H%M%S") + ".jpg"
            logger("capture_daylight_photo: " +  day_type + ", saving " + dt_filename)

            ###tl_filepath = '/home/pi/timelapse_images/' + dt_filename
            tl_filepath = tl_filepath + '/' + dt_filename
            
            #from picamera import PiCamera
            #camera = PiCamera()
            #camera.resolution = (3280, 2464)
            #camera.capture(tl_filepath)

            time_start = datetime.now()
            ###print("time_start: ", time_start)
            system('/usr/bin/raspistill -o ' + tl_filepath)
            time_end = datetime.now()
            ###print("time_end: ", time_end)
            time_seconds = (time_end - time_start).total_seconds()

            ###print("time_seconds = ", time_seconds)
            ###print("pause time: ", int(60/max_pix - time_seconds) )

            # pause between images
            #
            import time
            ##print("pause_start: ", datetime.now() )
            time.sleep(18)
            ##print("pause_end: ", datetime.now() )

    else:
        logger("capture_daylight_photo: night time, skipping")


if __name__ == '__main__':
    main()
