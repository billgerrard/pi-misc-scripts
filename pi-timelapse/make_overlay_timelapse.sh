#/bin/bash
#
# Create timelapse of overlay images

if [ -z "$1" ]
then
    # default to today
    #
    fd=$(/usr/bin/date +"%Y%m%d")
else
    fd=$1
fi

echo "Generating timelapse for $fd"

cd /media/pi/SeagateExternal/timelapse_images

/usr/bin/rm timelapse-wip.mp4

/usr/bin/ffmpeg -r 24 -pattern_type glob -i "overlay/${fd}/overlay-image-${fd}-*.jpg" -s hd1080 -vcodec libx264 timelapse-wip.mp4

mv timelapse-wip.mp4 "overlay-timelapse-${fd}.mp4"

#
# Cumulative timelapse
#

#/usr/bin/ffmpeg -r 24 -pattern_type glob -i "image-*.jpg" -s hd1080 -vcodec libx264 timelapse-wip.mp4
#
#mv timelapse-wip.mp4 timelapse.mp4

